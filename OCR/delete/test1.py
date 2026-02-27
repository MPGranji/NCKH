import os
import json
import re
import pdfplumber
from pyvi import ViTokenizer

# Cấu hình đường dẫn
BASE_DIR = r"D:\NCKH"
PDF_INPUT = "Giao Trinh_Lap_Trinh_Can_Ban_A_V2.pdf"

def clean_toc_dots(text):
    return re.sub(r'\s*\.\s*\.\s*[\.\s]*\d+', '', text)

def table_to_markdown(table):
    if not table or not any(table): return ""
    clean_table = []
    for row in table:
        clean_row = [str(cell).replace('\n', ' ').strip() if cell else "" for cell in row]
        if any(clean_row): clean_table.append(clean_row)
    if not clean_table: return ""
    md = ""
    for i, row in enumerate(clean_table):
        md += "| " + " | ".join(row) + " |\n"
        if i == 0: md += "| " + " | ".join(["---"] * len(row)) + " |\n"
    return md

def process_nckh_final_v6(pdf_name):
    pdf_path = os.path.join(BASE_DIR, pdf_name)
    output_txt = os.path.join(BASE_DIR, "output.txt")
    output_md = os.path.join(BASE_DIR, "output.md")
    output_jsonl = os.path.join(BASE_DIR, "data_rag_final.jsonl")

    try:
        final_data_for_jsonl = []
        full_text_review = []

        with pdfplumber.open(pdf_path) as pdf:
            print(f"--- Đang xử lý nâng cao: {pdf_name} ---")
            
            for i, page in enumerate(pdf.pages):
                width, height = page.width, page.height
                # Bỏ qua header (top 40) và footer (bottom 50)
                safe_zone = page.within_bbox((0, 40, width, height - 50))
                page_text = safe_zone.extract_text()
                
                if not page_text: continue
                
                # Làm sạch
                clean_text = clean_toc_dots(page_text)
                clean_text = re.sub(r'[ \t]+', ' ', clean_text).strip()
                
                # Tokenize để xử lý từ ghép
                tokenized_text = ViTokenizer.tokenize(clean_text)
                
                # Lấy bảng
                tables = page.extract_tables()
                table_md = "\n".join([table_to_markdown(t) for t in tables if t])

                # Hợp nhất nội dung
                page_content = f"TRANG {i+1}\n{tokenized_text}"
                if table_md:
                    page_content += f"\n\nBẢNG BIỂU:\n{table_md}"

                full_text_review.append(page_content)
                
                # Lưu vào danh sách JSONL (giữ nguyên để làm chunk)
                final_data_for_jsonl.append({
                    "text": page_content.replace("_", " "), # Xóa gạch dưới cho AI dễ đọc
                    "metadata": {"source": pdf_name, "page": i+1}
                })

        # Xuất file TXT và MD
        with open(output_txt, "w", encoding="utf-8") as f: f.write("\n\n".join(full_text_review))
        with open(output_md, "w", encoding="utf-8") as f: f.write("# NCKH OCR RESULT\n\n" + "\n\n".join(full_text_review))
        
        # Xuất file JSONL
        with open(output_jsonl, "w", encoding="utf-8") as f:
            for item in final_data_for_jsonl:
                f.write(json.dumps(item, ensure_ascii=False) + "\n")

        print(f"--- THÀNH CÔNG! Đã lưu 3 file vào {BASE_DIR} ---")

    except Exception as e:
        print(f"Lỗi: {e}")

process_nckh_final_v6(PDF_INPUT)