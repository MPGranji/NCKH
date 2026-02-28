# AI Moodle Question Generator - Pipeline Dự Án

## Tổng quan
Hệ thống tự động sinh câu hỏi trắc nghiệm chất lượng cao từ tài liệu giáo trình sử dụng local LLMs và tích hợp với Moodle LMS.

---

## Giai đoạn 1: Nạp dữ liệu

**Input:** `sample_data.txt` (Tài liệu giáo trình lập trình C)

**Quy trình:**
- File: `ingest_data.py`
- Parse chunks với pattern: `[CHUNK X | TRANG Y]`
- Chuyển đổi text thành embeddings
- Lưu vào ChromaDB với metadata (chunk ID, trang)

**Output:** Database ChromaDB lưu trữ (`db_moodle/`)
- Sẵn sàng truy vấn semantic
- Indexed và tối ưu cho vector similarity

---

## Giai đoạn 2: Đánh giá Model

**Ba Local LLM Models (Ollama):**
1. **Deepseek-coder-v2** - Chuyên ngành code
2. **Qwen2.5:7b** - Balanced mục đích chung
3. **Llama3.1:8b** - Lý thuyết và giải thích

**Công cụ đánh giá:**
- `test_quick.py` - So sánh 2 model cùng topic hoặc 2 loại câu cùng model
- `test_deepseek_code.py` - So sánh tất cả 3 models trên câu code

**Metrics đánh giá tự động:**
1. **Faithfulness** (0.0-1.0)
   - Câu hỏi có dựa trên context không?
   
2. **Relevancy** (0.0-1.0)
   - Câu hỏi có liên quan đến topic không?
   
3. **Quality** (0.0-1.0)
   - Câu hỏi có rõ ràng, đúng format không?

**Ngưỡng chấp nhận:** Score trung bình >= 0.35

**Output:**
- Kết quả so sánh hiệu suất model
- Model tốt nhất per topic/loại câu
- Dashboard metrics để ra quyết định

---

## Giai đoạn 3: Sinh & Export câu hỏi

**File:** `export_to_moodle.py`

**Quy trình:**

```
Cho mỗi (Topic, Model, Question Type):
  1. Query ChromaDB → Lấy context liên quan
  2. Gọi LLM → Sinh câu với options A) B) C) D)
  3. Parse format → Trích đáp án đúng
  4. Evaluate 3 metrics → Kiểm tra ngưỡng
  5. Chấp nhận/Bỏ dựa trên score
```

**Cấu hình:**
- **Topics:** Giải thuật cơ bản, Vòng lặp, Hàm & đệ quy
- **Models:** Tất cả 3 local LLMs
- **Question Types:** Lý thuyết, Code thực hành

**Ví dụ:**
- Tổ hợp tiềm năng: 3 topics × 3 models × 2 loại = 18 câu
- Sau lọc: ~12-15 câu có chất lượng cao

**Định dạng Output:** XML Aiken (chuẩn Moodle)

```xml
<quiz>
  <question type="multichoice">
    <name>Câu hỏi 1: Giải thuật cơ bản</name>
    <questiontext format="html">
      <text>Giải thuật là gì?...</text>
    </questiontext>
    <answer fraction="100">
      <text>Định nghĩa đúng...</text>
    </answer>
    <answer fraction="0">
      <text>Option B sai</text>
    </answer>
    ...
  </question>
</quiz>
```

**File:** `questions_export.xml`

---

## Giai đoạn 4: Tích hợp Moodle

**File:** `moodle_integration.py`

**Điều kiện tiên quyết:**
- URL server Moodle
- Web Service Token (User > Preferences > Web Services)
- REST API enabled trên Moodle

**API Wrapper Class: MoodleAPI**

**Các hàm chính:**
- `get_site_info()` - Test kết nối & lấy thông tin server
- `get_courses()` - Lấy danh sách khóa học
- `get_course_categories()` - Lấy cấu trúc khóa học
- `create_question()` - Tạo câu hỏi trong course
- `create_quiz()` - Tạo module quiz
- `add_question_to_quiz()` - Liên kết câu vào quiz
- `batch_import_questions()` - Import hàng loạt
- `get_enrolled_users()` - Lấy danh sách học viên
- `update_question()` / `delete_question()` - Quản lý câu

**Workflow:**
1. Xác thực bằng web service token
2. Parse questions_export.xml
3. Cho mỗi câu hỏi:
   - Trích text, options, đáp án đúng
   - Gọi API Moodle tạo câu hỏi
   - Gắn vào course/quiz
4. Xác minh upload thành công

**Output:** 
- Câu hỏi có sẵn trong course Moodle
- Quiz sẵn cho học viên
- Dữ liệu đánh giá thu trong gradebook

---

## Công cụ hỗ trợ

**File:** `view_chroma.py`

**Tính năng:**
- Xem thống kê collection ChromaDB
- Tìm kiếm documents theo semantic similarity
- Debug và xác minh chất lượng dữ liệu đã nạp
- Lấy mẫu để kiểm tra

---

## Orchestrator chính

**File:** `main.py`

**Các function pipeline:**
1. `print_header()` - Hiển thị banner
2. `run_step_1_ingestion()` - Thực hiện nạp dữ liệu
3. `run_step_2_evaluation()` - Chạy đánh giá model
4. `run_step_3_export()` - Sinh và export câu hỏi
5. `run_step_4_moodle_optional()` - Upload tùy chọn
6. `main()` - Orchestrate toàn bộ pipeline

**Thực thi:**
```bash
python main.py
```

---

## Biểu đồ luồng dữ liệu

```
                    sample_data.txt
                          ↓
                  [ingest_data.py]
                          ↓
    ┌─────────────────ChromaDB─────────────────┐
    │         (Embedded documents)             │
    │      db_moodle/chroma.sqlite3           │
    └─────────────────┬───────────────────────┘
                      ↓
            (truy vấn semantic similarity)
                      ↓
        ┌─────────────┴──────────────┐
        ↓                            ↓
  [export_to_moodle.py]      [test_*.py]
   (sinh câu hỏi)          (đánh giá model)
        ↓                            ↓
   ┌────────────┬────────────┐      ├─ Metrics
   ↓            ↓            ↓      ├─ Scores
Deepseek    Qwen2.5      Llama3.1   └─ Rankings
(LLM calls + evaluation metrics)
        ↓
   [Quality Filter: avg ≥ 0.35]
        ↓
 questions_export.xml (Aiken format)
        ↓
[moodle_integration.py]
   (REST API)
        ↓
   Moodle Server
        ↓
Quiz + Câu hỏi sẵn
   cho học viên
```

---

## Dependencies chính

```
chromadb          - Vector database cho semantic search
ollama            - Local LLM runtime
requests          - HTTP client cho Moodle API
xml.etree.ElementTree - XML parsing & generation
json              - Metadata handling
re                - Regular expression parsing
```

---

## Đảm bảo chất lượng

**Các điểm kiểm tra:**
1. ChromaDB ingestion: Xác minh số chunk & metadata
2. LLM generation: Kiểm tra format & tính hoàn chỉnh
3. Metric evaluation: Xác nhận compliance ngưỡng
4. XML export: Validate XML structure
5. Moodle API: Test kết nối trước upload

**Xử lý lỗi:**
- Graceful degradation khi LLM timeout
- Bỏ qua câu score thấp
- Logging chi tiết để debug
- Fallback options cho failed API calls

---

## Cấu trúc file

```
AI_Moodle/
├── main.py                    # Orchestrator pipeline
├── ingest_data.py             # Nạp dữ liệu
├── export_to_moodle.py        # Sinh & export câu
├── moodle_integration.py      # API wrapper Moodle
├── test_quick.py              # So sánh model nhanh
├── test_deepseek_code.py      # Test 3 model code
├── view_chroma.py             # Viewer ChromaDB
├── data/
│   └── sample_data.txt        # Tài liệu học
├── db_moodle/
│   ├── chroma.sqlite3         # Database ChromaDB
│   └── [collection folders]   # Vector indexes
├── questions_export.xml       # Câu hỏi sinh ra
├── README.md                  # Hướng dẫn nhanh
├── REPORT.md                  # Báo cáo toàn diện
├── PIPELINE.md                # File này
└── requirement.txt            # Python dependencies
```

---

## Cấu hình

### ChromaDB Setup
```python
client = chromadb.PersistentClient(path="./db_moodle")
collection = client.get_or_create_collection(name="giao_trinh_c")
```

### Kết nối Moodle
```python
api = MoodleAPI(
    moodle_url="https://moodle.example.com",
    web_service_token="YOUR_TOKEN_HERE"
)
```

### LLM Models
- Truy cập qua Ollama (thường chạy trên localhost:11434)
- Models được pull: `deepseek-coder-v2`, `qwen2.5:7b`, `llama3.1:8b`

---

## Ví dụ sử dụng

### 1. Chạy toàn bộ pipeline
```bash
python main.py
```

### 2. So sánh model nhanh
```bash
python test_quick.py
# Chọn: So sánh 2 models hoặc So sánh 2 loại câu
```

### 3. Đánh giá câu code
```bash
python test_deepseek_code.py
# So sánh tất cả 3 models trên câu code
```

### 4. Xem dữ liệu ChromaDB
```bash
python view_chroma.py
# Khám phá documents đã nạp và tìm kiếm
```

### 5. Sinh & Export câu hỏi
```bash
python export_to_moodle.py
# Sinh batch và export ra questions_export.xml
```

### 6. Test kết nối Moodle
```bash
python -c "from moodle_integration import test_connection; test_connection('URL', 'TOKEN')"
```

---

## Tiêu chí thành công

✓ ChromaDB nạp thành công tất cả tài liệu
✓ Tất cả 3 LLM model sinh câu hỏi
✓ Metrics đánh giá với score >= 0.35
✓ XML export là định dạng Aiken hợp lệ
✓ Kết nối API Moodle được thiết lập
✓ Câu hỏi upload thành công vào course
✓ Quiz sẵn cho học viên

---

## Khắc phục sự cố

| Vấn đề | Giải pháp |
|--------|----------|
| ChromaDB không tìm thấy | Đảm bảo `ingest_data.py` chạy trước |
| LLM timeout | Xác minh Ollama chạy: `ollama serve` |
| Score thấp | Xem lại context relevance, điều chỉnh topic |
| Moodle connection failed | Kiểm tra URL, token hợp lệ, mạng |
| XML parse error | Validate LLM output format, ký tự đặc biệt |
| Unicode/encoding issues | Đảm bảo UTF-8 encoding toàn bộ |

---

## Ghi chú hiệu suất

- **Nạp dữ liệu:** ~10-30 giây (tùy kích thước file)
- **Sinh 1 câu:** ~3-5 giây (LLM inference)
- **Batch 18 câu:** ~2-3 phút
- **Upload Moodle:** ~1-2 giây/câu

---

## Nâng cấp trong tương lai

- [ ] Tự động phát hiện ngôn ngữ trong documents
- [ ] Hỗ trợ loại câu hỏi bổ sung (essay, matching)
- [ ] Fine-tune model ML trên domain data
- [ ] Ước lượng độ khó cho mỗi câu
- [ ] Feedback loop từ hiệu suất học viên
- [ ] Hỗ trợ đa ngôn ngữ
- [ ] Tự động schedule với cron jobs
- [ ] Web UI dashboard để monitoring

---

## License & Credits

Project: AI Moodle Question Generator
Trạng thái: Dự án Nghiên cứu học tập
Năm: 2026
