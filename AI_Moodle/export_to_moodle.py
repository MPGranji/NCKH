#!/usr/bin/env python3
"""
EXPORT TO MOODLE
Sinh câu hỏi và export sang XML Aiken format
"""

import chromadb
import ollama
import time
from xml.etree.ElementTree import Element, SubElement, tostring
from xml.dom import minidom

# Kết nối ChromaDB
client = chromadb.PersistentClient(path="./db_moodle")
collection = client.get_collection(name="giao_trinh_c")

def evaluate_score(context_or_topic, generated_text, eval_type, eval_model="qwen2.5:7b"):
    """Đánh giá 1 tiêu chí"""
    if eval_type == "faithfulness":
        prompt = f"""Đánh giá (0.0-1.0): câu hỏi có dựa trên context không?
Context: {context_or_topic[:200]}...
Câu: {generated_text[:200]}...
Chỉ trả lời số từ 0 đến 1."""
    elif eval_type == "relevancy":
        prompt = f"""Đánh giá (0.0-1.0): câu hỏi có liên quan '{context_or_topic}' không?
Câu: {generated_text[:200]}...
Chỉ trả lời số từ 0 đến 1."""
    else:  # quality
        prompt = f"""Đánh giá (0.0-1.0): chất lượng, rõ ràng, đúng format?
Câu: {generated_text[:200]}...
Chỉ trả lời số từ 0 đến 1."""
    
    try:
        resp = ollama.generate(model=eval_model, prompt=prompt, stream=False)
        text = resp['response'].strip()
        # Extract number
        import re
        match = re.search(r'0\.\d+|1\.0|\d', text)
        if match:
            score = float(match.group())
            return min(1.0, max(0.0, score / 10 if score > 1 else score))
        return 0.5
    except:
        return 0.5

def generate_question(topic, model, question_type, threshold=0.35):
    """Sinh 1 câu hỏi và kiểm tra điểm"""
    try:
        # Lấy context
        results = collection.query(query_texts=[topic], n_results=1)
        if not results['documents'] or not results['documents'][0]:
            return None
            
        context = results['documents'][0][0]
        
        # Sinh câu hỏi
        if question_type == "code":
            prompt = f"Dựa vào ngữ cảnh: {context}\nTạo 1 câu trắc nghiệm CODE C dưới dạng:\nA) ...\nB) ...\nC) ...\nD) ...\nANSWER: [A/B/C/D]"
        else:
            prompt = f"Dựa vào ngữ cảnh: {context}\nTạo 1 câu trắc nghiệm LÝ THUYẾT dưới dạng:\nA) ...\nB) ...\nC) ...\nD) ...\nANSWER: [A/B/C/D]"
        
        response = ollama.generate(model=model, prompt=prompt, stream=False)
        question = response['response']
        
        # Đánh giá 3 metrics
        faith = evaluate_score(context, question, "faithfulness")
        time.sleep(0.1)
        relev = evaluate_score(topic, question, "relevancy")
        time.sleep(0.1)
        qual = evaluate_score("", question, "quality")
        
        avg = (faith + relev + qual) / 3
        
        # Chỉ return nếu pass threshold
        if avg >= threshold:
            return {
                'question': question,
                'topic': topic,
                'type': question_type,
                'model': model,
                'faith': faith,
                'relev': relev,
                'qual': qual,
                'avg': avg
            }
        else:
            return None
    except Exception as e:
        print(f"[ERROR] Error ({model}): {str(e)}")
        return None

def export_to_aiken(questions, filename="questions_export.xml"):
    """Xuất câu hỏi sang format Aiken (XML)"""
    
    # Tạo root element
    root = Element('quiz')
    
    for i, q in enumerate(questions):
        question_elem = SubElement(root, 'question')
        question_elem.set('type', 'multichoice')
        
        # Name
        name = SubElement(question_elem, 'name')
        name_text = SubElement(name, 'text')
        name_text.text = f"Câu hỏi {i+1}: {q['topic']}"
        
        # Question text
        quest_text_elem = SubElement(question_elem, 'questiontext')
        quest_text_elem.set('format', 'html')
        quest_text = SubElement(quest_text_elem, 'text')
        quest_text.text = q['question']
        
        # General feedback
        general_feedback = SubElement(question_elem, 'generalfeedback')
        general_feedback_text = SubElement(general_feedback, 'text')
        general_feedback_text.text = f"Model: {q['model']}, Điểm: {q['avg']:.2f}"
        
        # Correct answer feedback (parse từ question)
        default_mark = SubElement(question_elem, 'defaultmark')
        default_mark.text = "1.0"
        
        # Answer flag to parse ANSWER: [A/B/C/D]
        import re
        answer_match = re.search(r'ANSWER:\s*\[?([A-D])\]?', q['question'])
        correct_letter = answer_match.group(1) if answer_match else 'A'
        letter_to_num = {'A': 0, 'B': 1, 'C': 2, 'D': 3}
        correct_idx = letter_to_num.get(correct_letter, 0)
        
        # Options (A, B, C, D)
        options = re.findall(r'[A-D]\)\s*(.+?)(?=[A-D]\)|$)', q['question'], re.DOTALL)
        if not options:
            options = ['Option A', 'Option B', 'Option C', 'Option D']
        
        for j in range(4):
            answer = SubElement(question_elem, 'answer')
            answer.set('fraction', '100' if j == correct_idx else '0')
            answer_text = SubElement(answer, 'text')
            answer_text.text = options[j] if j < len(options) else f"Option {chr(65+j)}"
    
    # Pretty print
    xml_str = minidom.parseString(tostring(root)).toprettyxml(indent="  ")
    
    # Write to file
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(xml_str)
    
    print(f"Đã xuất {len(questions)} câu hỏi sang {filename}")

def batch_generate(topics, models, question_types, num_per_combo=1, threshold=0.35):
    """Sinh batch câu hỏi"""
    questions = []
    total = len(topics) * len(models) * len(question_types) * num_per_combo
    current = 0
    
    print(f"\nSinh {total} câu hỏi...\n")
    
    for topic in topics:
        for model in models:
            for qtype in question_types:
                for attempt in range(num_per_combo):
                    current += 1
                    print(f"[{current}/{total}] {topic} - {model} - {qtype}: ", end="", flush=True)
                    
                    result = generate_question(topic, model, qtype, threshold=threshold)
                    if result:
                        questions.append(result)
                        print("[OK]")
                    else:
                        print("[SKIP - Low score]")
                    
                    time.sleep(0.5)
    
    print(f"\nTổng sinh được: {len(questions)} câu hỏi")
    return questions

def main():
    print("""
════════════════════════════════════════════════════════════
 EXPORT TO MOODLE - SINH & XUẤT CÂU HỎI
════════════════════════════════════════════════════════════
    """)
    
    # Cấu hình
    topics = [
        "Giải thuật là gì",
        "Vòng lặp for",
        "Hàm và hàm đệ quy"
    ]
    
    models = [
        "deepseek-coder-v2",
        "qwen2.5:7b",
        "llama3.1:8b"
    ]
    
    qtypes = ["theory", "code"]
    
    # Sinh câu hỏi
    questions = batch_generate(
        topics=topics,
        models=models,
        question_types=qtypes,
        num_per_combo=1,
        threshold=0.35
    )
    
    # Xuất XML
    if questions:
        export_to_aiken(questions)
    else:
        print("\nKhông có câu hỏi nào thỏa mãn điều kiện!")

if __name__ == "__main__":
    main()

