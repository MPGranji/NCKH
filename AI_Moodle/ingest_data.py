import chromadb
import re

# 1. Khởi tạo ChromaDB lưu vào thư mục 'db_moodle' trên máy bạn
client = chromadb.PersistentClient(path="./db_moodle")
collection = client.get_or_create_collection(name="giao_trinh_c")

def ingest():
    with open("./data/sample_data.txt", "r", encoding="utf-8") as f:
        content = f.read()

    # Tách dữ liệu theo cấu trúc [CHUNK X | TRANG Y]
    chunks = re.split(r'\[CHUNK \d+ \| TRANG \d+\]', content)
    metadata_raw = re.findall(r'\[CHUNK (\d+) \| TRANG (\d+)\]', content)
    
    if chunks[0].strip() == "": chunks.pop(0)

    for i, text in enumerate(chunks):
        c_id, p_num = metadata_raw[i]
        collection.add(
            documents=[text.strip()],
            metadatas=[{"chunk": c_id, "page": p_num}],
            ids=[f"id_{c_id}"]
        )
    print(f"✅ Đã nạp xong {len(chunks)} dữ liệu vào ChromaDB!")

if __name__ == "__main__":
    ingest()