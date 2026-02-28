#!/usr/bin/env python3
"""
MOODLE INTEGRATION - Tích hợp API Moodle
Gửi câu hỏi vào Moodle thông qua REST API
"""

import requests
import json
from typing import Dict, List, Optional

class MoodleAPI:
    """Wrapper cho Moodle REST API"""
    
    def __init__(self, moodle_url: str, web_service_token: str):
        """
        Khởi tạo Moodle API client
        
        Args:
            moodle_url: URL của server Moodle (vd: https://moodle.example.com)
            web_service_token: Token xác thực (lấy từ User > Preferences > Web services)
        """
        self.moodle_url = moodle_url.rstrip('/')
        self.token = web_service_token
        self.base_url = f"{self.moodle_url}/webservice/rest/server.php"
        
    def _call_api(self, method: str, params: Dict = None) -> Dict:
        """Gọi Moodle API"""
        if params is None:
            params = {}
        
        params['wstoken'] = self.token
        params['wsfunction'] = method
        params['moodlewsrestformat'] = 'json'
        
        try:
            response = requests.post(self.base_url, data=params, timeout=10)
            response.raise_for_status()
            return response.json()
        except Exception as e:
            print(f"[ERROR] API Error: {str(e)}")
            return None
    
    def get_site_info(self) -> Optional[Dict]:
        """Lấy thông tin server Moodle"""
        return self._call_api('moodle_webservice_get_siteinfo')
    
    def get_courses(self, user_id: int = 0) -> Optional[List]:
        """Lấy danh sách khóa học"""
        params = {'userid': user_id} if user_id else {}
        result = self._call_api('core_user_get_courses_by_field', params)
        return result.get('courses', []) if result else None
    
    def get_course_categories(self) -> Optional[List]:
        """Lấy danh sách danh mục khóa học"""
        result = self._call_api('core_course_get_categories')
        return result if result else None
    
    def create_question(self, 
                       course_id: int,
                       question_name: str,
                       question_text: str,
                       answer_a: str,
                       answer_b: str,
                       answer_c: str,
                       answer_d: str,
                       correct_answer: str = 'A') -> Optional[Dict]:
        """
        Tạo câu hỏi trắc nghiệm
        
        Args:
            course_id: ID của khóa học
            question_name: Tên câu hỏi
            question_text: Nội dung câu hỏi
            answer_a, answer_b, answer_c, answer_d: Các option
            correct_answer: Đáp án đúng (A/B/C/D)
        """
        
        # Validate
        if correct_answer not in ['A', 'B', 'C', 'D']:
            print(f"[ERROR] Invalid correct answer: {correct_answer}")
            return None
        
        # Map letter to index
        answer_map = {'A': 0, 'B': 1, 'C': 2, 'D': 3}
        correct_idx = answer_map[correct_answer]
        
        # Chuyển đổi sang Moodle question format
        question_data = {
            'courseid': course_id,
            'questions': [{
                'type': 'multichoice',
                'name': question_name,
                'questiontext': question_text,
                'questiontextformat': 1,
                'defaultmark': 1,
                'penalty': 0,
                'hidden': 0,
                'option': [answer_a, answer_b, answer_c, answer_d],
                'fraction': [
                    100 if i == correct_idx else 0 
                    for i in range(4)
                ],
                'feedback': [''] * 4
            }]
        }
        
        # Gọi API (simplified - actual implementation needs proper format)
        print(f"[INFO] Creating question: {question_name}")
        return question_data
    
    def create_quiz(self, course_id: int, quiz_name: str, quiz_desc: str = "") -> Optional[Dict]:
        """Tạo bài quiz"""
        params = {
            'courseid': course_id,
            'name': quiz_name,
            'intro': quiz_desc,
        }
        result = self._call_api('core_course_create_modules', params)
        return result
    
    def get_quiz_questions(self, quiz_id: int) -> Optional[List]:
        """Lấy danh sách câu hỏi trong quiz"""
        params = {'quizid': quiz_id}
        result = self._call_api('mod_quiz_get_quiz_questions', params)
        return result.get('questions', []) if result else None
    
    def add_question_to_quiz(self, quiz_id: int, question_id: int, page: int = 0) -> bool:
        """Thêm câu hỏi vào quiz"""
        params = {
            'quizid': quiz_id,
            'questionid': question_id,
            'page': page
        }
        result = self._call_api('mod_quiz_add_quiz_questions', params)
        return result is not None
    
    def get_enrolled_users(self, course_id: int) -> Optional[List]:
        """Lấy danh sách học viên đã ghi danh"""
        params = {'courseid': course_id}
        result = self._call_api('core_enrol_get_enrolled_users', params)
        return result if result else None
    
    def update_question(self, question_id: int, question_data: Dict) -> bool:
        """Cập nhật câu hỏi"""
        params = {
            'questionid': question_id,
            **question_data
        }
        result = self._call_api('core_question_update_questions', params)
        return result is not None
    
    def delete_question(self, question_id: int) -> bool:
        """Xóa câu hỏi"""
        params = {'questionid': question_id}
        result = self._call_api('core_question_delete_questions', params)
        return result is not None
    
    def get_user_profile(self, user_id: int) -> Optional[Dict]:
        """Lấy thông tin profile người dùng"""
        params = {'userid': user_id, 'userfields': 'id,username,fullname,email'}
        result = self._call_api('core_user_get_users', params)
        return result.get('users', [])[0] if result and result.get('users') else None
    
    def batch_import_questions(self, course_id: int, questions: List[Dict]) -> int:
        """Nhập batch câu hỏi"""
        count = 0
        for q in questions:
            result = self.create_question(
                course_id=course_id,
                question_name=q.get('name', 'Untitled'),
                question_text=q.get('text', ''),
                answer_a=q.get('options', ['', '', '', ''])[0],
                answer_b=q.get('options', ['', '', '', ''])[1],
                answer_c=q.get('options', ['', '', '', ''])[2],
                answer_d=q.get('options', ['', '', '', ''])[3],
                correct_answer=q.get('answer', 'A')
            )
            if result:
                count += 1
        return count

def test_connection(moodle_url: str, token: str) -> bool:
    """Kiểm tra kết nối Moodle"""
    print(f"\nKiểm tra kết nối: {moodle_url}")
    
    api = MoodleAPI(moodle_url, token)
    info = api.get_site_info()
    
    if info:
        print(f"[OK] Kết nối thành công!")
        print(f"    Site: {info.get('sitename', 'Unknown')}")
        print(f"    Version: {info.get('version', 'Unknown')}")
        return True
    else:
        print(f"[ERROR] Không thể kết nối!")
        return False

def main():
    print("""
════════════════════════════════════════════════════════════
 MOODLE INTEGRATION TEST
════════════════════════════════════════════════════════════
    """)
    
    # Config
    MOODLE_URL = input("Nhập URL Moodle (vd: https://moodle.example.com): ").strip()
    TOKEN = input("Nhập Web Service Token: ").strip()
    
    if not MOODLE_URL or not TOKEN:
        print("[ERROR] URL và Token không được để trống!")
        return
    
    # Test kết nối
    if test_connection(MOODLE_URL, TOKEN):
        api = MoodleAPI(MOODLE_URL, TOKEN)
        
        # Lấy danh sách khóa học
        print("\nLấy danh sách khóa học...")
        courses = api.get_courses()
        
        if courses:
            print(f"Tìm thấy {len(courses)} khóa học:")
            for c in courses[:5]:
                print(f"   - {c.get('fullname', 'Unknown')} (ID: {c.get('id')})")
        else:
            print("[INFO] Không tìm thấy khóa học nào")

if __name__ == "__main__":
    main()

