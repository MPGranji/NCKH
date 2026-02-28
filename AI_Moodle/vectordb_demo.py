#!/usr/bin/env python3
"""
========================================================
  VECTORDB SEMANTIC SEARCH - DEMO CHI TIẾT
========================================================

Giải thích cách VectorDB tìm kiếm:
  1. Text input → Chuyển thành Vector (embedding)
  2. Vector được so sánh với tất cả vectors trong DB
  3. Trả về documents có vector gần nhất (cosine similarity)
  4. Không dựa vào keyword, mà dựa vào ý nghĩa

Ví dụ:
  Query: "vòng lặp"
  Results sẽ bao gồm:
    - Documents về "for loop"
    - Documents về "while loop"
    - Documents về "iteration"
    - Documents về "looping constructs"
  Tất cả vì chúng có ý nghĩa giống nhau!
"""

import chromadb
import json


def demo_semantic_search():
    """
    DEMO: Semantic Search trong VectorDB
    """
    
    print("""
╔════════════════════════════════════════════════════════════╗
║         CHROMADB SEMANTIC SEARCH - DEMO CHI TIẾT         ║
╚════════════════════════════════════════════════════════════╝
    """)
    
    # ========================================================
    # BƯỚC 1: CONNECT TỚI CHROMADB
    # ========================================================
    
    print("BƯỚC 1: Kết nối ChromaDB database...")
    client = chromadb.PersistentClient(path="./db_moodle")
    collection = client.get_collection(name="giao_trinh_c")
    
    total_docs = collection.count()
    print(f"✓ Kết nối thành công!")
    print(f"  - Database location: ./db_moodle/chroma.sqlite3")
    print(f"  - Collection: giao_trinh_c")
    print(f"  - Total documents: {total_docs}\n")
    
    # ========================================================
    # BƯỚC 2: XEM CẤU TRÚC DỮ LIỆU
    # ========================================================
    
    print("BƯỚC 2: Xem cấu trúc dữ liệu...")
    print("  Data structure:")
    print("  ├─ documents: [text content]")
    print("  ├─ embeddings: [768 chiều vectors - tự động tạo]")
    print("  ├─ metadatas: {chunk: X, page: Y}")
    print("  └─ ids: unique document IDs\n")
    
    # Lấy sample
    all_docs = collection.get(limit=1)
    if all_docs['documents']:
        sample = all_docs['documents'][0]
        meta = all_docs['metadatas'][0]
        print(f"Sample document:")
        print(f"  Content (first 150 chars): {sample[:150]}...")
        print(f"  Metadata: chunk={meta['chunk']}, page={meta['page']}\n")
    
    # ========================================================
    # BƯỚC 3: SEMANTIC QUERIES - SO SÁNH CÁC CÂU HỎI KHÁC NHAU
    # ========================================================
    
    queries = [
        "vòng lặp",
        "giải thuật",
        "hàm đệ quy",
        "cấu trúc dữ liệu"
    ]
    
    print("BƯỚC 3: Semantic Search Examples")
    print("=" * 60)
    
    for query in queries:
        print(f"\n📌 Query: '{query}'")
        print(f"   Tìm kiếm semantic (theo ý nghĩa)...\n")
        
        # Query semantic
        results = collection.query(
            query_texts=[query],
            n_results=3  # Lấy 3 kết quả tốt nhất
        )
        
        # Display results
        for i, (doc_id, doc_text, meta, distance) in enumerate(zip(
            results['ids'][0],
            results['documents'][0],
            results['metadatas'][0],
            results['distances'][0]
        )):
            
            # Distance score explanation
            if distance < 0.3:
                match_level = "🟢 Rất giống"
            elif distance < 0.5:
                match_level = "🟡 Khá giống"
            else:
                match_level = "🔴 Ít giống"
            
            print(f"   [{i+1}] {match_level} (distance: {distance:.4f})")
            print(f"       Chunk: {meta['chunk']}, Page: {meta['page']}")
            print(f"       Text: {doc_text[:100]}...")
            print()
    
    # ========================================================
    # BƯỚC 4: GIẢI THÍCH CHI TIẾT
    # ========================================================
    
    print("=" * 60)
    print("\nBƯỚC 4: Giải thích chi tiết\n")
    
    print("⚙️  Cách Embeddings hoạt động:")
    print("   1. Text input → Chuyển thành vector 768 chiều")
    print("   2. Mỗi từ/ý nghĩa được biểu diễn dưới dạng số")
    print("   3. Từ cùng ý nghĩa có vectors rất gần nhau")
    print("   4. Cosine similarity = độ giống giữa 2 vectors\n")
    
    print("📊 Distance Score:")
    print("   - 0.0  = Perfect match (hoàn toàn giống)")
    print("   - 0.1  = Very similar (rất giống)")
    print("   - 0.3  = Similar (khá giống)")
    print("   - 0.5  = Somewhat similar (ít giống)")
    print("   - 1.0  = Completely different (hoàn toàn khác)\n")
    
    print("💡 Ứng dụng trong dự án:")
    print("   1. Khi cần sinh câu hỏi về 'vòng lặp'")
    print("   2. Query ChromaDB → Tìm kiếm semantic")
    print("   3. Trả về documents về for/while/iteration")
    print("   4. Sử dụng làm context cho LLM")
    print("   5. LLM sinh câu hỏi từ context này\n")


def demo_batch_search():
    """
    DEMO: Batch Search - Tìm kiếm nhiều queries cùng lúc
    """
    
    print("\n" + "=" * 60)
    print("BONUS: Batch Search (Tìm kiếm multiple queries)")
    print("=" * 60 + "\n")
    
    client = chromadb.PersistentClient(path="./db_moodle")
    collection = client.get_collection(name="giao_trinh_c")
    
    # Tìm kiếm nhiều queries cùng lúc (nhanh hơn)
    batch_queries = [
        "for loop",
        "function call",
        "array manipulation"
    ]
    
    print(f"Tìm kiếm {len(batch_queries)} queries cùng lúc...\n")
    
    results = collection.query(
        query_texts=batch_queries,
        n_results=2  # 2 kết quả per query
    )
    
    for query_idx, query in enumerate(batch_queries):
        print(f"📌 Query {query_idx + 1}: '{query}'")
        
        for result_idx in range(len(results['documents'][query_idx])):
            doc = results['documents'][query_idx][result_idx]
            dist = results['distances'][query_idx][result_idx]
            print(f"   - Distance: {dist:.4f}, Text: {doc[:80]}...")
        print()


def main():
    """Main demo runner"""
    
    demo_semantic_search()
    
    choice = input("Muốn xem Batch Search demo? (y/n): ").strip().lower()
    if choice == 'y':
        demo_batch_search()
    
    print("\n✓ Demo hoàn tất!")
    print("  Hiểu rõ hơn về VectorDB? Hãy chạy: python view_chroma.py")


if __name__ == "__main__":
    main()
