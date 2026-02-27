import os
import json
import re
import logging
import pdfplumber
from pyvi import ViTokenizer

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

class RagDataProcessor:
    def __init__(self, base_dir, input_pdf):
        self.base_dir = base_dir
        self.pdf_name = input_pdf
        self.pdf_path = os.path.join(base_dir, input_pdf)
        
        # Output paths
        self.out_txt = os.path.join(base_dir, "pyvi_review.txt")
        self.out_md = os.path.join(base_dir, "pyvi_review.md")
        self.out_jsonl = os.path.join(base_dir, "data_rag_final.jsonl")

        if not os.path.exists(self.base_dir):
            os.makedirs(self.base_dir)

    def _clean_text(self, text):
        if not text: return ""
        text = re.sub(r'\s*\.\s*\.\s*[\.\s]*\d+', '', text)
        text = re.sub(r'[ \t]+', ' ', text)
        return text.strip()

    def _table_to_markdown(self, table):
        if not table or not any(table): return ""
        clean_table = []
        for row in table:
            clean_row = [str(cell).replace('\n', ' ').strip() if cell else "" for cell in row]
            if any(clean_row): clean_table.append(clean_row)
        
        if not clean_table: return ""
        md_output = "\n"
        for i, row in enumerate(clean_table):
            md_output += "| " + " | ".join(row) + " |\n"
            if i == 0:
                md_output += "| " + " | ".join(["---"] * len(row)) + " |\n"
        return md_output + "\n"

    def extract_layout_aware(self):
        """Giữ nguyên logic tọa độ Y của bạn để bóc văn bản + bảng"""
        final_pages_data = []
        try:
            with pdfplumber.open(self.pdf_path) as pdf:
                for i, page in enumerate(pdf.pages):
                    width, height = page.width, page.height
                    tables = page.find_tables()
                    tables.sort(key=lambda x: x.bbox[1])
                    
                    last_y = 0
                    page_blocks = []
                    
                    for table_obj in tables:
                        top_y = max(0, last_y)
                        bottom_y = table_obj.bbox[1]
                        
                        if bottom_y > top_y + 1:
                            safe_zone = page.within_bbox((0, top_y, width, bottom_y))
                            text_segment = safe_zone.extract_text()
                            if text_segment:
                                cleaned = self._clean_text(text_segment)
                                # NLP: Tokenize bằng PyVi cho từng đoạn văn
                                page_blocks.append(ViTokenizer.tokenize(cleaned))
                        
                        # Chèn bảng (Markdown)
                        page_blocks.append(self._table_to_markdown(table_obj.extract()))
                        last_y = table_obj.bbox[3]
                    
                    # Xử lý phần footer
                    if height - 50 > last_y + 1:
                        bottom_zone = page.within_bbox((0, last_y, width, height - 50))
                        footer_text = bottom_zone.extract_text()
                        if footer_text:
                            cleaned = self._clean_text(footer_text)
                            page_blocks.append(ViTokenizer.tokenize(cleaned))
                    
                    full_content = "\n".join(page_blocks)
                    final_pages_data.append({
                        "content_pyvi": full_content, # Bản có dấu _ để review
                        "content_clean": full_content.replace("_", " "), # Bản sạch để nạp RAG
                        "page": i + 1
                    })
            return final_pages_data
        except Exception as e:
            logging.error(f"Lỗi: {e}")
            return []

    def save_outputs(self, data):
        if not data: return

        # 1. Xuất file Review (TXT & MD) - Dùng bản Tokenized (có dấu _)
        with open(self.out_txt, "w", encoding="utf-8") as ft, \
             open(self.out_md, "w", encoding="utf-8") as fm:
            fm.write(f"# REVIEW NCKH: {self.pdf_name}\n\n")
            for d in data:
                ft.write(f"--- TRANG {d['page']} ---\n{d['content_pyvi']}\n\n")
                fm.write(f"## TRANG {d['page']}\n{d['content_pyvi']}\n\n---\n\n")

        # 2. Chia Chunk và xuất JSONL - Dùng bản Clean
        self._smart_chunking_save(data)

    def _smart_chunking_save(self, data, size=1200, overlap=200):
        rag_output_list = []
        for d in data:
            text = d["content_clean"]
            start = 0
            while start < len(text):
                end = start + size
                if end < len(text):
                    last_dot = text.rfind('.', start, end)
                    if last_dot != -1 and last_dot > start + (size // 2):
                        end = last_dot + 1
                
                chunk = text[start:end].strip()
                if len(chunk) > 30:
                    rag_output_list.append({
                        "text": chunk,
                        "metadata": {"source": self.pdf_name, "page": d["page"]}
                    })
                start += (size - overlap)

        with open(self.out_jsonl, "w", encoding="utf-8") as fj:
            for item in rag_output_list:
                fj.write(json.dumps(item, ensure_ascii=False) + "\n")
        logging.info("Đã xuất xong cả 3 định dạng: TXT, MD, JSONL!")

if __name__ == "__main__":
    processor = RagDataProcessor(base_dir=r"D:\NCKH", input_pdf="Giao Trinh_Lap_Trinh_Can_Ban_A_V2.pdf")
    extracted_data = processor.extract_layout_aware()
    processor.save_outputs(extracted_data)