import chromadb
import ollama
import time
import re
import xml.etree.ElementTree as ET
from xml.dom import minidom

# Kết nối ChromaDB
client = chromadb.PersistentClient(path="./db_moodle")
collection = client.get_collection(name="giao_trinh_c")

def evaluate_faithfulness(context, generated_text, eval_model="qwen2.5:7b"):
    """Đánh giá độ trung thực"""
    prompt = f"""Đánh giá xem câu hỏi sau có dựa trên thông tin từ context cung cấp không.
Context: {context[:300]}...
Câu hỏi: {generated_text[:300]}...

Trả lời bằng một số từ 0.0 đến 1.0.
Chỉ trả lời số thôi."""
    
    try:
        response = ollama.generate(model=eval_model, prompt=prompt, stream=False)
        score_text = response['response'].strip()
        score = float(''.join(c for c in score_text if c.isdigit() or c == '.')[:3])
        return min(1.0, max(0.0, score / 10 if score > 1 else score))
    except:
        return 0.5

def evaluate_relevancy(topic, generated_text, eval_model="llama3.1:8b"):
    """Đánh giá độ liên quan"""
    prompt = f"""Đánh giá xem câu hỏi sau có liên quan đến chủ đề '{topic}' không.
Câu hỏi: {generated_text[:300]}...

Trả lời bằng một số từ 0.0 đến 1.0.
Chỉ trả lời số thôi."""
    
    try:
        response = ollama.generate(model=eval_model, prompt=prompt, stream=False)
        score_text = response['response'].strip()
        score = float(''.join(c for c in score_text if c.isdigit() or c == '.')[:3])
        return min(1.0, max(0.0, score / 10 if score > 1 else score))
    except:
        return 0.5

def evaluate_quality(generated_text, question_type, eval_model="qwen2.5:7b"):
    """Đánh giá chất lượng câu hỏi"""
    prompt = f"""Đánh giá chất lượng câu hỏi trắc nghiệm ({question_type}) sau:
{generated_text[:300]}...

Tiêu chí: Rõ ràng, đúng format, đáp án hợp lý.
Trả lời bằng số từ 0.0 đến 1.0.
Chỉ trả lời số thôi."""
    
    try:
        response = ollama.generate(model=eval_model, prompt=prompt, stream=False)
        score_text = response['response'].strip()
        score = float(''.join(c for c in score_text if c.isdigit() or c == '.')[:3])
        return min(1.0, max(0.0, score / 10 if score > 1 else score))
    except:
        return 0.5

def extract_aiken_format(question_text):
    """
    Trích xuất format Aiken từ text sinh bởi LLM
    Parse linh hoạt: tìm câu hỏi (dòng "Câu hỏi: ..."), 4 đáp án, và ANSWER
    """
    import re
    
    lines = question_text.strip().split('\n')
    
    question = None
    options = {}
    answer = None
    
    # Tìm dòng câu hỏi - dòng bắt đầu với "Câu hỏi:" hoặc "Question:"
    for idx, line in enumerate(lines):
        line_clean = line.strip()
        
        # Pattern: "Câu hỏi: ..." hoặc "Question: ..."
        if re.match(r'^(Câu hỏi|Question|câu hỏi):\s*', line_clean):
            # Extract phần sau "Câu hỏi:"
            question = re.sub(r'^(Câu hỏi|Question|câu hỏi):\s*', '', line_clean)
            break
        # Nếu không tìm được, lấy dòng đầu tiên > 10 ký tự
        elif len(line_clean) > 10 and not re.match(r'^[A-D]\)', line_clean) and '?' in line_clean:
            question = line_clean
            break
    
    # Fallback: nếu vẫn không tìm được, lấy dòng đầu tiên + 100 ký tự
    if not question:
        for line in lines:
            line = line.strip()
            if len(line) > 10 and not re.match(r'^[A-D]\)', line) and not line.startswith('['):
                question = line[:100]
                break
    
    if not question:
        question = "Câu hỏi trắc nghiệm"
    
    # Tìm các đáp án - pattern: A) ..., A. ..., A: ...
    for line in lines:
        line = line.strip()
        
        for opt_char in ['A', 'B', 'C', 'D']:
            # Pattern 1: A) ..., A. ..., A: ...
            if re.match(rf'^{opt_char}[\)\.:\s]', line):
                text = re.sub(rf'^{opt_char}[\)\.:\s]+', '', line).strip()
                text = re.sub(r'^\[.*?\]\s*', '', text)  # Xóa checkbox
                text = re.sub(r'^\(.*?\)\s*', '', text)  # Xóa parentheses
                if text and len(text) > 2:
                    options[opt_char] = text
            
            # Pattern 2: - [A] ... hoặc - [ ] ...
            elif re.match(rf'^-\s*\[.*?{opt_char}.*?\]', line):
                text = re.sub(r'^-\s*\[.*?\]', '', line).strip()
                if text:
                    options[opt_char] = text
    
    # Tìm đáp án đúng - dòng có ANSWER:
    for line in lines:
        line_upper = line.upper()
        if 'ANSWER' in line_upper:
            for opt in ['A', 'B', 'C', 'D']:
                if opt in line:
                    answer = opt
                    break
        elif '[X]' in line_upper or '[x]' in line:
            for opt in ['A', 'B', 'C', 'D']:
                if f'{opt}' in line or f'{opt})' in line:
                    answer = opt
                    break
    
    # Nếu không tìm được answer, lấy option đầu tiên
    if not answer:
        answer = list(options.keys())[0] if options else 'A'
    
    # Nếu thiếu 4 options, tạo fallback
    if len(options) < 4:
        fallback = [
            "Không đủ thông tin để trả lời",
            "Cần thêm dữ liệu",
            "Không thể xác định",
            "Đáp án khác",
        ]
        
        for opt in ['A', 'B', 'C', 'D']:
            if opt not in options:
                idx = ord(opt) - ord('A')
                options[opt] = fallback[idx] if idx < len(fallback) else f"Tùy chọn {opt}"
    
    return {
        'question': question,
        'options': options,
        'answer': answer
    }

def generate_questions(topic, model_name, question_type, eval_threshold=0.4):
    """Sinh câu hỏi từ topic và đánh giá"""
    try:
        results = collection.query(query_texts=[topic], n_results=1)
        if not results['documents'] or not results['documents'][0]:
            print(f"❌ Không tìm thấy dữ liệu cho topic: {topic}")
            return None
        
        context = results['documents'][0][0]
        
        # Prompt sinh câu hỏi
        if question_type == "Code C":
            prompt = f"""Bạn là giáo viên lập trình đang tạo câu hỏi trắc nghiệm về code C.
Dưới đây là ngữ cảnh từ giáo trình:
{context[:300]}

Tạo 1 câu hỏi trắc nghiệm theo format này CHÍNH XÁC:

Câu hỏi: [VIẾT CÂU HỎI CỤ THỂ VỀ CODE - không viết "Câu hỏi?"]
A) [ĐÁP ÁN A]
B) [ĐÁP ÁN B]
C) [ĐÁP ÁN C]
D) [ĐÁP ÁN D]
ANSWER: A"""
        elif question_type == "Lỗi sai Code":
            prompt = f"""Bạn là giáo viên lập trình đang tạo câu hỏi về lỗi trong code C.
Ngữ cảnh: {context[:300]}

Tạo 1 câu hỏi theo format CHÍNH XÁC:

Câu hỏi: [VIẾT CÂU HỎI CỤ THỀ VỀ LỖI CODE]
A) [ĐÁP ÁN A]
B) [ĐÁP ÁN B]
C) [ĐÁP ÁN C]
D) [ĐÁP ÁN D]
ANSWER: B"""
        elif question_type == "Logic":
            prompt = f"""Bạn là giáo viên đang tạo câu hỏi về logic lập trình.
Ngữ cảnh: {context[:300]}

Tạo 1 câu hỏi theo format CHÍNH XÁC:

Câu hỏi: [VIẾT CÂU HỎI CỤ THỂ VỀ LOGIC/THUẬT TOÁN]
A) [ĐÁP ÁN A]
B) [ĐÁP ÁN B]
C) [ĐÁP ÁN C]
D) [ĐÁP ÁN D]
ANSWER: C"""
        else:  # Lý thuyết
            prompt = f"""Bạn là giáo viên lập trình tạo câu hỏi lý thuyết.
Ngữ cảnh: {context[:300]}

Tạo 1 câu hỏi theo format CHÍNH XÁC:

Câu hỏi: [VIẾT CÂU HỎI CỤ THỀ VỀ KHÁI NIỆM - không viết "Câu hỏi?"]
A) [ĐÁP ÁN A - ĐÚNG]
B) [ĐÁP ÁN B - SAI]
C) [ĐÁP ÁN C - SAI]
D) [ĐÁP ÁN D - SAI]
ANSWER: A"""
        
        # Sinh câu hỏi
        response = ollama.generate(model=model_name, prompt=prompt, stream=False)
        generated_text = response['response']
        
        # Đánh giá
        faithfulness = evaluate_faithfulness(context, generated_text)
        time.sleep(0.5)
        relevancy = evaluate_relevancy(topic, generated_text)
        time.sleep(0.5)
        quality = evaluate_quality(generated_text, question_type)
        
        avg_score = (faithfulness + relevancy + quality) / 3
        
        if avg_score < eval_threshold:
            print(f"⚠️  Câu hỏi không đạt chuẩn (score: {avg_score:.2f} < {eval_threshold})")
            return None
        
        # Parse format Aiken
        parsed = extract_aiken_format(generated_text)
        if not parsed:
            print(f"❌ Không thể parse format Aiken")
            return None
        
        return {
            'topic': topic,
            'type': question_type,
            'model': model_name,
            'question': parsed['question'],
            'options': parsed['options'],
            'answer': parsed['answer'],
            'scores': {
                'faithfulness': faithfulness,
                'relevancy': relevancy,
                'quality': quality,
                'average': avg_score
            },
            'raw_response': generated_text
        }
        
    except Exception as e:
        print(f"❌ Lỗi: {str(e)}")
        return None

def create_moodle_xml(questions):
    """
    Tạo file XML theo format Moodle
    Format: https://docs.moodle.org/402/en/Aiken_format
    """
    quiz = ET.Element('quiz')
    
    for idx, q in enumerate(questions, 1):
        question = ET.SubElement(quiz, 'question', type='multichoice')
        question.set('format', 'aiken')
        
        # Name
        name = ET.SubElement(question, 'name')
        name_text = ET.SubElement(name, 'text')
        name_text.text = f"{q['type']} - Q{idx}"
        
        # Question text
        questiontext = ET.SubElement(question, 'questiontext', format='html')
        text = ET.SubElement(questiontext, 'text')
        text.text = q['question']
        
        # General (metadata)
        general = ET.SubElement(question, 'general')
        
        # Answer options
        answer = ET.SubElement(question, 'answer', fraction='100' if q['answer'] == 'A' else '0')
        answer_text = ET.SubElement(answer, 'text')
        answer_text.text = q['options'].get('A', '')
        
        for opt in ['B', 'C', 'D']:
            answer = ET.SubElement(question, 'answer', fraction='100' if q['answer'] == opt else '0')
            answer_text = ET.SubElement(answer, 'text')
            answer_text.text = q['options'].get(opt, '')
        
        # Shuffle
        shuffle = ET.SubElement(question, 'shuffle')
        shuffle.text = '1'
        
        # Single answer
        single = ET.SubElement(question, 'single')
        single.text = 'true'
    
    # Pretty print with proper XML declaration
    xml_str = ET.tostring(quiz, encoding='unicode')
    dom = minidom.parseString(xml_str)
    xml_lines = dom.toprettyxml(indent="  ").split('\n')
    
    # Thêm XML declaration
    result_lines = ['<?xml version="1.0" encoding="UTF-8"?>']
    
    # Bỏ 2 dòng đầu của dom output (declaration + blank), thêm phần còn lại
    for line in xml_lines[2:]:
        if line.strip():  # Bỏ dòng trống
            result_lines.append(line)
    
    return '\n'.join(result_lines)

def export_to_file(questions, output_file="questions_export.xml"):
    """Export câu hỏi sang file XML"""
    if not questions:
        print("❌ Không có câu hỏi để export")
        return False
    
    xml_content = create_moodle_xml(questions)
    
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(xml_content)
    
    print(f"✅ Đã export {len(questions)} câu hỏi sang {output_file}")
    return True

if __name__ == "__main__":
    print("🚀 BẮT ĐẦU SINH V À EXPORT CÂU HỎI\n")
    
    configs = [
        ("Giải thuật là gì", "qwen2.5:7b", "Lý thuyết"),
        ("Hoán đổi hai biến", "llama3.1:8b", "Logic"),
        ("Cấu trúc vòng lặp for", "deepseek-coder-v2", "Code C"),
        ("Lỗi trong code C", "deepseek-coder-v2", "Lỗi sai Code")
    ]
    
    all_questions = []
    for topic, model, qtype in configs:
        print(f"\n📝 Sinh câu hỏi: {qtype} | Model: {model}")
        q = generate_questions(topic, model, qtype, eval_threshold=0.35)
        if q:
            all_questions.append(q)
            print(f"✅ Câu hỏi: {q['question'][:50]}...")
            print(f"   Score: {q['scores']['average']:.2f}")
        time.sleep(2)
    
    # Export
    if all_questions:
        export_to_file(all_questions, "questions_export.xml")
        print(f"\n📊 Tổng: {len(all_questions)}/{len(configs)} câu hỏi")
