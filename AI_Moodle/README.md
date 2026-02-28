# AI Moodle Question Generator

Hệ thống tự động sinh câu hỏi trắc nghiệm chất lượng cao từ tài liệu giáo trình và tích hợp với Moodle LMS.

## Tính năng

- Nạp dữ liệu từ file text vào ChromaDB Vector Database
- Sinh câu hỏi tự động từ 3 local LLM models (Qwen2.5, Llama3.1, Deepseek-coder-v2)
- Đánh giá chất lượng câu hỏi tự động (faithfulness, relevancy, quality)
- Export câu hỏi sang format XML Aiken cho Moodle
- Tích hợp API với Moodle (tùy chọn)

## Bắt đầu nhanh

### 1. Chuẩn bị

```bash
# Cài đặt dependencies
pip install -r requirement.txt

# Pull local models (nếu chưa có)
ollama pull qwen2.5:7b
ollama pull llama3.1:8b
ollama pull deepseek-coder-v2

# Khởi động Ollama
ollama serve
```

### 2. Chạy Pipeline chính

```bash
python main.py
```

Pipeline sẽ tự động thực hiện:
1. Nạp dữ liệu - Load tài liệu vào ChromaDB
2. Sinh câu hỏi - Sinh câu từ các model khác nhau
3. Đánh giá chất lượng - Kiểm tra từng câu hỏi
4. Export XML - Lưu câu hỏi vào `questions_export.xml`

### 3. Chạy các bước riêng lẻ

#### A. Nạp dữ liệu
```bash
python ingest_data.py
```
- Đọc `data/sample_data.txt`
- Tách thành chunks theo cấu trúc `[CHUNK X | TRANG Y]`
- Lưu vào ChromaDB tại `db_moodle/`

#### B. So sánh model nhanh
```bash
python test_quick.py
```
Menu tùy chọn:
- So sánh 2 model trên cùng topic
- So sánh 2 loại câu hỏi trên cùng model

#### C. Test câu hỏi code
```bash
python test_deepseek_code.py
```
- So sánh cả 3 models trên câu hỏi code
- Hiển thị báo cáo hiệu suất chi tiết

#### D. Sinh & Export câu hỏi
```bash
python export_to_moodle.py
```
- Sinh câu hỏi từ tất cả topic
- Lọc theo điểm chất lượng (> 0.35)
- Export ra `questions_export.xml` định dạng Aiken

#### E. Xem dữ liệu ChromaDB
```bash
python view_chroma.py
```
- Duyệt collections và documents
- Tìm kiếm theo semantic similarity
- Debug dữ liệu đã nạp

#### F. Tích hợp Moodle API (tùy chọn)
```bash
python moodle_integration.py
```
- Kiểm tra kết nối Moodle
- Lấy danh sách khóa học
- Upload câu hỏi qua REST API

## Cấu trúc dự án

```
AI_Moodle/
├── main.py                    # Orchestrator pipeline chính
├── ingest_data.py             # Module nạp dữ liệu
├── test_quick.py              # Tool so sánh model nhanh
├── test_deepseek_code.py      # Đánh giá câu hỏi code
├── export_to_moodle.py        # Sinh câu & export XML
├── moodle_integration.py      # API wrapper cho Moodle
├── view_chroma.py             # Viewer ChromaDB
├── data/
│   └── sample_data.txt        # Tài liệu giáo trình
├── db_moodle/                 # Lưu trữ ChromaDB
│   ├── chroma.sqlite3
│   └── [collection folders]
├── questions_export.xml       # Câu hỏi đã sinh (tạo sau khi chạy)
├── README.md                  # File này
├── REPORT.md                  # Báo cáo toàn diện (tiếng Việt)
├── PIPELINE.md                # Hướng dẫn workflow chi tiết (tiếng Anh)
└── requirement.txt            # Python dependencies
```

## Các module chính

### main.py
Orchestrator chính cho toàn bộ pipeline.

**Các function:**
- `print_header()` - Hiển thị banner chào mừng
- `run_step_1_ingestion()` - Thực hiện nạp dữ liệu
- `run_step_2_evaluation()` - Chạy đánh giá model
- `run_step_3_export()` - Sinh và export câu hỏi
- `run_step_4_moodle_optional()` - Upload tùy chọn lên Moodle

### ingest_data.py
Nạp tài liệu giáo trình vào ChromaDB để tìm kiếm semantic.

**Các function chính:**
- `ingest()` - Parse chunks và lưu embeddings

### export_to_moodle.py
Sinh câu hỏi và export định dạng Aiken.

**Các function chính:**
- `generate_question()` - Sinh và đánh giá một câu hỏi
- `evaluate_score()` - Tính 3 metrics chất lượng
- `export_to_aiken()` - Tạo XML định dạng Aiken
- `batch_generate()` - Sinh batch câu hỏi

### moodle_integration.py
API wrapper REST cho Moodle.

**Các method chính:**
- `get_site_info()` - Test kết nối
- `get_courses()` - Lấy danh sách khóa học
- `create_question()` - Tạo câu hỏi trong course
- `create_quiz()` - Tạo module quiz
- `batch_import_questions()` - Import hàng loạt

### test_quick.py & test_deepseek_code.py
Tool so sánh và đánh giá model.

**Tính năng:**
- So sánh models trên cùng topic
- So sánh loại câu hỏi trên cùng model
- Sinh báo cáo hiệu suất chi tiết

### view_chroma.py
Utility để khám phá ChromaDB.

**Tính năng:**
- Xem thống kê collection
- Tìm kiếm theo semantic similarity
- Lấy mẫu document để kiểm tra

## Metrics đánh giá chất lượng

Hệ thống sử dụng 3 metrics tự động để đánh giá câu hỏi:

| Metric | Mô tả | Thang điểm |
|--------|-------|-----------|
| Faithfulness | Câu hỏi có dựa trên context không? | 0.0 - 1.0 |
| Relevancy | Câu hỏi có liên quan đến topic không? | 0.0 - 1.0 |
| Quality | Câu hỏi có rõ ràng, đúng format không? | 0.0 - 1.0 |

**Ngưỡng chấp nhận:** Điểm trung bình >= 0.35

## Định dạng câu hỏi

Câu hỏi được sinh định dạng Aiken (chuẩn Moodle):

```
Nêu khái niệm của biến trong lập trình C?
A) Tên vùng bộ nhớ
B) Địa chỉ bộ nhớ
C) Kiểu dữ liệu
D) Giá trị khởi tạo

ANSWER: A
```

## Tích hợp Moodle

### Cách 1: Upload thủ công (Khuyến cáo)
1. Đăng nhập vào Moodle
2. Vào Course → Settings → Question bank → Import
3. Chọn file: `questions_export.xml`
4. Định dạng import: **Aiken**
5. Click "Upload and import"

### Cách 2: Upload qua API (Nâng cao)
1. Cấu hình Moodle Web Services (xem phần bên dưới)
2. Chạy:
```bash
python moodle_integration.py
```
3. Nhập URL Moodle, token và course ID
4. API tự động upload câu hỏi

## Cấu hình Moodle Web Services

Cho Cách 2 (API upload):

1. **Bật Web Services** (Admin)
   - Site Administration → Advanced features
   - Check "Enable web services"

2. **Tạo Service**
   - Site Administration → Plugins → Web services → Manage services
   - Service name: "AI Question Generator"
   - Check "Enable service"
   - Check "Generate token"

3. **Tạo Token**
   - Site Administration → Plugins → Web services → Manage tokens
   - Tạo token và copy để dùng trong script

## Khắc phục sự cố

| Lỗi | Giải pháp |
|-----|----------|
| "Data not found for topic" | Chạy `python ingest_data.py` trước để nạp dữ liệu |
| "Model not found" | Đảm bảo Ollama đang chạy với `ollama serve` |
| "Aiken format parse error" | Kiểm tra output LLM theo format A) B) C) D) ANSWER: |
| "Moodle API connection failed" | Kiểm tra URL, token hợp lệ, kết nối mạng |
| "Low quality scores" | Điều chỉnh từ khóa topic hoặc thử model khác |
| "Unicode/encoding issues" | Đảm bảo UTF-8 encoding trên toàn bộ |

## Hiệu suất

- Nạp dữ liệu: ~10-30 giây (tùy kích thước file)
- Sinh một câu hỏi: ~3-5 giây (LLM inference)
- Batch 18 câu: ~2-3 phút
- Upload Moodle API: ~1-2 giây/câu

## Các model LLM

Hệ thống sử dụng ba model LLM open-source qua Ollama:

1. **Deepseek-coder-v2** - Chuyên ngành code generation và phân tích
2. **Qwen2.5:7b** - Mục đích chung balanced với reasoning mạnh
3. **Llama3.1:8b** - Hiệu suất tốt trên lý thuyết và giải thích

## Luồng dữ liệu

```
sample_data.txt
    ↓
[ingest_data.py]
    ↓
ChromaDB (Embedded documents)
    ↓
[Query by topic]
    ↓
[export_to_moodle.py] + [test_*.py]
    ↓
LLM Models (Ollama)
    ↓
[Evaluate metrics]
    ↓
[Filter by score]
    ↓
questions_export.xml (Aiken format)
    ↓
[moodle_integration.py]
    ↓
Moodle Server
    ↓
Quiz sẵn sàng cho học viên
```

## Tài liệu tham khảo

- [PIPELINE.md](PIPELINE.md) - Hướng dẫn workflow chi tiết (tiếng Anh)
- [REPORT.md](REPORT.md) - Báo cáo dự án toàn diện (tiếng Việt)
- [Moodle Aiken Format](https://docs.moodle.org/402/en/Aiken_format)
- [Moodle Web Services](https://docs.moodle.org/402/en/Web_services)
- [ChromaDB Documentation](https://docs.trychroma.com/)
- [Ollama Models](https://ollama.ai/library)

## Yêu cầu

Xem `requirement.txt` để biết Python dependencies:
- chromadb
- ollama
- requests
- xml.etree.ElementTree (built-in)
- re (built-in)
- json (built-in)

## Tác giả

AI Moodle Question Generator Project

## License

MIT License

---

Để biết chi tiết về workflow dự án, xem [PIPELINE.md](PIPELINE.md).
Để xem báo cáo toàn diện, xem [REPORT.md](REPORT.md).
