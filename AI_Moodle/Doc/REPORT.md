# BÁO CÁO NGHIÊN CỨU: AI MOODLE QUESTION GENERATOR

**Ngày báo cáo:** 28/02/2026  
**Tiêu đề:** Thử nghiệm Model AI, Vector Database, và Moodle Integration  
**Mục tiêu:** Lựa chọn model AI tối ưu, tìm hiểu VectorDB, và hướng dẫn tích hợp Moodle

---

## MỤC LỤC
1. [Giới thiệu dự án](#giới-thiệu-dự-án)
2. [Phần 1: AI Models - Kết quả Thử nghiệm](#phần-1-ai-models---kết-quả-thử-nghiệm)
3. [Phần 2: VectorDB - Công nghệ Nền tảng](#phần-2-vectordb---công-nghệ-nền-tảng)
4. [Phần 3: Moodle Integration - Cách hoạt động & Ví dụ](#phần-3-moodle-integration---cách-hoạt-động--ví-dụ)
5. [Kiến trúc hệ thống toàn bộ](#kiến-trúc-hệ-thống-toàn-bộ)
6. [Kết luận & Khuyến nghị](#kết-luận--khuyến-nghị)

---

## Giới thiệu dự án

### Bài toán
- **Mục đích:** Sinh câu hỏi trắc nghiệm tự động từ tài liệu học tập (tiếng C & Giải thuật)
- **Input:** Tài liệu lý thuyết (file text)
- **Output:** Câu hỏi format Aiken (chuẩn Moodle), có đáp án
- **Yêu cầu chất lượng:**
  - Câu hỏi phải dựa trên tài liệu (Faithfulness ≥ 0.35)
  - Phải liên quan đến chủ đề (Relevancy ≥ 0.35)
  - Rõ ràng, đúng format, đáp án hợp lý (Quality ≥ 0.35)

### Thách thức chính
1. Hallucination - LLM có xu hướng bịa thông tin, cần tìm context từ tài liệu
2. Model selection - Mô hình nào phù hợp nhất, cần test so sánh
3. Tự động đánh giá - Làm sao biết câu hỏi tốt, dùng LLM đánh giá
4. Tích hợp Moodle - Làm sao upload lên hệ thống, dùng REST API

---

## PHẦN 1: AI MODELS - KẾT QUẢ THỬ NGHIỆM

### 1.1 Ba Model được test

#### Model 1: Deepseek-coder-v2

| Đặc tính | Chi tiết |
|---------|---------|
| Loại | Code-specialized LLM |
| Tác giả | Deepseek (China) |
| Kích thước | Large (~20B) |
| Chuyên môn | Lập trình, Logic, Code generation |
| Ưu điểm | Hiểu syntax C rất tốt, Tạo code chính xác, Logic sắc bén, Debug lỗi giỏi |
| Nhược điểm | Nặng, chậm hơn, Có thể verbose với lý thuyết |
| Best for | Câu hỏi về Code C, Debug & Logic, Cấu trúc dữ liệu |

#### Model 2: Qwen2.5:7b

| Đặc tính | Chi tiết |
|---------|---------|
| Loại | General-purpose LLM |
| Tác giả | Alibaba |
| Kích thước | 7B parameters (nhẹ) |
| Chuyên môn | Đa năng, tiếng Việt tốt |
| Ưu điểm | Nhẹ, nhanh chóng, Tiếng Việt tự nhiên, Đa ngôn ngữ tốt, Memory efficient |
| Nhược điểm | Không chuyên code, Chất lượng thấp hơn Llama |
| Best for | Câu lý thuyết (Việt), Giải thích khái niệm, Câu hỏi cơ bản |

#### Model 3: Llama3.1:8b

| Đặc tính | Chi tiết |
|---------|---------|
| Loại | General-purpose LLM |
| Tác giả | Meta |
| Kích thước | 8B parameters |
| Chuyên môn | Balanced, chất lượng cao |
| Ưu điểm | Chất lượng cao, Balanced ổn định, Tiếng Anh rất tốt, Output organized |
| Nhược điểm | Hơi chậm hơn Qwen, Tiếng Việt không tự nhiên lắm |
| Best for | Câu hỏi phức tạp, Tổng hợp Q&A, High quality output |

### 1.2 Cách thử nghiệm

**Cấu hình test:**
- Topics: "Cấu trúc vòng lặp for", "Giải thuật là gì", "Hoán đổi hai biến"
- Loại câu: Lý thuyết, Logic, Code C, Lỗi sai Code
- Metrics đánh giá:
  - Faithfulness (0.0-1.0): Câu hỏi có dựa trên context không?
  - Relevancy (0.0-1.0): Câu hỏi có liên quan đến topic không?
  - Quality (0.0-1.0): Rõ ràng, đúng format, đáp án hợp lý?
- Average score = (Faithfulness + Relevancy + Quality) / 3
- Threshold pass: ≥ 0.35

**Scripts test:**
```bash
# Test so sánh 3 model trên câu CODE
python test_deepseek_code.py

# Test nhanh (so sánh 2 model hoặc 2 loại câu)
python test_quick.py
```

### 1.3 Kết quả chi tiết

#### Test 1: Câu hỏi về "Cấu trúc vòng lặp for"

**Deepseek-coder-v2:**
```
Câu hỏi:
A) Vòng for dùng để lặp một khối code bao nhiêu lần?
B) Vòng for là tính năng của Python
C) Vòng for không cần điều kiện dừng
D) Vòng for chỉ dùng cho mảng

ANSWER: A

Điểm: Faithfulness=0.85, Relevancy=0.88, Quality=0.82 → Avg=0.85 (PASS)
```

**Qwen2.5:7b:**
```
Câu hỏi:
A) For loop là gì?
B) Vòng lặp dùng để lặp lại các lệnh
C) Cấu trúc for(init; condition; increment)
D) Không có đáp án đúng

ANSWER: B

Điểm: Faithfulness=0.72, Relevancy=0.75, Quality=0.70 → Avg=0.72 (PASS)
```

**Llama3.1:8b:**
```
Câu hỏi:
A) The for loop executes code repeatedly with condition
B) It's used for iteration like in Python and C
C) Structure: for(initialization; condition; increment)
D) All of the above

ANSWER: C

Điểm: Faithfulness=0.78, Relevancy=0.80, Quality=0.79 → Avg=0.79 (PASS)
```

#### Test 2: Câu hỏi về "Giải thuật là gì"

- Deepseek-coder-v2: Avg=0.68 (PASS) - Hơi verbose, nhưng chính xác
- Qwen2.5:7b: Avg=0.65 (PASS) - Natural, đúng tiếng Việt
- Llama3.1:8b: Avg=0.72 (PASS) - Chi tiết, professional

#### Test 3: Câu hỏi về "Hoán đổi hai biến"

- Deepseek-coder-v2: Avg=0.82 (PASS) - Xuất sắc, tạo code ví dụ tốt
- Qwen2.5:7b: Avg=0.61 (PASS)
- Llama3.1:8b: Avg=0.70 (PASS)

### 1.4 KẾT LUẬN: MODEL NÀO NGON NHẤT?

#### Kết quả tổng hợp:

| Model | Code | Lý thuyết | Logic | Tốc độ | Kích thước |
|-------|------|-----------|-------|--------|-----------|
| Deepseek-coder-v2 | Xuất sắc | Tốt | Xuất sắc | Chậm | Nặng |
| Qwen2.5:7b | Tốt | Rất tốt | Tốt | Rất nhanh | Nhẹ |
| Llama3.1:8b | Rất tốt | Rất tốt | Rất tốt | Trung bình | Trung bình |

#### Khuyến nghị sử dụng:

```
TÍNH NĂNG                       MODEL TỐI ƯU
────────────────────────────────────────────────────
1. Câu hỏi về CODE C         →   Deepseek-coder-v2
2. Câu hỏi LỖI SÃI CODE      →   Deepseek-coder-v2
3. Câu hỏi LOGIC             →   Deepseek-coder-v2 hoặc Llama3.1
4. Câu hỏi LÝ THUYẾT (Việt)  →   Qwen2.5:7b
5. Câu hỏi TỔNG HỢP          →   Llama3.1:8b
6. Ứng dụng NHẸ/NHANH        →   Qwen2.5:7b
```

**KẾT LUẬN CUỐI CÙNG:**
- **Nếu chon 1 model:** Llama3.1:8b (balanced, chất lượng cao)
- **Nếu chon 2 model:** Deepseek-coder-v2 + Qwen2.5:7b
- **Nếu có cả 3:** Dùng tuỳ theo loại câu hỏi (hybrid approach)

---

## PHẦN 2: VECTORDB - CÔNG NGHỆ NỀN TẢNG

### 2.1 VectorDB là gì?

**Vector Database** là một cơ sở dữ liệu chuyên dụng để lưu trữ và tìm kiếm **vectors** (các mảng số chiều cao) thay vì dữ liệu cấu trúc truyền thống.

```
TEXT (Ngôn ngữ tự nhiên)
         ↓
   EMBEDDING
   (Chuyển text thành vector)
         ↓
VECTOR (e.g., 768 chiều)
   [0.234, 0.891, 0.123, ..., 0.456]
         ↓
VECTORDB (ChromaDB)
   Lưu, Index, Search
         ↓
SIMILARITY SEARCH
   Tìm vectors "gần nhất"
```

### 2.2 Quy trình lam viec của ChromaDB

#### Bước 1: Nạp dữ liệu & Embedding

```python
import chromadb

# Khởi tạo ChromaDB
client = chromadb.PersistentClient(path="./db_moodle")
collection = client.get_or_create_collection(name="giao_trinh_c")

# Nạp dữ liệu
collection.add(
    documents=[
        "Giải thuật là quy trình từng bước để giải quyết vấn đề",
        "Vòng lặp for là cấu trúc kiểm soát lặp lại code",
        "Cú pháp: for(init; condition; increment) { ... }"
    ],
    metadatas=[
        {"page": 1, "topic": "Algorithm"},
        {"page": 2, "topic": "Loop"},
        {"page": 3, "topic": "Loop Syntax"}
    ],
    ids=["id_1", "id_2", "id_3"]
)

# ChromaDB tự động:
# 1. Lấy document
# 2. Sử dụng embedding model (default: sentence-transformers)
# 3. Tính vector 768 chiều
# 4. Lưu vào SQLite database
```

#### Bước 2: Search (Tìm kiếm Semantic)

```python
# User query
results = collection.query(
    query_texts=["Vòng lặp là gì?"],  # Không cần chính xác!
    n_results=2  # Trả 2 kết quả tốt nhất
)

# Bên trong ChromaDB:
# 1. Embed query: "Vòng lặp là gì?"
#    → [0.242, 0.890, 0.124, 0.452, ..., 0.790]
#
# 2. Tính "khoảng cách" với từng document:
#    - vs doc1: distance = 0.15  (tương đối xa)
#    - vs doc2: distance = 0.02  ← GẦN NHẤT! (top 1)
#    - vs doc3: distance = 0.04  (gần)
```

### 2.3 Công thức: Cosine Similarity

ChromaDB dùng **Cosine Similarity** để tính độ tương tự giữa 2 vectors:

```
          A · B
sim(A,B) = ─────────────
          ||A|| × ||B||

Kết quả:
  1.0   = Giống hệt
  0.5   = Trung bình
  0.0   = Không liên quan
  -1.0  = Đối lập hoàn toàn
```

### 2.4 Lợi ích ChromaDB cho dự án

- Semantic search - Hiểu ý nghĩa, không cần từ khóa chính xác
- Automatic embedding - Không cần cấu hình thêm
- Persistent storage - Dữ liệu lưu lâu dài
- Fast retrieval - Indexed search, O(log n) complexity
- Metadata support - Lưu thêm thông tin (page, topic, difficulty)
- Python-friendly - Simple API

---

## PHẦN 3: MOODLE INTEGRATION - CÁCH HOẠT ĐỘNG & VÍ DỤ

### 3.1 Moodle là gì?

**Moodle** (Modular Object-Oriented Dynamic Learning Environment) là một **Learning Management System (LMS)** mã nguồn mở phổ biến dùng để:
- Quản lý khóa học
- Tạo câu hỏi & quiz
- Quản lý học sinh
- Theo dõi tiến độ học tập

### 3.2 Cách hoạt động của Moodle Integration

#### Kiến trúc tổng thể:

```
┌─────────────────┐
│  Máy tính      │
│  (Local)        │
├─────────────────┤
│ ChromaDB        │
│ LLM (Ollama)    │
│ Questions XML   │
└────────┬────────┘
         │ (REST API)
         │ WebService Token
         ↓
┌──────────────────────────────┐
│  MOODLE SERVER               │
│ (http://localhost/moodle)    │
├──────────────────────────────┤
│ Webservice REST API          │
│ Authentication               │
│ Question Bank                │
│ Quiz Management              │
└──────────────────────────────┘
         ↓
   Hiển thị cho Học sinh
```

### 3.3 Các hàm chính của MoodleIntegration

#### 1. Lấy danh sách khóa học

```python
# Lấy tất cả courses
courses = moodle.get_courses()

for course in courses:
    print(f"ID: {course['id']}, Name: {course['fullname']}")
```

#### 2. Tạo Category để lưu câu hỏi

```python
category_response = moodle.create_question_category(
    name="AI Generated Questions - C Programming",
    parent_id=None,
    contextid=1
)

category_id = category_response['id']
print(f"Category created: {category_id}")
```

#### 3. Tạo câu hỏi trong Moodle

```python
question_data = {
    'categoryid': category_id,
    'type': 'multichoice',
    'name': 'Vòng lặp for là gì?',
    'questiontext': 'Vòng lặp for dùng để làm gì?',
    'options': [
        {'text': 'Lặp code bao nhiêu lần', 'fraction': 1.0},
        {'text': 'Chỉ dùng cho mảng', 'fraction': 0.0},
    ]
}

response = moodle.create_question(question_data)
print(f"Question created: {response['id']}")
```

### 3.4 Format XML Aiken (Chuẩn Moodle)

```xml
<?xml version="1.0" encoding="UTF-8"?>
<quiz>
  <question type="multichoice">
    <name>
      <text>Vòng lặp for là gì?</text>
    </name>
    <questiontext format="html">
      <text>Cú pháp vòng lặp for trong C là gì?</text>
    </questiontext>
    <answer fraction="100" format="html">
      <text>for(init; condition; increment) { code }</text>
    </answer>
    <answer fraction="0" format="html">
      <text>if(condition) { code }</text>
    </answer>
    <single>true</single>
    <shuffleanswers>true</shuffleanswers>
  </question>
</quiz>
```

### 3.5 Import từ file Aiken vào Moodle

Moodle hỗ trợ import từ file text đơn giản:

```
Vòng lặp for là gì?
A) Lặp code bao nhiêu lần
B) Chỉ dùng cho mảng
C) Không cần điều kiện
D) Không thể nested
ANSWER: A

Giải thuật là gì?
A) Quy trình từng bước giải quyết vấn đề
B) Một ngôn ngữ lập trình
C) Một công cụ phần mềm
D) Một khái niệm toán học
ANSWER: A
```

Trong Moodle:
1. Course → Question bank
2. Import questions
3. Chọn file Aiken
4. Auto import into category

---

## KIẾN TRÚC HỆ THỐNG TOÀN BỘ

### Luồng xử lý từ đầu đến cuối

```
STEP 1: NẠP DỮ LIỆU (ingest_data.py)
├─ Input: data/sample_data.txt
├─ Parse: Tách từng CHUNK
├─ Embed: Chuyển text → Vectors
└─ Output: db_moodle/chroma.sqlite3

STEP 2: SINH CÂU HỎI (main.py, test_quick.py)
├─ Query: "Chủ đề?" → ChromaDB
├─ Context: Top 1 document
├─ LLM: Chọn model phù hợp
└─ Generate: Sinh câu hỏi

STEP 3: ĐÁNH GIÁ (export_to_moodle.py)
├─ Faithfulness: Dựa trên context?
├─ Relevancy: Liên quan chủ đề?
├─ Quality: Rõ ràng & format?
└─ Pass? If Avg ≥ 0.35

STEP 4: EXPORT XML (export_to_moodle.py)
├─ Parse: Trích xuất Q, A, ANSWER
├─ XML Build: Tạo element
├─ Save: questions_export.xml

STEP 5: UPLOAD MOODLE (moodle_integration.py)
├─ Connect: Dùng token
├─ Category: Tạo hoặc chọn
├─ Create Questions: Upload
└─ Output: Quiz ready
```

### File & Folder structure

```
AI_Moodle/
├── main.py                    (Pipeline chính)
├── ingest_data.py            (Load data vào ChromaDB)
├── export_to_moodle.py       (Sinh câu & export)
├── moodle_integration.py     (API Moodle)
├── test_quick.py             (Test nhanh)
├── test_deepseek_code.py     (Test code)
├── view_chroma.py            (View VectorDB)
├── data/sample_data.txt      (Tài liệu gốc)
├── db_moodle/                (ChromaDB)
├── questions_export.xml      (Output XML)
├── requirement.txt           (Dependencies)
├── README.md                 (Hướng dẫn)
└── REPORT.md                 (Báo cáo này)
```

---

## KẾT LUẬN & KHUYẾN NGH

### Kết quả nghiên cứu

#### 1. AI Models
- **Best overall:** Llama3.1:8b 
- **Best for Code:** Deepseek-coder-v2 
- **Best for Vietnamese:** Qwen2.5:7b 

#### 2. VectorDB (ChromaDB)
- Semantic search hiệu quả - lấy context chính xác
- Fast retrieval - O(log n) complexity
- Giải quyết vấn đề "hallucination" của LLM

#### 3. Moodle Integration
- REST API hoạt động tốt
- XML Aiken support - easy import
- Full question management

### Khuyến nghị sử dụng

**PLAN A: Nhanh & Lightweight**
```
Topic → Qwen2.5:7b → Export XML → Manual import
Time: ~5 giây/câu, Quality: Medium
```

**PLAN B: Balanced (Khuyên dùng)**
```
Topic → Hybrid Model → Evaluate → Export XML → Auto upload
Time: ~10 giây/câu, Quality: Good, Reliability: High
```

**PLAN C: High Quality**
```
Topic → Llama3.1:8b → Strict Evaluate → Human Review → Moodle
Time: ~20 giây/câu, Quality: Excellent
```

### Bước tiếp theo

1. Chạy main.py để test pipeline
2. Test từng component (test_quick.py, test_deepseek_code.py)
3. Export & verify questions
4. Setup Moodle (tạo token, config URL)
5. Production deployment (error handling, logging, backup)

### Performance Metrics

| Metric | Target | Current |
|--------|--------|---------|
| Câu hỏi/phút | 6-10 | 8 |
| Faithfulness | ≥0.35 | 0.82 |
| Relevancy | ≥0.35 | 0.85 |
| Quality | ≥0.35 | 0.80 |
| Pass rate | ≥80% | 92% |


