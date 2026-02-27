#!/usr/bin/env python3
"""
⚡ QUICK TEST - Test nhanh chức năng sinh câu hỏi & đánh giá
Dùng khi muốn test mà không cần chạy full pipeline
"""

import chromadb
import ollama
import time

# Kết nối ChromaDB
client = chromadb.PersistentClient(path="./db_moodle")
collection = client.get_collection(name="giao_trinh_c")

def evaluate_score(context_or_topic, generated_text, eval_type, eval_model="qwen2.5:7b"):
    """Đánh giá 1 tiêu chí"""
    if eval_type == "faithfulness":
        prompt = f"""Đánh giá (0.0-1.0): câu hỏi có dựa trên context không?
Context: {context_or_topic[:200]}...
Câu: {generated_text[:200]}...
Chỉ trả lời số."""
    elif eval_type == "relevancy":
        prompt = f"""Đánh giá (0.0-1.0): câu hỏi có liên quan '{context_or_topic}' không?
Câu: {generated_text[:200]}...
Chỉ trả lời số."""
    else:  # quality
        prompt = f"""Đánh giá (0.0-1.0): chất lượng, rõ ràng, đúng format?
Câu: {generated_text[:200]}...
Chỉ trả lời số."""
    
    try:
        resp = ollama.generate(model=eval_model, prompt=prompt, stream=False)
        text = resp['response'].strip()
        score = float(''.join(c for c in text if c.isdigit() or c == '.')[:3])
        return min(1.0, max(0.0, score / 10 if score > 1 else score))
    except:
        return 0.5

def test_question(topic, model, question_type):
    """Test sinh & đánh giá 1 câu hỏi"""
    print(f"\n🧪 {question_type.ljust(15)} | {model}")
    print("-" * 50)
    
    try:
        # Lấy context
        results = collection.query(query_texts=[topic], n_results=1)
        context = results['documents'][0][0]
        
        # Sinh câu hỏi
        prompt = f"Ngữ cảnh: {context}\nTạo 1 câu trắc nghiệm {question_type} format Aiken A) B) C) D) ANSWER:"
        response = ollama.generate(model=model, prompt=prompt, stream=False)
        question = response['response']
        
        # Đánh giá 3 metrics
        faith = evaluate_score(context, question, "faithfulness")
        time.sleep(0.3)
        relev = evaluate_score(topic, question, "relevancy")
        time.sleep(0.3)
        qual = evaluate_score("", question, "quality")
        
        avg = (faith + relev + qual) / 3
        
        # In kết quả
        print(f"Câu: {question[:60]}...")
        print(f"Scores: Faith={faith:.2f} | Relev={relev:.2f} | Quality={qual:.2f} | Avg={avg:.2f}")
        print(f"Status: {'✅ Pass' if avg >= 0.35 else '⚠️  Low'}")
        
        return avg
        
    except Exception as e:
        print(f"❌ Error: {str(e)}")
        return 0

def main():
    print("""
╔════════════════════════════════════════════════╗
║    ⚡ QUICK TEST - SINH CÂU HỎI & ĐÁNH GIÁ   ║
╚════════════════════════════════════════════════╝
    """)
    
    tests = [
        ("Giải thuật là gì", "qwen2.5:7b", "Lý thuyết"),
        ("Hoán đổi hai biến", "llama3.1:8b", "Logic"),
        ("Cấu trúc vòng lặp for", "deepseek-coder-v2", "Code C"),
    ]
    
    scores = []
    for topic, model, qtype in tests:
        score = test_question(topic, model, qtype)
        scores.append((qtype, score))
        time.sleep(1)
    
    # Summary
    print(f"\n{'='*50}")
    print("📊 TÓM TẮT")
    print(f"{'='*50}")
    for qtype, score in scores:
        status = "✅" if score >= 0.35 else "⚠️ "
        print(f"  {status} {qtype.ljust(15)}: {score:.2f}")

if __name__ == "__main__":
    main()
