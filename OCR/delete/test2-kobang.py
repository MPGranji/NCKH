import os
import json
import re
import pdfplumber
from pyvi import ViTokenizer

BASE_DIR = r"D:\NCKH"
PDF_INPUT = "Giao Trinh_Lap_Trinh_Can_Ban_A_V2.pdf"

def table_to_markdown(table):
    if not table or not any(table): return ""
    clean_table = []
    for row in table:
        clean_row = [str(cell).replace('\n', ' ').strip() if cell else "" for cell in row]
        if any(clean_row): clean_table.append(clean_row)
    if not clean_table: return ""
    md = "\n"
    for i, row in enumerate(clean_table):
        md += "| " + " | ".join(row) + " |\n"
        if i == 0: md += "| " + " | ".join(["---"] * len(row)) + " |\n"
    return md + "\n"

def process_nckh_final_v9():
    pdf_path = os.path.join(BASE_DIR, PDF_INPUT)
    out_txt = os.path.join(BASE_DIR, "pyvi_review.txt")
    out_md = os.path.join(BASE_DIR, "pyvi_review.md")
    out_jsonl = os.path.join(BASE_DIR, "data_rag_final.jsonl")

    try:
        final_docs = []
        with pdfplumber.open(pdf_path) as pdf:
            print(f"--- Đang trích xuất (Bản sửa lỗi Zero Area) ---")
            
            for i, page in enumerate(pdf.pages):
                width, height = page.width, page.height
                tables_found = page.find_tables()
                tables_found.sort(key=lambda x: x.bbox[1])
                
                last_y = 0
                page_content_blocks = []
                
                for table_obj in tables_found:
                    # Kiểm tra diện tích vùng text trước khi trích xuất
                    top_y = max(0, last_y)
                    bottom_y = table_obj.bbox[1]
                    
                    if bottom_y > top_y + 1: # Chỉ lấy nếu vùng có chiều cao > 1 pixel
                        upper_zone = page.within_bbox((0, top_y, width, bottom_y))
                        upper_text = upper_zone.extract_text()
                        if upper_text:
                            txt = re.sub(r'\s*\.\s*\.\s*[\.\s]*\d+', '', upper_text)
                            txt = re.sub(r'[ \t]+', ' ', txt).strip()
                            page_content_blocks.append(ViTokenizer.tokenize(txt))
                    
                    # Thêm bảng
                    page_content_blocks.append(table_to_markdown(table_obj.extract()))
                    last_y = table_obj.bbox[3]
                
                # Đoạn text cuối trang
                if height - 50 > last_y + 1:
                    lower_zone = page.within_bbox((0, last_y, width, height - 50))
                    lower_text = lower_zone.extract_text()
                    if lower_text:
                        txt = re.sub(r'\s*\.\s*\.\s*[\.\s]*\d+', '', lower_text)
                        txt = re.sub(r'[ \t]+', ' ', txt).strip()
                        page_content_blocks.append(ViTokenizer.tokenize(txt))
                
                page_text_flow = "\n".join(page_content_blocks)
                final_docs.append({
                    "review": page_text_flow,
                    "rag": page_text_flow.replace("_", " "),
                    "metadata": {"source": PDF_INPUT, "page": i+1}
                })
                print(f"Xong trang {i+1}/{len(pdf.pages)}")

        # GHI FILE
        with open(out_txt, "w", encoding="utf-8") as ft, open(out_md, "w", encoding="utf-8") as fm:
            for d in final_docs:
                ft.write(f"--- TRANG {d['metadata']['page']} ---\n{d['review']}\n\n")
                fm.write(f"## TRANG {d['metadata']['page']}\n{d['review']}\n\n---\n")

        with open(out_jsonl, "w", encoding="utf-8") as fj:
            for d in final_docs:
                fj.write(json.dumps({"text": d["rag"], "metadata": d["metadata"]}, ensure_ascii=False) + "\n")

        print("\n" + "="*40 + "\nHOÀN THÀNH MIÊN MÃN!\n" + "="*40)

    except Exception as e:
        print(f"Lỗi: {e}")

if __name__ == "__main__":
    process_nckh_final_v9()