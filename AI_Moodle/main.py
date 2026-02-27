#!/usr/bin/env python3
"""
PIPELINE CHÍNH - AI Moodle Question Generator
Quy trình: Data Ingestion → Question Generation → Export XML → Optional: Upload to Moodle
"""

import os
import sys
import time
from pathlib import Path

def print_header(title):
    """In header"""
    print(f"\n{'='*70}")
    print(f"🔷 {title}")
    print(f"{'='*70}\n")

def run_step_1_ingestion():
    """Step 1: Nạp dữ liệu vào ChromaDB"""
    print_header("BƯỚC 1: NẠP DỮ LIỆU VÀO CHROMADB")
    
    try:
        from ingest_data import ingest
        ingest()
        print("✅ Hoàn thành bước 1\n")
        return True
    except Exception as e:
        print(f"❌ Lỗi ở bước 1: {str(e)}\n")
        return False

def run_step_2_evaluation():
    """Step 2: Sinh câu hỏi và đánh giá"""
    print_header("BƯỚC 2: SINH CÂU HỎI VÀ ĐÁNH GIÁ")
    
    try:
        import chromadb
        import ollama
        import time
        
        client = chromadb.PersistentClient(path="./db_moodle")
        collection = client.get_collection(name="giao_trinh_c")
        
        print("📊 Thử nghiệm 4 dạng câu hỏi...\n")
        
        configs = [
            ("Giải thuật là gì", "qwen2.5:7b", "Lý thuyết"),
            ("Hoán đổi hai biến", "llama3.1:8b", "Logic"),
            ("Cấu trúc vòng lặp for", "deepseek-coder-v2", "Code C"),
            ("Lỗi trong code C", "deepseek-coder-v2", "Lỗi sai Code")
        ]
        
        results = []
        for topic, model, qtype in configs:
            print(f"  ⏳ {qtype} ({model})...", end=" ", flush=True)
            
            # Lấy context
            query_results = collection.query(query_texts=[topic], n_results=1)
            context = query_results['documents'][0][0]
            
            # Sinh câu hỏi
            prompt = f"Ngữ cảnh: {context}\nTạo 1 câu trắc nghiệm {qtype} format Aiken."
            response = ollama.generate(model=model, prompt=prompt, stream=False)
            generated = response['response']
            
            results.append({
                'topic': topic,
                'type': qtype,
                'model': model,
                'text': generated
            })
            
            print("✓")
            time.sleep(1)
        
        print(f"\n✅ Hoàn thành bước 2 ({len(results)} câu hỏi)\n")
        return True
        
    except Exception as e:
        print(f"❌ Lỗi ở bước 2: {str(e)}\n")
        return False

def run_step_3_export():
    """Step 3: Export sang XML Moodle"""
    print_header("BƯỚC 3: EXPORT SANG XML CHO MOODLE")
    
    try:
        from export_to_moodle import generate_questions, export_to_file
        
        print("📝 Sinh và export câu hỏi...\n")
        
        configs = [
            ("Giải thuật là gì", "qwen2.5:7b", "Lý thuyết"),
            ("Hoán đổi hai biến", "llama3.1:8b", "Logic"),
            ("Cấu trúc vòng lặp for", "deepseek-coder-v2", "Code C"),
            ("Lỗi trong code C", "deepseek-coder-v2", "Lỗi sai Code")
        ]
        
        questions = []
        for topic, model, qtype in configs:
            print(f"  ⏳ {qtype} ({model})...", end=" ", flush=True)
            q = generate_questions(topic, model, qtype, eval_threshold=0.35)
            if q:
                questions.append(q)
                print("✓")
            else:
                print("✗ (không đạt chuẩn)")
            time.sleep(1)
        
        if questions:
            export_to_file(questions, "questions_export.xml")
            print(f"\n✅ Hoàn thành bước 3 ({len(questions)} câu hỏi được export)\n")
            return True
        else:
            print("\n⚠️  Không có câu hỏi nào được export\n")
            return False
        
    except Exception as e:
        print(f"❌ Lỗi ở bước 3: {str(e)}\n")
        import traceback
        traceback.print_exc()
        return False

def run_step_4_moodle_optional():
    """Step 4 (Optional): Tích hợp với Moodle"""
    print_header("BƯỚC 4 (TÙY CHỌN): TÍCH HỢP VỚI MOODLE")
    
    print("""
Để upload câu hỏi lên Moodle, bạn có 2 lựa chọn:

1️⃣  CÁCH ĐỀ XUẤT (Dễ nhất):
   ✓ Đăng nhập Moodle
   ✓ Course Settings → Question bank → Import
   ✓ Chọn file: questions_export.xml
   ✓ Import format: Aiken
   ✓ Click "Upload and import"

2️⃣  CÓ THÊM YÊU CẦU (API):
   ✓ Cấu hình Moodle Web Services
   ✓ Chạy: moodle_integration.py
   ✓ Nhập URL, Token, Course ID
    
Để tạo Web Service Token, xem hướng dẫn trong file:
    moodle_integration.py

✅ File questions_export.xml đã sẵn sàng!
    """)
    
    return True

def main():
    """Main pipeline"""
    print("""
╔════════════════════════════════════════════════════════════╗
║    AI MOODLE QUESTION GENERATOR - MAIN PIPELINE        ║
╚════════════════════════════════════════════════════════════╝
    """)
    
    print("⏱Khởi động pipeline...\n")
    
    steps = [
        ("1️⃣  Nạp dữ liệu", run_step_1_ingestion),
        ("2️⃣  Sinh & Đánh giá", run_step_2_evaluation),
        ("3️⃣  Export XML", run_step_3_export),
        ("4️⃣  Moodle (Tùy)", run_step_4_moodle_optional),
    ]
    
    completed = []
    failed = []
    
    for step_name, step_func in steps:
        print(f"\n{step_name}")
        try:
            if step_func():
                completed.append(step_name)
                time.sleep(1)
            else:
                failed.append(step_name)
                break  # Dừng nếu bước nào thất bại
        except KeyboardInterrupt:
            print("\n⚠️  Pipeline bị dừng bởi người dùng")
            break
        except Exception as e:
            print(f"❌ Lỗi: {str(e)}")
            failed.append(step_name)
            break
    
    # Summary
    print("\n" + "="*70)
    print("📊 TÓM TẮT KẾT QUẢ")
    print("="*70)
    
    for step in completed:
        print(f"  ✅ {step}")
    
    if failed:
        for step in failed:
            print(f"  ❌ {step}")
    
    if len(completed) == len(steps):
        print(f"\nPIPELINE HOÀN THÀNH TOÀN BỘ!")
        print(f"\nFile output:")
        print(f"   - questions_export.xml (sẵn sàng import vào Moodle)")
    elif len(completed) == len(steps) - 1:
        print(f"\nPIPELINE THÀNH CÔNG!")
        print(f"   Bước Moodle là tùy chọn (có thể bỏ qua)")
    else:
        print(f"\nPipeline dừng tại bước {len(completed) + 1}")
    
    print("\n" + "="*70)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n⚠️  Pipeline dừng")
        sys.exit(1)
    except Exception as e:
        print(f"\n\n❌ Lỗi không mong muốn: {str(e)}")
        import traceback
        traceback.print_exc()
        sys.exit(1)