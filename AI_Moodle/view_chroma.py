#!/usr/bin/env python3
"""
========================================================
  VECTORDB VIEWER - XEM & TÌM KIẾM DỮ LIỆU CHROMADB
========================================================

ChromaDB Query có 2 cách:
  1. get(limit=N) - Lấy N documents đầu tiên
  2. query(query_texts=[text], n_results=N) - TÌM KIẾM SEMANTIC
  
Semantic Search = Tìm theo ý nghĩa, không phải keyword
Ví dụ: "vòng lặp" sẽ tìm bao gồm "for", "while", "loop"
       vì chúng có ý nghĩa giống nhau
"""

import chromadb
import json


def view_collection_info():
    """
    Xem thông tin collection và sample documents trong ChromaDB
    
    Cách hoạt động:
      1. Kết nối tới ChromaDB database
      2. List tất cả collections
      3. Lấy 3 sample documents từ mỗi collection
      4. Hiển thị metadata (chunk ID, page number)
    """
    print("""
════════════════════════════════════════════════════════════
 VIEW CHROMADB - XEM THÔNG TIN COLLECTIONS
════════════════════════════════════════════════════════════
    """)
    
    # Kết nối ChromaDB database (phải ở ./db_moodle)
    client = chromadb.PersistentClient(path="./db_moodle")
    
    # Lấy danh sách tất cả collections
    collections = client.list_collections()
    print(f"\nTổng collections: {len(collections)}")
    
    for collection in collections:
        print(f"\n[Collection] {collection.name}")
        print(f"   Số documents: {collection.count()}")
        
        # ========================================================
        # Get sample documents (lấy mẫu)
        # ========================================================
        # collection.get() lấy documents mà không cần query
        # limit=3 là lấy 3 docs đầu tiên
        results = collection.get(limit=3)
        
        if results['documents']:
            print(f"   Sample documents:")
            for i, (doc_id, doc, meta) in enumerate(zip(
                results['ids'],                  # Unique ID của document
                results['documents'],            # Nội dung text
                results['metadatas']             # Metadata (chunk, page)
            )):
                print(f"      [{i+1}] ID: {doc_id}")
                print(f"          Content: {doc[:80]}..." if len(doc) > 80 else f"          Content: {doc}")
                print(f"          Metadata: {json.dumps(meta)}")


def search_documents(collection_name: str, query: str, n_results: int = 5):
    """
    TÌM KIẾM SEMANTIC - Tìm documents liên quan đến query
    
    Cách hoạt động:
      1. Chuyển query text thành vector (embedding)
      2. So sánh vector với tất cả documents đã lưu
      3. Trả về top N documents có ý nghĩa gần nhất (cosine similarity)
      4. Hiển thị distance score (càng nhỏ càng giống)
    
    Ứng dụng:
      - Query: "vòng lặp" → Tìm documents về for, while, loop
      - Query: "hàm" → Tìm documents về functions, methods, procedures
      - Query: "đệ quy" → Tìm documents về recursion, backtracking
    """
    
    client = chromadb.PersistentClient(path="./db_moodle")
    
    try:
        # Lấy collection
        collection = client.get_collection(name=collection_name)
        
        # ========================================================
        # SEMANTIC QUERY - TÌM KIẾM THEO Ý NGHĨA
        # ========================================================
        
        # collection.query() = Tìm kiếm semantic
        # query_texts=[query] = Text để tìm kiếm
        # n_results=5 = Trả về 5 kết quả tốt nhất
        results = collection.query(
            query_texts=[query],           # Query string
            n_results=n_results            # Số kết quả trả về
        )
        
        print(f"\n╔════════════════════════════════════════════════════════════╗")
        print(f"║ TÌM KIẾM SEMANTIC: '{query}'")
        print(f"║ Kết quả: {len(results['documents'][0])} documents")
        print(f"╚════════════════════════════════════════════════════════════╝\n")
        
        # ========================================================
        # HIỂN THỊ KẾT QUẢ
        # ========================================================
        
        for i, (doc_id, doc, meta, dist) in enumerate(zip(
            results['ids'][0],              # Document ID
            results['documents'][0],        # Nội dung text
            results['metadatas'][0],        # Metadata (chunk, page)
            results['distances'][0]         # Distance score (cosine distance)
        )):
            # Distance score: 
            #   - 0.0 = Hoàn toàn giống (perfect match)
            #   - 1.0 = Hoàn toàn khác (no match)
            print(f"[{i+1}] Distance: {dist:.4f} (càng nhỏ càng giống)")
            print(f"    ID: {doc_id}")
            print(f"    Content: {doc[:100]}..." if len(doc) > 100 else f"    Content: {doc}")
            print(f"    Metadata: Chunk {meta.get('chunk')}, Trang {meta.get('page')}")
            print()
    
    except Exception as e:
        print(f"[ERROR] Error: {str(e)}")


def main():
    print("""
════════════════════════════════════════════════════════════
 CHROMADB VIEWER - EXPLORE VECTORDB
════════════════════════════════════════════════════════════

Menu:
  1 - Xem thông tin collections (View collections info)
  2 - Tìm kiếm semantic (Semantic search)
  0 - Thoát (Exit)
    """)
    
    choice = input("Chọn (0-2): ").strip()
    
    if choice == "1":
        view_collection_info()
    elif choice == "2":
        collection_name = input("Nhập tên collection (default: giao_trinh_c): ").strip() or "giao_trinh_c"
        query = input("Nhập query tìm kiếm (vd: 'vòng lặp', 'hàm', 'đệ quy'): ").strip()
        n = input("Số kết quả (default: 5): ").strip() or "5"
        
        try:
            search_documents(collection_name, query, int(n))
        except:
            print("[ERROR] Lỗi!")
    elif choice == "0":
        print("Thoát!")
    else:
        print("[ERROR] Lựa chọn không hợp lệ!")


if __name__ == "__main__":
    main()

