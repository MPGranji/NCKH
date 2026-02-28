"""
========================================================
  VECTORDB INGESTION - NẠP DỮ LIỆU VÀO CHROMADB
========================================================

VectorDB (ChromaDB) là một vector database cho phép:
  1. Lưu trữ text + embeddings (vector hóa)
  2. Tìm kiếm semantic (tìm ý nghĩa, không phải keyword)
  3. Lấy context liên quan khi sinh câu hỏi

Quy trình:
  Text → Embedding (chuyển thành vector 768 chiều)
       → Lưu vào ChromaDB
       → Query khi cần context liên quan
"""

import chromadb
import re

# ========================================================
# BƯỚC 1: KHỞI TẠO CHROMADB
# ========================================================

# PersistentClient = Lưu data trên ổ cứng (không phải RAM)
# path="./db_moodle" = Tạo folder db_moodle nếu chưa có
# Lợi ích: Dữ liệu không mất khi tắt chương trình
client = chromadb.PersistentClient(path="./db_moodle")

# get_or_create_collection = Lấy hoặc tạo collection mới
# name="giao_trinh_c" = Tên collection để quản lý
# Collection = 1 tập hợp documents
collection = client.get_or_create_collection(name="giao_trinh_c")


def ingest():
    """
    Hàm nạp dữ liệu từ file text vào ChromaDB
    
    Quy trình:
      1. Đọc file sample_data.txt
      2. Tách thành chunks theo cấu trúc [CHUNK X | TRANG Y]
      3. ChromaDB tự động chuyển mỗi chunk thành vector (embedding)
      4. Lưu vector + metadata vào database
    """
    
    # ========================================================
    # BƯỚC 2: ĐỌC FILE LÀM DỮ LIỆU
    # ========================================================
    
    with open("./data/sample_data.txt", "r", encoding="utf-8") as f:
        content = f.read()
    
    # ========================================================
    # BƯỚC 3: TÁCH CHUNKS
    # ========================================================
    
    # Dữ liệu được đánh dấu: [CHUNK 1 | TRANG 5] ... text ... [CHUNK 2 | TRANG 6]
    # Tách theo pattern regex để lấy text của mỗi chunk
    chunks = re.split(r'\[CHUNK \d+ \| TRANG \d+\]', content)
    
    # Lấy chunk ID và page number từ metadata
    # Ví dụ: [CHUNK 1 | TRANG 5] → chunk: "1", page: "5"
    metadata_raw = re.findall(r'\[CHUNK (\d+) \| TRANG (\d+)\]', content)
    
    # Bỏ chunk rỗng ở đầu
    if chunks[0].strip() == "": 
        chunks.pop(0)

    # ========================================================
    # BƯỚC 4: THÊM DOCUMENTS VÀO CHROMADB
    # ========================================================
    
    for i, text in enumerate(chunks):
        c_id, p_num = metadata_raw[i]
        
        # ChromaDB tự động:
        #   1. Chuyển text thành embeddings (vector hóa)
        #   2. Lưu vector vào database
        #   3. Tạo index để tìm kiếm nhanh
        collection.add(
            documents=[text.strip()],  # Text nội dung chunk
            metadatas=[{
                "chunk": c_id,         # Chunk ID để track
                "page": p_num          # Page để referral
            }],
            ids=[f"id_{c_id}"]        # Unique ID mỗi document
        )
    
    print(f"✓ Đã nạp xong {len(chunks)} chunks vào ChromaDB!")
    print(f"  Location: ./db_moodle/chroma.sqlite3")
    print(f"  Collection: giao_trinh_c")
    print(f"  Sẵn sàng cho semantic search!")


if __name__ == "__main__":
    ingest()
