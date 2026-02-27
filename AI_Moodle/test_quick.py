#!/usr/bin/env python3
"""
⚡ QUICK TEST - So sánh và test nhanh câu hỏi
Chế độ: So sánh 2 model / So sánh 2 loại câu hỏi
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

def generate_question(topic, model, question_type):
    """Sinh 1 câu hỏi"""
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
            'avg': avg
        }
    except Exception as e:
        print(f"❌ Error: {str(e)}")
        return None

def compare_models():
    """So sánh 2 model cùng topic"""
    print("""
╔════════════════════════════════════════════════════════════╗
║           🔄 SO SÁNH 2 MODEL TRÊN CÙNG TOPIC              ║
╚════════════════════════════════════════════════════════════╝
    """)
    
    topic = "Giải thuật là gì"
    model1 = "qwen2.5:7b"
    model2 = "llama3.1:8b"
    qtype = "Lý thuyết"
    
    print(f"\n📌 Topic: {topic}")
    print(f"📌 Loại câu: {qtype}")
    print(f"\n🟦 Model 1: {model1}")
    print(f"🟩 Model 2: {model2}\n")
    
    result1 = generate_question(topic, model1, qtype)
    print("⏳ Generating model 2...")
    time.sleep(1)
    result2 = generate_question(topic, model2, qtype)
    
    # So sánh
    print("\n" + "="*70)
    print("📊 KẾT QUẢ SO SÁNH")
    print("="*70 + "\n")
    
    print(f"🟦 {model1}")
    print(f"   Câu: {result1['question'][:80]}...")
    print(f"   Faithfulness: {result1['faith']:.2f}")
    print(f"   Relevancy:    {result1['relev']:.2f}")
    print(f"   Quality:      {result1['qual']:.2f}")
    print(f"   ⭐ TRUNG BÌNH: {result1['avg']:.2f} {'✅ Pass' if result1['avg'] >= 0.35 else '⚠️  Low'}")
    
    print()
    
    print(f"🟩 {model2}")
    print(f"   Câu: {result2['question'][:80]}...")
    print(f"   Faithfulness: {result2['faith']:.2f}")
    print(f"   Relevancy:    {result2['relev']:.2f}")
    print(f"   Quality:      {result2['qual']:.2f}")
    print(f"   ⭐ TRUNG BÌNH: {result2['avg']:.2f} {'✅ Pass' if result2['avg'] >= 0.35 else '⚠️  Low'}")
    
    print("\n" + "="*70)
    print("🏆 KÊTT LUẬN")
    print("="*70)
    
    if result1['avg'] > result2['avg']:
        diff = result1['avg'] - result2['avg']
        print(f"   🟦 {model1} tốt hơn {diff:.2f} điểm")
    elif result2['avg'] > result1['avg']:
        diff = result2['avg'] - result1['avg']
        print(f"   🟩 {model2} tốt hơn {diff:.2f} điểm")
    else:
        print(f"   ⚖️  Cả hai bằng nhau!")

def compare_question_types():
    """So sánh 2 loại câu hỏi"""
    print("""
╔════════════════════════════════════════════════════════════╗
║        🔄 SO SÁNH 2 LOẠI CÂU HỎI TRÊN CÙNG MODEL         ║
╚════════════════════════════════════════════════════════════╝
    """)
    
    topic = "Cấu trúc vòng lặp for"
    model = "deepseek-coder-v2"
    qtype1 = "Lý thuyết"
    qtype2 = "Code thực hành"
    
    print(f"\n📌 Topic: {topic}")
    print(f"📌 Model: {model}")
    print(f"\n🟦 Loại 1: {qtype1}")
    print(f"🟩 Loại 2: {qtype2}\n")
    
    result1 = generate_question(topic, model, qtype1)
    print("⏳ Generating loại 2...")
    time.sleep(1)
    result2 = generate_question(topic, model, qtype2)
    
    # So sánh
    print("\n" + "="*70)
    print("📊 KẾT QUẢ SO SÁNH")
    print("="*70 + "\n")
    
    print(f"🟦 {qtype1}")
    print(f"   Câu: {result1['question'][:80]}...")
    print(f"   Faithfulness: {result1['faith']:.2f}")
    print(f"   Relevancy:    {result1['relev']:.2f}")
    print(f"   Quality:      {result1['qual']:.2f}")
    print(f"   ⭐ TRUNG BÌNH: {result1['avg']:.2f} {'✅ Pass' if result1['avg'] >= 0.35 else '⚠️  Low'}")
    
    print()
    
    print(f"🟩 {qtype2}")
    print(f"   Câu: {result2['question'][:80]}...")
    print(f"   Faithfulness: {result2['faith']:.2f}")
    print(f"   Relevancy:    {result2['relev']:.2f}")
    print(f"   Quality:      {result2['qual']:.2f}")
    print(f"   ⭐ TRUNG BÌNH: {result2['avg']:.2f} {'✅ Pass' if result2['avg'] >= 0.35 else '⚠️  Low'}")
    
    print("\n" + "="*70)
    print("🏆 KẾT LUẬN")
    print("="*70)
    
    if result1['avg'] > result2['avg']:
        diff = result1['avg'] - result2['avg']
        print(f"   🟦 {qtype1} tốt hơn {diff:.2f} điểm")
    elif result2['avg'] > result1['avg']:
        diff = result2['avg'] - result1['avg']
        print(f"   🟩 {qtype2} tốt hơn {diff:.2f} điểm")
    else:
        print(f"   ⚖️  Cả hai bằng nhau!")

def main():
    print("""
╔════════════════════════════════════════════════════════════╗
║    ⚡ QUICK TEST - SO SÁNH NHANH                          ║
╚════════════════════════════════════════════════════════════╝

Lựa chọn:
  1️⃣  So sánh 2 MODEL (cùng topic)
  2️⃣  So sánh 2 LOẠI CÂU HỎI (cùng model)
  0️⃣  Thoát
    """)
    
    choice = input("Chọn (0-2): ").strip()
    
    if choice == "1":
        compare_models()
    elif choice == "2":
        compare_question_types()
    elif choice == "0":
        print("Thoát!")
    else:
        print("❌ Lựa chọn không hợp lệ!")

if __name__ == "__main__":
    main()
