"""
PIPELINE XỬ LÝ TÀI LIỆU TIẾNG VIỆT CHO RAG (NCKH)
Pipeline: PDF -> pdfplumber (Layout Aware) -> PyVi (NLP) -> Chunking -> JSONL/MD/TXT
Chatbot cứu
"""

import os
import json
import re
import logging
import pdfplumber
from pyvi import ViTokenizer

# --- CẤU HÌNH LOGGING ---
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    datefmt='%H:%M:%S'
)

class RagDataProcessor:
    def __init__(self, base_dir, input_pdf):
        self.base_dir = base_dir
        self.pdf_name = input_pdf
        self.pdf_path = os.path.join(base_dir, input_pdf)
        
        # output paths
        self.out_txt = os.path.join(base_dir, "pyvi_review.txt")
        self.out_md = os.path.join(base_dir, "pyvi_review.md")
        self.out_jsonl = os.path.join(base_dir, "data_rag_final.jsonl")

        # Đảm bảo thư mục tồn tại
        if not os.path.exists(self.base_dir):
            os.makedirs(self.base_dir)
            logging.info(f"Đã tạo thư mục: {self.base_dir}")

    def _clean_text(self, text):
        """Làm sạch các ký tự rác, mục lục và khoảng trắng thừa"""
        if not text: return ""
        # Xóa các chuỗi dấu chấm kéo dài (mục lục)
        text = re.sub(r'\s*\.\s*\.\s*[\.\s]*\d+', '', text)
        # Chuẩn hóa khoảng trắng và tab
        text = re.sub(r'[ \t]+', ' ', text)
        return text.strip()

    def _table_to_markdown(self, table):
        """Chuyển đổi dữ liệu bảng sang định dạng Markdown chuẩn"""
        if not table or not any(table): return ""
        clean_table = []
        for row in table:
            clean_row = [str(cell).replace('\n', ' ').strip() if cell else "" for cell in row]
            if any(clean_row): clean_table.append(clean_row)
        
        if not clean_table: return ""
        
        md_output = "\n"
        for i, row in enumerate(clean_table):
            md_output += "| " + " | ".join(row) + " |\n"
            if i == 0: # Thêm dòng ngăn cách header
                md_output += "| " + " | ".join(["---"] * len(row)) + " |\n"
        return md_output + "\n"

    def extract_layout_aware(self):
        """Trích xuất văn bản và bảng biểu theo trình tự đọc (Y-coordinate)"""
        final_pages_data = []
        
        try:
            with pdfplumber.open(self.pdf_path) as pdf:
                total_pages = len(pdf.pages)
                logging.info(f"Bắt đầu xử lý: {self.pdf_name} ({total_pages} trang)")

                for i, page in enumerate(pdf.pages):
                    width, height = page.width, page.height
                    
                    # Tìm và sắp xếp bảng theo tọa độ Y
                    tables = page.find_tables()
                    tables.sort(key=lambda x: x.bbox[1])
                    
                    last_y = 0
                    page_blocks = []
                    
                    for table_obj in tables:
                        top_y = max(0, last_y)
                        bottom_y = table_obj.bbox[1]
                        
                        # Trích xuất văn bản phía trên bảng (kiểm tra diện tích vùng an toàn)
                        if bottom_y > top_y + 1:
                            safe_zone = page.within_bbox((0, top_y, width, bottom_y))
                            text_segment = safe_zone.extract_text()
                            if text_segment:
                                cleaned = self._clean_text(text_segment)
                                page_blocks.append(ViTokenizer.tokenize(cleaned))
                        
                        # Chèn bảng vào đúng vị trí flow
                        page_blocks.append(self._table_to_markdown(table_obj.extract()))
                        last_y = table_obj.bbox[3]
                    
                    # Trích xuất phần văn bản cuối trang (loại bỏ vùng Footer 50px)
                    if height - 50 > last_y + 1:
                        bottom_zone = page.within_bbox((0, last_y, width, height - 50))
                        footer_text = bottom_zone.extract_text()
                        if footer_text:
                            cleaned = self._clean_text(footer_text)
                            page_blocks.append(ViTokenizer.tokenize(cleaned))
                    
                    full_content = "\n".join(page_blocks)
                    final_pages_data.append({
                        "review": full_content,
                        "rag_base": full_content.replace("_", " "),
                        "page": i + 1
                    })
                    
                    if (i + 1) % 20 == 0:
                        logging.info(f"Tiến độ: {i+1}/{total_pages} trang")

            return final_pages_data
        except Exception as e:
            logging.error(f"Lỗi khi trích xuất PDF: {e}")
            return []

    def save_outputs(self, data):
        """Ghi dữ liệu ra các định dạng Review (MD/TXT) và RAG (JSONL)"""
        if not data: return

        # 1. Ghi file Review (Dành cho con người đọc kiểm tra)
        try:
            with open(self.out_txt, "w", encoding="utf-8") as ft, \
                 open(self.out_md, "w", encoding="utf-8") as fm:
                fm.write(f"# TÀI LIỆU REVIEW NCKH: {self.pdf_name}\n\n")
                for d in data:
                    ft.write(f"--- TRANG {d['page']} ---\n{d['review']}\n\n")
                    fm.write(f"## TRANG {d['page']}\n{d['review']}\n\n---\n\n")
            logging.info("Đã xuất file Review (.txt, .md)")
        except Exception as e:
            logging.error(f"Lỗi khi ghi file review: {e}")

        # 2. Chia Chunk thông minh và ghi file JSONL (Dành cho AI)
        self._smart_chunking_and_save(data)

    def _smart_chunking_and_save(self, data, size=1200, overlap=200):
        """Chia nhỏ văn bản có gối đầu (overlap) để nạp vào Vector Database"""
        rag_output_list = []
        
        for d in data:
            text = d["rag_base"]
            p_num = d["page"]
            
            if len(text) <= size:
                rag_output_list.append({
                    "text": text,
                    "metadata": {"source": self.pdf_name, "page": p_num, "chunk_id": len(rag_output_list)+1}
                })
            else:
                start = 0
                while start < len(text):
                    end = start + size
                    # Ưu tiên ngắt chunk tại dấu chấm câu
                    if end < len(text):
                        last_dot = text.rfind('.', start, end)
                        if last_dot != -1 and last_dot > start + (size // 2):
                            end = last_dot + 1
                    
                    chunk = text[start:end].strip()
                    if len(chunk) > 30:
                        rag_output_list.append({
                            "text": chunk,
                            "metadata": {"source": self.pdf_name, "page": p_num, "chunk_id": len(rag_output_list)+1}
                        })
                    start += (size - overlap)

        try:
            with open(self.out_jsonl, "w", encoding="utf-8") as fj:
                for item in rag_output_list:
                    fj.write(json.dumps(item, ensure_ascii=False) + "\n")
            logging.info(f"Đã tạo thành công {len(rag_output_list)} chunks vào JSONL")
        except Exception as e:
            logging.error(f"Lỗi khi ghi file JSONL: {e}")

if __name__ == "__main__":
    # Khởi tạo Processor
    processor = RagDataProcessor(
        base_dir=r"D:\NCKH", 
        input_pdf="Giao Trinh_Lap_Trinh_Can_Ban_A_V2.pdf"
    )
    
    #Pipeline
    extracted_data = processor.extract_layout_aware()
    processor.save_outputs(extracted_data)
    
    print("\n" + "="*50)
    print("HOÀN TẤT")
    print("="*50)