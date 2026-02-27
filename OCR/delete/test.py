import pdfplumber
import json
import re
from pyvi import ViTokenizer

def clean_toc_dots(text):
    # Xóa các chuỗi dấu chấm kéo dài đến số trang (ví dụ: ... ... 148)
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
        if i == 0:
            md += "| " + " | ".join(["---"] * len(row)) + " |\n"
    return md

def process_pro_rag_v6(pdf_path, output_name="data_rag_final"):
    try:
        final_chunks = []
        with pdfplumber.open(pdf_path) as pdf:
            print(f"--- Đang xử lý: {pdf_path} ---")
            
            for i, page in enumerate(pdf.pages):
                # LẤY TỌA ĐỘ TRANG
                width, height = page.width, page.height
                # Định nghĩa vùng an toàn: bỏ qua 50 pixel dưới cùng (thường là số trang)
                footer_limit = height - 50 
                
                # Trích xuất text trong vùng an toàn (crop trang)
                safe_zone = page.within_bbox((0, 40, width, footer_limit))
                page_text = safe_zone.extract_text()
                
                if not page_text: continue
                
                # 1. Xóa dấu chấm mục lục rác
                clean_text = clean_toc_dots(page_text)
                
                # 2. Làm sạch khoảng trắng và Tokenize
                clean_text = re.sub(r'[ \t]+', ' ', clean_text).strip()
                tokenized_text = ViTokenizer.tokenize(clean_text)
                
                # 3. Lấy Bảng
                tables = page.extract_tables()
                table_md_list = [table_to_markdown(t) for t in tables if t]
                
                # 4. Gom dữ liệu
                content = f"[CHUNK {i+1} | TRANG {i+1}]\n{tokenized_text}"
                if table_md_list:
                    content += f"\n[BẢNG TRANG {i+1}]:\n" + "\n".join(table_md_list)
                
                final_chunks.append(content)

        # XUẤT FILE TXT
        with open(f"{output_name}_review.txt", "w", encoding="utf-8") as f_txt:
            f_txt.write("\n\n".join(final_chunks))

        print(f"--- Đã dọn sạch số trang và dấu chấm! Kiểm tra file: {output_name}_review.txt ---")

    except Exception as e:
        print(f"Lỗi: {e}")

process_pro_rag_v6("Giao Trinh_Lap_Trinh_Can_Ban_A_V2.pdf")