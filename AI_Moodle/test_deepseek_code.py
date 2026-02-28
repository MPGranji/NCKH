#!/usr/bin/env python3
"""
TEST DEEPSEEK CODE - So sánh 3 model trên câu hỏi CODE
So sánh: deepseek-coder-v2 vs qwen2.5:7b vs llama3.1:8b
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

def generate_code_question(topic, model):
    """Sinh 1 câu hỏi code"""
    try:
        # Lấy context
        results = collection.query(query_texts=[topic], n_results=1)
        context = results['documents'][0][0]
        
        # Sinh câu hỏi code
        prompt = f"Ngữ cảnh: {context}\nTạo 1 câu trắc nghiệm CODE C format Aiken A) B) C) D) ANSWER:"
        response = ollama.generate(model=model, prompt=prompt, stream=False)
        question = response['response']
        
        # Đánh giá 3 metrics
        faith = evaluate_score(context, question, "faithfulness")
        time.sleep(0.2)
        relev = evaluate_score(topic, question, "relevancy")
        time.sleep(0.2)
        qual = evaluate_score("", question, "quality")
        
        avg = (faith + relev + qual) / 3
        
        return {
            'question': question,
            'faith': faith,
            'relev': relev,
            'qual': qual,
            'avg': avg,
            'model': model
        }
    except Exception as e:
        print(f"[ERROR] Error ({model}): {str(e)}")
        return None

def main():
    print("""
════════════════════════════════════════════════════════════
 TEST DEEPSEEK CODE - COMPARE 3 MODELS
════════════════════════════════════════════════════════════
    """)
    
    topic = "Cấu trúc vòng lặp for"
    qtype = "Code C"
    
    models = [
        "deepseek-coder-v2",
        "qwen2.5:7b",
        "llama3.1:8b"
    ]
    
    print(f"\nChủ đề: {topic}")
    print(f"Loại câu: {qtype}")
    print(f"\nSinh câu hỏi từ 3 model...\n")
    
    results = []
    
    for i, model in enumerate(models):
        print(f"   [{i+1}] {model}...", end=" ", flush=True)
        result = generate_code_question(topic, model)
        if result:
            results.append(result)
            print("[OK]")
        else:
            print("[FAILED]")
        time.sleep(1)
    
    # So sánh
    print("\n" + "="*70)
    print("KẾT QUẢ SO SÁNH CHI TIẾT")
    print("="*70 + "\n")
    
    for i, result in enumerate(results):
        print(f"[Model {i+1}] {result['model'].ljust(20)}")
        print(f"   Câu: {result['question'][:90]}...")
        print(f"   Faithfulness: {result['faith']:.2f}")
        print(f"   Relevancy:    {result['relev']:.2f}")
        print(f"   Quality:      {result['qual']:.2f}")
        status = "PASS" if result['avg'] >= 0.35 else "LOW"
        print(f"   AVG: {result['avg']:.2f} [{status}]")
        print()
    
    # Xếp hạng
    print("="*70)
    print("BẢNG XẾP HẠNG")
    print("="*70 + "\n")
    
    sorted_results = sorted(results, key=lambda x: x['avg'], reverse=True)
    
    for i, result in enumerate(sorted_results):
        print(f"   [{i+1}] {result['model'].ljust(25)} - {result['avg']:.2f}")
    
    print("\n" + "="*70)
    print("NHẬN XÉT")
    print("="*70)
    
    best = sorted_results[0]
    worst = sorted_results[-1]
    diff = best['avg'] - worst['avg']
    
    print(f"""
   [BEST] Model tốt nhất: {best['model']}
      Điểm: {best['avg']:.2f}
   
   [WORST] Model yếu nhất: {worst['model']}
      Điểm: {worst['avg']:.2f}
   
   [DIFF] Chênh lệch: {diff:.2f} điểm
    """)

if __name__ == "__main__":
    main()

