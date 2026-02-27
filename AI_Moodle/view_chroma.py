#!/usr/bin/env python3
"""
🔍 XEM DỮ LIỆU LƯUTRỮ TRONG CHROMADB
"""

import chromadb

def view_chroma_data():
    """Xem toàn bộ dữ liệu lưu trong ChromaDB"""
    
    print("""
╔════════════════════════════════════════════════════════════╗
║          XEM DỮ LIỆU CHROMADB                             ║
╚════════════════════════════════════════════════════════════╝
    """)
    
    try:
        # Kết nối ChromaDB
        client = chromadb.PersistentClient(path="./db_moodle")
        
        # Liệt kê các collection
        print("📚 Danh sách Collections:")
        collections = client.list_collections()
        print(f"   Tìm thấy: {len(collections)} collection\n")
        
        for col in collections:
            print(f"   ├─ {col.name}")
        
        # Xem chi tiết collection "giao_trinh_c"
        print("\n" + "="*70)
        print("📖 CHI TIẾT COLLECTION: giao_trinh_c")
        print("="*70 + "\n")
        
        collection = client.get_collection(name="giao_trinh_c")
        
        # Thống kê
        count = collection.count()
        print(f"📊 Tổng số documents: {count}\n")
        
        # Xem một số documents
        print("📄 Danh sách 10 document đầu tiên:\n")
        
        all_data = collection.get(limit=count)
        
        for i, (doc_id, document, metadata) in enumerate(
            zip(all_data['ids'], all_data['documents'], all_data['metadatas']), 1
        ):
            print(f"{i}. ID: {doc_id}")
            print(f"   📝 Nội dung: {document[:100]}...")
            if metadata:
                print(f"   📌 Metadata: {metadata}")
            print()
            
            if i >= 10:  # Chỉ show 10 cái đầu
                break
        
        if count > 10:
            print(f"   ... và {count - 10} document khác")
        
        # Thử search
        print("\n" + "="*70)
        print("🔎 THỬ SEARCH TEST")
        print("="*70 + "\n")
        
        query = "Giải thuật"
        results = collection.query(query_texts=[query], n_results=3)
        
        print(f"Tìm kiếm: '{query}'\n")
        print(f"Tìm thấy {len(results['documents'][0])} kết quả:\n")
        
        for i, (doc, dist) in enumerate(zip(results['documents'][0], results['distances'][0]), 1):
            print(f"{i}. [Distance: {dist:.4f}]")
            print(f"   {doc[:150]}...")
            print()
        
        print("\n✅ Hoàn tất!")
        
    except Exception as e:
        print(f"❌ Lỗi: {str(e)}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    view_chroma_data()
