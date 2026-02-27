# 🤖 AI Moodle Question Generator

Hệ thống tự động sinh câu hỏi trắc nghiệm từ tài liệu giáo trình và tích hợp với Moodle LMS.

## 📋 Tính năng

- ✅ Nạp dữ liệu từ file text vào ChromaDB Vector Database
- ✅ Sinh câu hỏi tự động từ 3 local LLM models (qwen2.5, llama3.1, deepseek-coder)
- ✅ Đánh giá chất lượng câu hỏi (faithfulness, relevancy, quality)
- ✅ Export câu hỏi sang format XML Aiken cho Moodle
- ✅ Tích hợp API với Moodle (tùy chọn)

## 🚀 Cách sử dụng

### 1. Chuẩn bị

```bash
# Cài đặt dependencies
pip install -r requirement.txt

# Pull local models (nếu chưa có)
ollama pull qwen2.5:7b
ollama pull llama3.1:8b
ollama pull deepseek-coder-v2
```

### 2. Chạy Pipeline Chính

```bash
python main.py
```

Pipeline sẽ tự động thực hiện:
1. **Nạp dữ liệu** - Load giáo trình vào ChromaDB
2. **Sinh câu hỏi** - Sinh 4 dạng câu hỏi từ các model khác nhau
3. **Đánh giá** - Kiểm tra chất lượng của mỗi câu hỏi
4. **Export XML** - Lưu câu hỏi sang file `questions_export.xml`

### 3. Chạy các bước riêng lẻ

#### A. Nạp dữ liệu
```bash
python ingest_data.py
```
- Đọc `data/sample_data.txt`
- Tách thành chunks theo cấu trúc `[CHUNK X | TRANG Y]`
- Lưu vào ChromaDB tại `db_moodle/`

#### B. Sinh & Đánh giá (thử nghiệm)
```bash
python test_experiment_eval.py
```
- Sinh 4 dạng câu hỏi
- Đánh giá chất lượng bằng 3 metrics
- Hiển thị bảng tóm tắt kết quả

#### C. Export sang XML
```bash
python export_to_moodle.py
```
- Sinh câu hỏi từ 4 topics
- Lọc những câu đạt chuẩn (score > 0.35)
- Export ra file `questions_export.xml`

#### D. Tích hợp Moodle API (tùy chọn)
```bash
python moodle_integration.py
```
- Hiển thị hướng dẫn cấu hình Moodle Web Services
- Cho phép upload câu hỏi trực tiếp qua API

## 📂 Cấu trúc dự án

```
AI_Moodle/
├── main.py                      # Pipeline chính
├── ingest_data.py              # Nạp dữ liệu vào ChromaDB
├── test_experiment_eval.py      # Thử nghiệm và đánh giá
├── export_to_moodle.py         # Export sang XML
├── moodle_integration.py        # Tích hợp Moodle API
├── data/
│   └── sample_data.txt         # Dữ liệu giáo trình
├── db_moodle/                  # ChromaDB storage
│   ├── chroma.sqlite3
│   └── [uuid]/
├── questions_export.xml        # Output: Câu hỏi XML (tạo sau khi chạy)
└── requirement.txt             # Dependencies
```

## 🔧 Các file chính

### `main.py`
Orchestrator chính - chạy toàn bộ pipeline 4 bước

**Models sử dụng:**
- `qwen2.5:7b` - Sinh câu hỏi lý thuyết, tốt với tiếng Việt
- `llama3.1:8b` - Sinh câu hỏi logic, tốt với reasoning
- `deepseek-coder-v2` - Sinh câu hỏi code, tốt với lập trình

### `export_to_moodle.py`
Chuyển đổi câu hỏi sang XML format Moodle

**Hàm chính:**
- `generate_questions()` - Sinh + đánh giá 1 câu hỏi
- `create_moodle_xml()` - Tạo XML format Moodle
- `export_to_file()` - Lưu file XML

### `moodle_integration.py`
Kết nối với Moodle qua REST API

**Sử dụng:**
```python
from moodle_integration import MoodleIntegration

moodle = MoodleIntegration(
    moodle_url="http://localhost/moodle",
    token="your_token_here"
)

# Test kết nối
moodle.test_connection()

# Lấy danh sách khóa học
courses = moodle.get_courses()
```

## 📊 Metrics Đánh giá

Hệ thống sử dụng 3 metrics để đánh giá chất lượng câu hỏi:

| Metric | Mô tả | Thang điểm |
|--------|-------|-----------|
| **Faithfulness** | Câu hỏi có dựa trên context không? | 0.0 - 1.0 |
| **Relevancy** | Câu hỏi có liên quan đến topic không? | 0.0 - 1.0 |
| **Quality** | Câu hỏi có rõ ràng, đúng format không? | 0.0 - 1.0 |

**Ngưỡng lọc**: Score trung bình > 0.35 mới được export

## 📝 Format Câu hỏi

Câu hỏi được sinh theo format **Aiken** (chuẩn Moodle):

```
Nêu khái niệm của biến trong lập trình C?
A) Tên vùng bộ nhớ
B) Địa chỉ bộ nhớ
C) Kiểu dữ liệu
D) Giá trị khởi tạo

ANSWER: A
```

## 🔌 Tích hợp Moodle

### Cách 1: Upload thủ công (Khuyến cáo)
1. Đăng nhập Moodle
2. Vào Course → Settings → Question bank → Import
3. Chọn file: `questions_export.xml`
4. Import format: **Aiken**
5. Click "Upload and import"

### Cách 2: Upload qua API (Nâng cao)
1. Setup Moodle Web Services (xem `moodle_integration.py`)
2. Chạy:
```bash
python moodle_integration.py
```
3. Nhập Moodle URL, Token, Course ID
4. API sẽ tự động upload câu hỏi

## 📋 Cấu hình Moodle Web Services

**Cho Cách 2 (API):**

1. **Enable Web Services** (Admin)
   - Site Administration → Advanced features
   - ✓ Enable web services

2. **Tạo Service**
   - Site Administration → Plugins → Web services → Manage services
   - Name: "AI Question Generator"
   - ✓ Enable service
   - ✓ Token generated

3. **Add Functions**
   - core_course_get_courses
   - core_question_create_questions
   - core_question_get_categories

4. **Tạo Token**
   - Site Administration → Plugins → Web services → Manage tokens
   - Copy token và dùng trong script

## 🐛 Troubleshooting

### Lỗi: "Không tìm thấy dữ liệu cho topic"
- Kiểm tra file `data/sample_data.txt` có tồn tại không
- Chạy `python ingest_data.py` trước

### Lỗi: "Model không tìm thấy"
- Kiểm tra ollama đang chạy không
- Chạy `ollama serve` trong terminal khác
- Pull model: `ollama pull qwen2.5:7b`

### Lỗi: "Không parse được format Aiken"
- Model đang sinh câu hỏi không đúng format
- Thử tăng prompt specificity hoặc đổi model khác
- Giảm eval_threshold nếu cần

### Lỗi: "Moodle API connection failed"
- Kiểm tra Moodle URL có đúng không
- Kiểm tra Web Services có enable không
- Token có hợp lệ không
- Firewall có block không

## 📈 Kết quả

Sau khi chạy xong, bạn sẽ có:

- ✅ 4 câu hỏi trắc nghiệm
- ✅ File `questions_export.xml` sẵn sàng import
- ✅ Log thử nghiệm chi tiết
- ✅ Bảng tóm tắt scores

**Ví dụ output:**
```
📊 BẢNG ĐIỂM
Loại          Model              Trung thực  Liên quan  Chất lượng  Trung bình
─────────────────────────────────────────────────────────────────────────────
Lý thuyết     qwen2.5:7b         0.80        0.00       0.60       0.47
Logic         llama3.1:8b        0.50        0.50       0.60       0.53
Code C        deepseek-coder-v2  0.00        0.50       0.70       0.40
Lỗi sai Code  deepseek-coder-v2  0.00        0.50       0.80       0.43
─────────────────────────────────────────────────────────────────────────────
TB CHUNG                          0.33        0.38       0.68       0.46
```

## 🔄 Quy trình tự động

```
Tài liệu PDF/Text
       ↓
   Nạp vào ChromaDB
       ↓
 Truy vấn theo topic
       ↓
 Sinh câu hỏi (3 models)
       ↓
   Đánh giá chất lượng
       ↓
  Lọc câu đạt chuẩn
       ↓
   Export XML Aiken
       ↓
  Import vào Moodle
       ↓
  Sinh bài kiểm tra
```

## 📚 Tài liệu tham khảo

- [Moodle Aiken Format](https://docs.moodle.org/402/en/Aiken_format)
- [Moodle Web Services](https://docs.moodle.org/402/en/Web_services)
- [ChromaDB Documentation](https://docs.trychroma.com/)
- [Ollama Models](https://ollama.ai/library)

## 👨‍💻 Tác giả

Xây dựng cho dự án AI tích hợp Moodle

## 📄 License

MIT License
