# VectorDB (ChromaDB) - Hướng dẫn chi tiết

## VectorDB là gì?

**VectorDB** (Vector Database) = Database lưu trữ vectors + Tính toán similarity

```
Text "vòng lặp" → Embedding (768 chiều vector) → Lưu vào DB
Text "for loop" → Embedding (768 chiều vector) → So sánh similarity
```

Kết quả: Tìm kiếm theo **ý nghĩa**, không phải **keyword**

---

## 3 Thành phần chính

### 1️⃣ Ingestion (Nạp dữ liệu)
**File:** `ingest_data.py`

```
sample_data.txt
    ↓
Tách chunks [CHUNK X | TRANG Y]
    ↓
ChromaDB tự động chuyển thành embeddings
    ↓
Lưu vào db_moodle/chroma.sqlite3
```

**Chú thích chi tiết:**
- PersistentClient = Lưu trên ổ cứng
- Collection = 1 tập hợp documents
- Add documents = ChromaDB tự embedding

### 2️⃣ Search (Tìm kiếm Semantic)
**File:** `view_chroma.py`

```
Query: "vòng lặp"
    ↓
ChromaDB chuyển thành vector
    ↓
So sánh cosine similarity với tất cả documents
    ↓
Trả về top N documents gần nhất
```

**Distance Score:**
- 0.0 = Perfect match
- 0.3 = Very similar
- 0.5 = Somewhat similar
- 1.0 = Completely different

### 3️⃣ Demo (Khám phá)
**File:** `vectordb_demo.py`

```bash
python vectordb_demo.py
# Xem chi tiết cách semantic search hoạt động
```

---

## Các câu hỏi thường gặp

### ❓ VectorDB khác Collections thế nào?
**Collections** = Nhóm documents trong VectorDB
- 1 VectorDB có thể có nhiều collections
- Ví dụ: collection "giao_trinh_c" (lập trình C)

### ❓ Embeddings là gì?
**Embeddings** = Vector đại diện cho ý nghĩa của text
```
Text:  "vòng lặp"
Vector: [-0.023, 0.145, -0.089, ..., 0.234]  (768 chiều)

Text:  "for loop"  
Vector: [-0.021, 0.148, -0.092, ..., 0.231]  (768 chiều)

→ Vectors rất gần nhau = Ý nghĩa giống nhau
```

### ❓ Cosine Similarity là gì?
**Cosine Similarity** = Đo độ giống giữa 2 vectors
```
Công thức: similarity = cos(θ) = (A · B) / (|A| * |B|)

Kết quả:
  - 1.0  = Song song cùng chiều (giống 100%)
  - 0.0  = Vuông góc (không liên quan)
  - -1.0 = Ngược chiều (hoàn toàn khác)

ChromaDB dùng distance = 1 - similarity
```

### ❓ Làm sao tìm được documents liên quan?
```
Query: "vòng lặp"
  ↓ [Embedding]
Vector: [-0.023, 0.145, -0.089, ..., 0.234]
  ↓ [Cosine Similarity so với tất cả]
Scores:
  - Document 1 (for loop): 0.015 ← Gần nhất!
  - Document 2 (while loop): 0.032
  - Document 3 (iteration): 0.041
  - Document 4 (array): 0.234
  ↓ [Return top 3]
Results: [Document 1, 2, 3]
```

---

## Cách sử dụng

### 1. Nạp dữ liệu lần đầu
```bash
python ingest_data.py
# Tạo ./db_moodle/chroma.sqlite3 với 18 chunks
```

### 2. Xem & Tìm kiếm
```bash
python view_chroma.py
# Option 1: Xem collections info
# Option 2: Tìm kiếm semantic
```

### 3. Demo chi tiết
```bash
python vectordb_demo.py
# Xem cách semantic search hoạt động theo từng bước
```

### 4. Dùng trong code
```python
import chromadb

# Connect
client = chromadb.PersistentClient(path="./db_moodle")
collection = client.get_collection(name="giao_trinh_c")

# Semantic query
results = collection.query(
    query_texts=["vòng lặp"],
    n_results=5
)

# Results: {
#   'ids': [...],
#   'documents': [...],
#   'metadatas': [...],
#   'distances': [...]
# }
```

---

## VectorDB vs SQL Database

| Tính năng | SQL Database | VectorDB |
|-----------|-------------|----------|
| **Lưu trữ** | Structured tables | Documents + Vectors |
| **Tìm kiếm** | Exact match (WHERE) | Similarity search |
| **Ý nghĩa** | Không hiểu | Hiểu ý nghĩa |
| **Ứng dụng** | Quản lý data | Semantic search |

---

## Ứng dụng trong dự án

```
"Sinh câu hỏi về vòng lặp"
    ↓
1. Query ChromaDB: "vòng lặp"
    ↓
2. Lấy top 5 documents liên quan
    ↓
3. Sử dụng documents làm context
    ↓
4. Pass context + topic tới LLM
    ↓
5. LLM sinh câu hỏi dựa trên context
    ↓
6. Đánh giá chất lượng
    ↓
7. Export nếu pass threshold
```

---

## Performance

| Hoạt động | Thời gian | Chú thích |
|-----------|-----------|----------|
| Ingestion | ~5-10s | Lần đầu |
| Query | ~0.1s | Per query |
| Batch query (18) | ~2s | 18 LLM requests |

---

## Resources

- ChromaDB Docs: https://docs.trychroma.com/
- Embeddings: https://huggingface.co/docs/transformers/tasks/sentence_similarity
- Semantic Search: https://en.wikipedia.org/wiki/Semantic_search

---

## Tóm tắt

VectorDB cho phép:
1. ✅ Lưu documents + embeddings
2. ✅ Tìm kiếm theo ý nghĩa (semantic)
3. ✅ Trả về documents liên quan
4. ✅ Sử dụng làm context cho LLM

Kết quả: **Sinh câu hỏi chất lượng cao từ tài liệu!**
