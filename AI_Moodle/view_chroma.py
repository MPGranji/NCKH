#!/usr/bin/env python3
"""
VIEW CHROMA - Xem dữ liệu trong ChromaDB
"""

import chromadb
import json

def view_collection_info():
    """Xem thông tin collection"""
    print("""
════════════════════════════════════════════════════════════
 VIEW CHROMADB
════════════════════════════════════════════════════════════
    """)
    
    # Kết nối ChromaDB
    client = chromadb.PersistentClient(path="./db_moodle")
    
    # List collections
    collections = client.list_collections()
    print(f"\nTổng collections: {len(collections)}")
    
    for collection in collections:
        print(f"\n[Collection] {collection.name}")
        print(f"   Số documents: {collection.count()}")
        
        # Get sample documents
        results = collection.get(limit=3)
        if results['documents']:
            print(f"   Sample documents:")
            for i, (doc_id, doc, meta) in enumerate(zip(
                results['ids'], 
                results['documents'], 
                results['metadatas']
            )):
                print(f"      [{i+1}] ID: {doc_id}")
                print(f"          Content: {doc[:80]}..." if len(doc) > 80 else f"          Content: {doc}")
                print(f"          Metadata: {json.dumps(meta)}")

def search_documents(collection_name: str, query: str, n_results: int = 5):
    """Tìm kiếm documents"""
    client = chromadb.PersistentClient(path="./db_moodle")
    
    try:
        collection = client.get_collection(name=collection_name)
        results = collection.query(query_texts=[query], n_results=n_results)
        
        print(f"\nTìm kiếm: '{query}'")
        print(f"Kết quả: {len(results['documents'][0])} documents\n")
        
        for i, (doc, meta, dist) in enumerate(zip(
            results['documents'][0],
            results['metadatas'][0],
            results['distances'][0]
        )):
            print(f"[{i+1}] Distance: {dist:.4f}")
            print(f"    Content: {doc[:100]}..." if len(doc) > 100 else f"    Content: {doc}")
            print(f"    Metadata: {json.dumps(meta)}")
            print()
    
    except Exception as e:
        print(f"[ERROR] Error: {str(e)}")

def main():
    print("""
════════════════════════════════════════════════════════════
 CHROMADB VIEWER
════════════════════════════════════════════════════════════

Menu:
  1 - Xem thông tin collections
  2 - Tìm kiếm documents
  0 - Thoát
    """)
    
    choice = input("Chọn (0-2): ").strip()
    
    if choice == "1":
        view_collection_info()
    elif choice == "2":
        collection_name = input("Nhập tên collection (default: giao_trinh_c): ").strip() or "giao_trinh_c"
        query = input("Nhập query tìm kiếm: ").strip()
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

