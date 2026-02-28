# AI Moodle Question Generator - Project Pipeline

## Overview
An automated system that generates high-quality quiz questions using local LLMs and integrates them with Moodle LMS.

---

## Stage 1: Data Ingestion

**Input:** `sample_data.txt` (C programming course materials)

**Process:**
- File: `ingest_data.py`
- Parse document chunks with pattern: `[CHUNK X | PAGE Y]`
- Convert text to embeddings
- Store in ChromaDB with metadata (chunk ID, page number)

**Output:** Persistent ChromaDB database (`db_moodle/`)
- Ready for semantic search queries
- Indexed and optimized for vector similarity

---

## Stage 2: Model Evaluation

**Three Local LLM Models (Ollama):**
1. **Deepseek-coder-v2** - Code-specific expertise
2. **Qwen2.5:7b** - Balanced general purpose
3. **Llama3.1:8b** - Strong theory understanding

**Evaluation Tools:**
- `test_quick.py` - Compare 2 models on same topic OR 2 question types on same model
- `test_deepseek_code.py` - Compare all 3 models on code-based questions

**Automatic Quality Metrics:**
1. **Faithfulness** (0.0-1.0)
   - Does the question accurately reflect the source context?
   
2. **Relevancy** (0.0-1.0)
   - Is the question related to the specified topic?
   
3. **Quality** (0.0-1.0)
   - Is it clear, well-formatted, and pedagogically sound?

**Acceptance Threshold:** Average score ≥ 0.35

**Output:**
- Model performance comparison results
- Best-performing model per topic/question type
- Metrics dashboard for decision-making

---

## Stage 3: Question Generation & Export

**File:** `export_to_moodle.py`

**Process:**

```
For each (Topic, Model, Question Type):
  1. Query ChromaDB → Retrieve relevant context
  2. Call LLM → Generate question with options A) B) C) D)
  3. Parse answer format → Extract correct answer
  4. Evaluate 3 metrics → Check against threshold
  5. Accept/Reject based on score
```

**Configuration:**
- **Topics:** Algorithm basics, Loop structures, Functions & recursion
- **Models:** All 3 local LLMs
- **Question Types:** Theory, Code implementation

**Example:**
- Potential combinations: 3 topics × 3 models × 2 types = 18 questions
- After filtering: ~12-15 high-quality questions retained

**Output Format:** XML Aiken (Moodle standard)

```xml
<quiz>
  <question type="multichoice">
    <name>Question 1: Basic Algorithm</name>
    <questiontext format="html">
      <text>What is an algorithm?...</text>
    </questiontext>
    <answer fraction="100">
      <text>A correct definition...</text>
    </answer>
    <answer fraction="0">
      <text>Incorrect option B</text>
    </answer>
    ...
  </question>
</quiz>
```

**File:** `questions_export.xml`

---

## Stage 4: Moodle Integration

**File:** `moodle_integration.py`

**Prerequisites:**
- Moodle server URL
- Web Service Token (User > Preferences > Web Services)
- REST API enabled on Moodle

**API Wrapper Class: MoodleAPI**

**Core Functions:**
- `get_site_info()` - Test connection & retrieve server info
- `get_courses()` - List available courses
- `get_course_categories()` - Retrieve course structure
- `create_question()` - Create multichoice question in course
- `create_quiz()` - Create new quiz module
- `add_question_to_quiz()` - Link questions to quiz
- `batch_import_questions()` - Mass import from XML
- `get_enrolled_users()` - Retrieve student list
- `update_question()` / `delete_question()` - Manage questions

**Workflow:**
1. Authenticate using web service token
2. Parse questions_export.xml
3. For each question:
   - Extract text, options, correct answer
   - Call Moodle API to create question
   - Attach to specified course/quiz
4. Verify import success

**Output:** 
- Questions available in Moodle course
- Quiz ready for students to attempt
- Assessment data collected in Moodle gradebook

---

## Supporting Tools

**File:** `view_chroma.py`

**Features:**
- View ChromaDB collection statistics
- Search documents by semantic similarity
- Debug and verify ingested data quality
- Sample retrieval for validation

---

## Main Orchestrator

**File:** `main.py`

**Pipeline Functions:**
1. `print_header()` - Display welcome banner
2. `run_step_1_ingestion()` - Execute data ingestion
3. `run_step_2_evaluation()` - Run model evaluation
4. `run_step_3_export()` - Generate and export questions
5. `run_step_4_moodle_optional()` - Optional Moodle upload
6. `main()` - Orchestrate full pipeline

**Execution:**
```bash
python main.py
```

---

## Data Flow Diagram

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
            (semantic similarity query)
                      ↓
        ┌─────────────┴──────────────┐
        ↓                            ↓
  [export_to_moodle.py]      [test_*.py]
   (generate questions)     (evaluate models)
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
Quiz + Questions Ready
   for Students
```

---

## Key Dependencies

```
chromadb          - Vector database for semantic search
ollama            - Local LLM runtime
requests          - HTTP client for Moodle API
xml.etree.ElementTree - XML parsing & generation
json              - Metadata handling
re                - Regular expression parsing
```

---

## Quality Assurance

**Validation Points:**
1. ChromaDB ingestion: Verify chunk count & metadata
2. LLM generation: Check question format & completeness
3. Metric evaluation: Confirm threshold compliance
4. XML export: Validate XML structure
5. Moodle API: Test connection before upload

**Error Handling:**
- Graceful degradation on LLM timeouts
- Skip low-scoring questions
- Detailed logging for debugging
- Fallback options for failed API calls

---

## File Structure

```
AI_Moodle/
├── main.py                    # Pipeline orchestrator
├── ingest_data.py             # Data ingestion
├── export_to_moodle.py        # Question generation
├── moodle_integration.py      # Moodle API wrapper
├── test_quick.py              # Quick model comparison
├── test_deepseek_code.py      # 3-model code test
├── view_chroma.py             # ChromaDB viewer
├── data/
│   └── sample_data.txt        # Course materials
├── db_moodle/
│   ├── chroma.sqlite3         # ChromaDB database
│   └── [collection folders]   # Vector indexes
├── questions_export.xml       # Generated questions
├── README.md                  # Project documentation
├── REPORT.md                  # Comprehensive report
├── PIPELINE.md                # This file
└── requirement.txt            # Python dependencies
```

---

## Configuration

### ChromaDB Setup
```python
client = chromadb.PersistentClient(path="./db_moodle")
collection = client.get_or_create_collection(name="giao_trinh_c")
```

### Moodle Connection
```python
api = MoodleAPI(
    moodle_url="https://moodle.example.com",
    web_service_token="YOUR_TOKEN_HERE"
)
```

### LLM Models
- Access via Ollama (typically running on localhost:11434)
- Models pulled: `deepseek-coder-v2`, `qwen2.5:7b`, `llama3.1:8b`

---

## Usage Examples

### 1. Full Pipeline Execution
```bash
python main.py
```

### 2. Quick Model Comparison
```bash
python test_quick.py
# Choose: Compare 2 models or Compare 2 question types
```

### 3. Code Question Evaluation
```bash
python test_deepseek_code.py
# Compare all 3 models on code-based questions
```

### 4. View ChromaDB Contents
```bash
python view_chroma.py
# Explore ingested documents and search
```

### 5. Generate & Export Questions
```bash
python export_to_moodle.py
# Batch generate and export to questions_export.xml
```

### 6. Test Moodle Connection
```bash
python -c "from moodle_integration import test_connection; test_connection('URL', 'TOKEN')"
```

---

## Success Criteria

✓ ChromaDB successfully ingests all course materials
✓ All 3 LLM models generate questions
✓ Metrics evaluate with score ≥ 0.35 threshold
✓ XML export is valid Aiken format
✓ Moodle API connection established
✓ Questions successfully uploaded to course
✓ Quiz ready for student enrollment

---

## Troubleshooting

| Issue | Solution |
|-------|----------|
| ChromaDB not found | Ensure `ingest_data.py` ran successfully first |
| LLM timeout | Verify Ollama is running: `ollama serve` |
| Low quality scores | Review context relevance; adjust topic keywords |
| Moodle connection failed | Check URL, token validity, and network |
| XML parse error | Validate LLM output format; check special chars |
| Unicode/encoding issues | Ensure UTF-8 encoding throughout |

---

## Performance Notes

- **Ingestion Time:** ~10-30 seconds (depends on file size)
- **Per-Question Generation:** ~3-5 seconds (LLM inference)
- **Full Batch (18 questions):** ~2-3 minutes
- **Moodle Upload:** ~1-2 seconds per question

---

## Future Enhancements

- [ ] Auto-detect language in documents
- [ ] Support for additional question types (essay, matching)
- [ ] Machine learning model fine-tuning on domain data
- [ ] Difficulty estimation per question
- [ ] Student performance feedback loop
- [ ] Multi-language support
- [ ] Batch scheduling with cron jobs
- [ ] Web UI dashboard for monitoring

---

## License & Credits

Project: AI Moodle Question Generator
Status: Academic Research Project
Date: 2026
