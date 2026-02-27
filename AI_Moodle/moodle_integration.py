import requests
import json
from typing import Dict, List, Optional
import time

class MoodleIntegration:
    """Tích hợp với Moodle LMS qua REST API"""
    
    def __init__(self, moodle_url: str, token: str):
        """
        Khởi tạo kết nối Moodle
        
        Args:
            moodle_url: URL gốc Moodle (ví dụ: http://localhost/moodle)
            token: Web service token từ Moodle
        """
        self.moodle_url = moodle_url.rstrip('/')
        self.token = token
        self.base_url = f"{self.moodle_url}/webservice/rest/server.php"
    
    def _make_request(self, wsfunction: str, params: Dict = None, method: str = "GET"):
        """
        Thực hiện request tới Moodle API
        
        Args:
            wsfunction: Tên function Moodle
            params: Các parameters
            method: GET hoặc POST
        
        Returns:
            Response JSON
        """
        if params is None:
            params = {}
        
        data = {
            'wstoken': self.token,
            'wsfunction': wsfunction,
            'moodlewsrestformat': 'json',
            **params
        }
        
        try:
            if method == "GET":
                response = requests.get(self.base_url, params=data, timeout=10)
            else:
                response = requests.post(self.base_url, data=data, timeout=10)
            
            result = response.json()
            
            if 'exception' in result:
                print(f"❌ Moodle API Error: {result.get('message', 'Unknown error')}")
                return None
            
            return result
            
        except Exception as e:
            print(f"❌ Request Error: {str(e)}")
            return None
    
    def get_courses(self):
        """Lấy danh sách các khóa học"""
        return self._make_request('core_course_get_courses')
    
    def get_course_by_id(self, course_id: int):
        """Lấy thông tin khóa học theo ID"""
        return self._make_request('core_course_get_courses', {'ids[0]': course_id})
    
    def get_question_categories(self, course_id: int):
        """Lấy danh sách category câu hỏi của khóa học"""
        return self._make_request(
            'core_question_get_questions_by_category',
            {'categoryid': course_id}
        )
    
    def create_question_category(self, name: str, parent_id: int = None, contextid: int = None):
        """
        Tạo category câu hỏi
        
        Args:
            name: Tên category
            parent_id: ID category cha (optional)
            contextid: Context ID (optional)
        
        Returns:
            ID category được tạo
        """
        params = {'name': name}
        if parent_id:
            params['parent'] = parent_id
        # Thường contextid = 1 (system context)
        
        return self._make_request('core_question_create_categories', params)
    
    def create_question(self, question_data: Dict):
        """
        Tạo câu hỏi trong Moodle
        
        Cấu trúc question_data:
        {
            'name': 'Tên câu hỏi',
            'questiontext': 'Nội dung câu hỏi',
            'category': category_id,
            'qtype': 'multichoice',
            'options': [
                {'option': 'A', 'text': 'Đáp án A', 'fraction': 0},
                {'option': 'B', 'text': 'Đáp án B', 'fraction': 100},
                ...
            ]
        }
        """
        # Moodle API không trực tiếp tạo question, phải dùng core_question_create_questions
        # Hoặc import XML
        return self._make_request('core_question_create_questions', question_data)
    
    def import_questions_from_xml(self, question_file: str, category_id: int, course_id: int):
        """
        Import câu hỏi từ file XML (Aiken format)
        
        Args:
            question_file: Đường dẫn file XML
            category_id: ID category để import vào
            course_id: ID khóa học
        
        Returns:
            Kết quả import
        """
        try:
            with open(question_file, 'r', encoding='utf-8') as f:
                file_content = f.read()
            
            # Moodle expects base64 encoded file hoặc gửi file upload
            # Sử dụng core_import_questions nếu có plugin
            
            # Cách thay thế: Dùng webservice upload_files và sau đó import
            # Nhưng đơn giản hơn là dùng moodle CLI hoặc web interface
            
            print("⚠️  Để import file XML, hãy upload qua Moodle web interface:")
            print(f"   Course Settings → Question bank → Import")
            print(f"   Chọn file: {question_file}")
            
            return True
            
        except Exception as e:
            print(f"❌ Error reading file: {str(e)}")
            return False
    
    def test_connection(self):
        """Test kết nối Moodle"""
        result = self.get_courses()
        if result:
            print("✅ Kết nối Moodle thành công!")
            return True
        else:
            print("❌ Kết nối Moodle thất bại!")
            return False

def guide_moodle_setup():
    """Hướng dẫn setup Moodle Web Services"""
    print("""
╔════════════════════════════════════════════════════════════╗
║         HƯỚNG DẪN SETUP MOODLE WEB SERVICES               ║
╚════════════════════════════════════════════════════════════╝

1. BƯỚC 1: Enable Web Services trên Moodle
   - Đăng nhập Moodle với tài khoản Admin
   - Site Administration → Advanced features → Enable web services ✓
   - Lưu thay đổi

2. BƯỚC 2: Tạo Web Service
   - Site Administration → Plugins → Web services → Manage services
   - Tạo service mới:
     • Name: "AI Question Generator"
     • Enable service: ✓
     • Restrict by IP: ✗ (hoặc thêm IP máy của bạn)
     • Token generated: ✓

3. BƯỚC 3: Add Functions vào Service
   - Click vào service vừa tạo
   - Add functions cần thiết:
     • core_course_get_courses
     • core_question_get_categories
     • core_question_create_questions
     • core_question_update_questions

4. BƯỚC 4: Tạo User Token
   - Site Administration → Plugins → Web services → Manage tokens
   - Tạo token mới:
     • User: (chọn user của bạn)
     • Service: "AI Question Generator"
   - Copy token và lưu


5. THÔNG TIN CẦN CÓ:
   - Moodle URL: http://your-moodle-url
   - Token: xxxxxxxxxxxxxxxxxxxxxxxxxxxxx
   - Course ID: (tìm ở URL khi vào khóa học, ?id=XXX)

6. CÁCH IMPORT CÂU HỎI:
   Option A: Dùng Moodle Web Interface (dễ nhất)
      - Course → Settings → Question bank → Import
      - Chọn file XML → Choose import format: Aiken → Upload
   
   Option B: Dùng Moodle CLI (cần SSH access)
      - php admin/tool/importquestions/cli/import.php
   
   Option C: Dùng API (nếu Moodle plugin hỗ trợ)
      - Sử dụng script Python dưới đây

═══════════════════════════════════════════════════════════════
    """)

def interactive_setup():
    """Thiết lập interactively"""
    print("\n📋 THIẾT LẬP MOODLE INTEGRATION\n")
    
    moodle_url = input("Nhập Moodle URL (ví dụ: http://localhost/moodle): ").strip()
    token = input("Nhập Web Service Token: ").strip()
    
    if not moodle_url or not token:
        print("❌ URL hoặc Token không được để trống!")
        return None
    
    # Test connection
    print("\n🔗 Test kết nối...")
    integration = MoodleIntegration(moodle_url, token)
    
    if integration.test_connection():
        print("\n✅ Setup thành công!")
        return integration
    else:
        print("\n❌ Không thể kết nối đến Moodle")
        print("Vui lòng kiểm tra:")
        print("  - Moodle URL có đúng không?")
        print("  - Token có hợp lệ không?")
        print("  - Web services có enable trên Moodle không?")
        return None

if __name__ == "__main__":
    # Hiển thị guide
    guide_moodle_setup()
    
    # Setup interactively (optional)
    # moodle = interactive_setup()
    # if moodle:
    #     courses = moodle.get_courses()
    #     print(f"✅ Tìm thấy {len(courses)} khóa học")
