# REVIEW NCKH: Giao Trinh_Lap_Trinh_Can_Ban_A_V2.pdf

## TRANG 1
Giáo_trình Lập_trình căn_bản 
 Lâm_Hoài_Bảo , Dương Văn Hiếu , Nguyễn_Văn_Linh 
 Khoa Công_Nghệ_Thông_Tin & Truyền_Thông , Đại_Học Cần_Thơ 
 2005

---

## TRANG 2
Lập_trình căn_bản 
 MỤC_LỤC 
 Mở_đầu 
 Chương 1 : GIẢI_THUẬT VÀ BIỂU_DIỄN_GIẢI_THUẬT 
 Chương 2 : TỔNG_QUAN VỀ NGÔN_NGỮ LẬP_TRÌNH C 
 Chương 3 : CÁC CÂU_LỆNH ĐƠN TRONG C 
 Chương 4 : CÁC LỆNH CÓ CẤU_TRÚC 
 Chương 5 : CHƯƠNG_TRÌNH CON ( HÀM ) 
 Chương 6 : MẢNG 
 Chương 7 : CON_TRỎ 
 Chương 8 : CHUỖI KÝ_TỰ 
 Chương 9 : KIỂU CẤU_TRÚC – STRUCT 
 Chương 10 : TẬP_TIN 
 TÀI_LIỆU THAM_KHẢO

---

## TRANG 3
Lập_trình căn_bản 
 MỞ_ĐẦU 
 I. MỤC_ĐÍCH 
 Quyển sách này cung_cấp cho người đọc những kiến_thức cơ_bản 
 về lập_trình thông_qua ngôn_ngữ lập_trình C._Đây là cơ_sở để 
 người đọc từng bước tiếp_cận với thế_giới lập_trình , từ đó người 
 đọc có một nền_tảng vững_chắc để có_thể tiếp_thu hầu_hết các lĩnh 
 vực trong chuyên_ngành Công_Nghệ_Thông_Tin . 
 Các vấn_đề chính được trình_bày trong quyển sách này : 
  Các khái_niệm : ngôn_ngữ lập_trình , kiểu dữ_liệu . 
  Khái_niệm giải_thuật và biểu_diễn_giải_thuật 
_ Ngôn_ngữ lập_trình C ( sau đây gọi tắt là C ) : 
  Các thành_phần của C. 
  Các kiểu dữ_liệu trong C. 
  Các câu_lệnh trong C. 
  Cách thiết_kế và sử_dụng các hàm trong C. 
  Một_số cấu_trúc dữ_liệu trong C.

---

## TRANG 4
Lập_trình căn_bản 
 Chương 1 
 GIẢI_THUẬT VÀ BIỂU_DIỄN_GIẢI_THUẬT 
 Các vấn_đề được trình_bày trong chương này : 
  Từ bài_toán đến chương_trình 
  Giải_thuật và biểu_diễn_giải_thuật 
  Một_số khái_niệm : kiểu dữ_liệu , ngôn_ngữ lập_trình , chương 
 trình dịch 
 Nội_dung chính của chương này là giải_thuật & các cách biểu 
 diễn_giải_thuật . Lý_do vì chương_trình máy_tính của một bài_toán 
 cụ_thể được tạo ra từ các biểu_diễn của giải_thuật . 
 I. TỪ BÀI_TOÁN ĐẾN CHƯƠNG_TRÌNH 
 Theo [ 6 ] , mọi bài_toán đều có_thể được diễn_giải theo một sơ 
 đồ chung : A  B 
 Trong đó : 
  A là giả_thiết , là điều_kiện ban_đầu . 
  B là kết_luận , là mục_tiêu cần đạt hoặc là cái phải tìm . 
   là suy_luận , là giải_pháp cần thực_hiện để tìm B từ cái đã 
 biết A. 
 Một bài_toán trên máy_tính cũng mang đầy_đủ các tính_chất của 
 bài_toán ở trên . Trong đó : 
  A là thông_tin vào ( đầu_vào - input ) 
  B là thông_tin ra ( đầu_ra - output ) 
   là chương_trình tạo ra từ các lệnh cơ_bản của máy_tính 
 cho phép tạo B từ A. 
 Như_vậy , việc giải một bài_toán trên máy_tính là việc xác_định 
 các yếu_tố đầu_vào , đầu_ra cũng như xác_định cách giải_quyết bài 
 toán bằng chương_trình máy_tính .

---

## TRANG 5
Lập_trình căn_bản 
 Thí_dụ : Giả_sử có hai bình B1 và B2 đựng hai loại chất_lỏng 
 khác nhau , chẳng_hạn bình B1 đựng rượu , bình B2 đựng nước 
 mắm . Làm thế_nào để hoán_đổi chất_lỏng trong 02 bình , tức_bình 
 B1 đựng nước_mắm , bình B2 đựng rượu ? 
  Đầu_vào của bài_toán là 02 bình B1 , B2 với mỗi bình lần 
 lượt chứa rượu và nước_mắm . 
  Đầu_ra của bài_toán là bình B1 chứa nước_mắm , bình B2 
 chứa rượu . 
  Một dãy các bước để thực_hiện bài_toán này là : 
 o Có thêm một bình thứ ba gọi là B3 . 
 o Bước 1 : Đổ rượu từ bình B1 vào bình B3 . 
 o Bước 2 : Đổ nước_mắm từ bình B2 sang bình B1 . 
 o Bước 3 : Đổ rượu từ bình B3 sang B2 . 
 Trong thí_dụ trên , dãy các bước để thực_hiện bài_toán hoán 
 đổi chất_lỏng trong 02 bình chưa phải là 1 chương_trình . Tuy 
 nhiên chương_trình máy_tính thực_hiện bài_toán này được cài_đặt 
 với các lệnh được mô_tả gần với cách mô_tả trong dãy các bước 
 trên . Dãy các bước trên còn được gọi là giải_thuật để giải bài_toán 
 hoán_đổi chất_lỏng trong 02 bình trên . 
 II. GIẢI_THUẬT 
 II. 1 . Khái_niệm giải_thuật 
 Giải_thuật là một hệ_thống chặt_chẽ và rõ_ràng các quy_tắc 
 nhằm xác_định một dãy các thao_tác trên những dữ_liệu vào sao 
 cho sau một_số hữu_hạn bước thực_hiện các thao_tác đó ta thu 
 được kết_quả của bài_toán . 
 Thí_dụ : Tìm ước_số chung lớn nhất của 2 số_nguyên a , b . 
  Đầu_vào : 2 số_nguyên a , b . 
  Đầu_ra : ước_số chung lớn nhất của a , b 
  Giải_thuật : 
 o Bước 1 : Nhập vào hai số a và b .

---

## TRANG 6
Lập_trình căn_bản 
 o Bước 2 : So_sánh 2 số a , b chọn số nhỏ nhất gán cho 
 UCLN. 
 o Bước 3 : Nếu một trong hai số a hoặc b không chia hết_cho 
 UCLN thì thực_hiện bước 4 , ngược_lại ( cả a và b đều chia 
 hết cho UCLN ) thì thực_hiện bước 5 . 
 o Bước 4 : Giảm UCLN một đơn_vị và quay lại bước 3 
 o Bước 5 : In UCLN - Kết_thúc . 
 II. 2 Các đặc_trưng của giải_thuật 
  Tính kết_thúc : Giải_thuật phải dừng sau một_số hữu_hạn 
 bước . 
  Tính xác_định : Các thao_tác máy_tính phải thực_hiện được và 
 các máy_tính khác nhau thực_hiện cùng một bước của cùng một 
 giải_thuật phải cho_cùng một kết_quả . 
  Tính phổ_dụng : Giải_thuật phải " vét ' hết các trường_hợp và 
 áp_dụng cho một loạt bài_toán cùng loại . 
  Tính hiệu_quả : Một giải_thuật được đánh_giá là tốt nếu nó đạt 
 hai tiêu_chuẩn sau : 
 o Thực_hiện nhanh , tốn ít thời_gian . 
 o Tiêu_phí ít tài_nguyên của máy , chẳng_hạn tốn ít bộ_nhớ . 
 Giải_thuật tìm UCLN nêu trên đạt tính kết_thúc bởi_vì qua mỗi 
 lần thực_hiện bước 4 thì UCLN sẽ giảm đi một đơn_vị cho_nên 
 trong trường_hợp xấu nhất thì UCLN = 1 , giải_thuật phải dừng . 
 Các thao_tác trình_bày trong các bước , máy_tính đều có_thể thực 
 hiện được nên nó có tính xác_định . Giải_thuật này cũng đạt tính 
 phổ_dụng vì nó được dùng để tìm UCLN cho hai số_nguyên 
 dương a và b bất_kỳ . Tuy_nhiên tính hiệu_quả của giải_thuật có_thể 
 chưa cao ; cụ_thể là thời_gian chạy máy có_thể còn tốn nhiều hơn 
 một_số giải_thuật khác ` mà chúng_ta sẽ có dịp trở_lại trong các 
 chương tiếp_theo . 
 II. 3 Ngôn_ngữ biểu_diễn_giải_thuật 
 Để biểu_diễn_giải_thuật , cần phải có một tập_hợp các ký_hiệu dùng 
 để biểu_diễn , mỗi ký_hiệu biểu_diễn cho một hành_động nào đó . 
 Tập_hợp các ký_hiệu đó lại tạo_thành ngôn_ngữ biểu_diễn_giải 
 thuật .

---

## TRANG 7
Lập_trình căn_bản 
 II. 3.1 Ngôn_ngữ tự_nhiên 
 Ngôn_ngữ tự_nhiên là ngôn_ngữ của chúng_ta đang sử_dụng . 
 Chẳng_hạn , các thí_dụ ở trên dùng ngôn_ngữ tự_nhiên để biểu_diễn 
 giải_thuật . 
 Thí_dụ : Giải_thuật giải phương_trình bậc nhất dạng ax + b = 0 
 như sau : 
  Đầu_vào : 2 số_thực a , b . 
  Đầu_ra : Các kết_luận về các trường_hợp nghiệm của 
 phương_trình ax + b = 0 . 
  Giải_thuật : 
 o Bước 1 : Nhận giá_trị của các tham_số a , b 
 o Bước 2 : Xét giá_trị của a xem có bằng 0 hay không ? Nếu 
 a = 0 thì làm bước 3 , nếu a khác không thì làm bước 4 . 
 o Bước 3 : ( a bằng 0 ) Nếu b bằng 0 thì ta kết_luận phương 
 trình vô_số nghiệm , nếu b khác 0 thì ta kết_luận phương 
 trình vô_nghiệm . 
 o Bước 4 : ( a khác 0 ) Kết_luận phương_trình có nghiệm 
 x = - b / a . 
 II. 3.2 Lưu_đồ 
 Lưu_đồ là một tập ký_hiệu trực_quan dùng để thể_hiện giải_thuật . 
 Các ký_hiệu được sử_dụng trong lưu_đồ được cho trong bảng sau :

---

## TRANG 8
Lập_trình căn_bản

| Ký hiệu | Ý nghĩa |
| --- | --- |
|  | Bắt đầu/ Kết thúc |
|  | Nhập/Xuất |
|  | Tính toán (xử lý) |
|  | Quyết định và rẽ nhánh |
|  | Khối nối |
|  | Đường đi |


Chẳng_hạn lưu_đồ để biểu_diễn_giải_thuật tìm ước_số chung lớn 
 nhất theo cách_thức như trên là :

---

## TRANG 9
Lập_trình căn_bản 
 II. 3.3 Một_số thí_dụ 
 Thí_dụ 1 : Cần viết chương_trình cho máy_tính sao cho khi thực 
 hiện chương_trình đó , máy_tính yêu_cầu người sử_dụng chương 
 trình nhập vào các số_hạng của tổng ( n ) ; nhập vào dãy các số 
 hạng a của tổng . Sau đó , máy_tính sẽ thực_hiện việc tính tổng_các 
 i 
 số a này và in kết_quả của tổng_tính được . 
 i 
 Yêu_cầu : Tính tổng_n số S = a + a + a + ... ... + a . 
 1 2 3 n 
 Để tính tổng trên , chúng_ta sử_dụng phương_pháp “ cộng 
 tích_lũy ” nghĩa_là khởi_đầu cho S = 0 . Sau mỗi lần nhận được một 
 số_hạng a từ bàn_phím , ta cộng tích_lũy a vào S ( lấy giá_trị được 
 i i 
 lưu_trữ trong S , cộng thêm a và lưu trở_lại vào S ) . Tiếp_tục quá 
 i 
 trình này đến khi ta tích_lũy được a vào S thì ta có S là tổng_các 
 n 
 a . Chi_tiết giải_thuật được mô_tả bằng ngôn_ngữ tự_nhiên như sau : 
 i 
 o Bước 1 : Nhập số các số_hạng n . 
 o Bước 2 : Cho S = 0 ( lưu_trữ số 0 trong S ) 
 o Bước 3 : Cho i = 1 ( lưu_trữ số 1 trong i ) 
 o Bước 4 : Kiểm_tra nếu i < = n thì thực_hiện bước 5 , ngược_lại 
 thực_hiện bước 8 . 
 o Bước 5 : Nhập_a 
 i 
 o Bước 6 : Cho S = S + a ( lưu_trữ giá_trị S + a trong S ) 
 i i 
 o Bước 7 : Tăng i lên 1 đơn_vị và quay lại bước 4 . 
 o Bước 8 : In S và kết_thúc chương_trình . 
 Chi_tiết giải_thuật trên bằng lưu_đồ :

---

## TRANG 10
Lập_trình căn_bản 
 Thí_dụ 2 : Viết chương_trình cho phép nhập vào 2 giá_trị a , b 
 mang ý_nghĩa_là các hệ_số a , b của phương_trình bậc nhất . Dựa 
 vào các giá_trị a , b đó cho biết nghiệm của phương_trình bậc nhất 
 ax + b = 0 . 
 Mô_tả giải_thuật bằng ngôn_ngữ tự_nhiên ( trang 6 ) 
 Lưu_đồ của giải_thuật giải phương_trình bậc nhất :

---

## TRANG 11
Lập_trình căn_bản 
 Thí_dụ 3 : Viết chương_trình cho phép nhập vào 1 số n , sau đó 
 lần_lượt nhập vào n giá_trị a , a , … , a . Hãy tìm và in ra giá_trị lớn 
 1 2 n 
 nhất trong n số a , a , … , a . 
 1 2 n 
 Để giải_quyết bài_toán trên , chúng_ta áp_dụng phương_pháp 
 “ thử và sửa ” . Ban_đầu giả_sử a là số lớn nhất ( được lưu trong giá 
 1 
 trị max ) ; sau đó lần_lượt xét các a còn lại , nếu a nào lớn hơn giá 
 i i 
 trị max thi lúc đó max sẽ nhận giá_trị là a . Sau khi đã xét hết các 
 i 
 a thì max chính là giá_trị lớn nhất cần tìm . 
 i 
 Mô_tả giải_thuật bằng ngôn_ngữ tự_nhiên : 
 o Bước 1 : Nhập số n 
 o Bước 2 : Nhập số thứ nhất a 
 1 
 o Bước 3 : Gán max = a 
 1 
 o Bước 4 : Gán i = 2 
 o Bước 5 : Nếu i < = n thì thực_hiện bước 6 , ngược_lại thực 
 hiện bước 9 
 o Bước 6 : Nhập_a 
 i 
 o Bước 7 : Nếu max < a thì gán max = a . 
 i i 
 o Bước 8 : Tăng i lên một đơn_vị và quay lại bước 5 
 o Bước 9 : In max - kết_thúc 
 Phần mô_tả giải_thuật bằng lưu_đồ , độc_giả có_thể xem như 1 
 bài_tập . 
 Thí_dụ 4 : Viết chương_trình cho phép nhập vào 1 số n , sau đó 
 lần_lượt nhập vào n giá_trị a , a , … , a . Sắp theo thứ tự tăng dần 
 1 2 n 
 một dãy n số a , a , ... a nói trên . 
 1 2 n 
 Dưới đây là một trong những phương_pháp để sắp_xếp thứ_tự 
 1 dãy các số : 
 Giả_sử ta đã nhập vào 1 dãy n số a , a , ... , a . Việc sắp_xếp dãy 
 1 2 n 
 số này trải qua ( n - 1 ) lần : 
  Lần 1 : So_sánh phần_tử đầu_tiên với tất_cả các phần_tử đứng 
 sau phần_tử đầu_tiên . Nếu có phần_tử nào nhỏ hơn phần_tử đầu 
 tiên thì đổi chỗ phần_tử đầu_tiên với phần_tử nhỏ hơn đó . Sau 
 lần 1 , ta được phần_tử đầu_tiên là phần_tử nhỏ nhất .

---

## TRANG 12
Lập_trình căn_bản 
  Lần 2 : So_sánh phần_tử thứ 2 với tất_cả các phần_tử đứng 
 sau phần_tử thứ 2 . Nếu có phần_tử nào nhỏ hơn phần_tử thứ 2 
 thì đổi chỗ phần_tử thứ 2 với phần_tử nhỏ hơn đó . Sau lần 2 , 
 ta được phần_tử đầu_tiên và phần_tử thứ 2 là đúng vị_trí của nó 
 khi sắp_xếp . 
  … 
  Lần ( n - 1 ) : So_sánh phần_tử thứ ( n - 1 ) với phần_tử đứng sau 
 phần_tử ( n - 1 ) là phần_tử thứ n . Nếu phần_tử thứ n nhỏ hơn 
 phần_tử thứ ( n - 1 ) thì đổi chỗ 2 phần_tử này . 
 Sau lần thứ ( n - 1 ) , ta được danh_sách gồm n phần_tử được sắp 
 thứ_tự . 
 Mô_tả giải_thuật bằng ngôn_ngữ tự_nhiên : 
 o Bước 1 : Gán i = 1 
 o Bước 2 : Gán j = i + 1 
 o Bước 3 : Nếu i < = n - 1 thì thực_hiện bước 4 , ngược_lại thực 
 hiện bước 8 
 o Bước 4 : Nếu j < = n thì thực_hiện bước 5 , ngược_lại thì thực 
 hiện bước 7 . 
 o Bước 5 : Nếu a > a thì hoán_đổi a và a cho nhau ( nếu 
 i j i j 
 không thì thôi ) . 
 o Bước 6 : Tăng j lên một đơn_vị và quay lại bước 4 
 o Bước 7 : Tăng i lên một đơn_vị và quay lại bước 3 
 o Bước 8 : In dãy số a , a , ... , a - Kết_thúc . 
 1 2 n 
 II. 4 Các cấu_trúc suy_luận cơ_bản của giải_thuật 
 Giải_thuật được thiết_kế theo các cấu_trúc suy_luận cơ_bản sau 
 đây : 
 II. 4.1 Tuần_tự ( Sequential ) : Các công_việc được thực_hiện một 
 cách tuần_tự , công_việc này nối_tiếp công_việc kia .

---

## TRANG 13
Lập_trình căn_bản 
 II. 4.2 Lựa_chọn ( Selection ) : Lựa_chọn một công_việc để thực_hiện 
 căn_cứ vào một điều_kiện nào đó . Một_số biến_thể của cấu_trúc 
 này như sau : 
 1 : Nếu < điều_kiện > ( đúng ) thì thực_hiện < công_việc > 
 2 : Nếu < điều_kiện > ( đúng ) thì thực_hiện < công_việc 1 > , 
 ngược_lại ( điều_kiện sai ) thì thực_hiện < công_việc 2 > 
 3 : Trường_hợp < i > thực_hiện < công_việc i > 
 II. 4.3 . Lặp ( Repeating ) 
 Thực_hiện lặp lại một công_việc không hoặc nhiều lần căn_cứ vào 
 một điều_kiện nào đó . Có hai dạng như sau : 
 - Lặp_xác_định : là loại lặp mà khi mô_tả giải_thuật , số lần 
_lặp của công_việc đã được xác_định . 
 - Lặp không xác_định : là loại lặp mà khi mô_tả giải_thuật , 
 số lần lặp của công_việc chưa thể xác_định . Tùy_thuộc vào những 
 lần thực_thi khác nhau của chương_trình cài_đặt giải_thuật , số lần 
 lặp có_thể khác nhau . 
 III. MỘT_SỐ KHÁI_NIỆM KHÁC 
 III. 1 . Ngôn_ngữ lập_trình 
 Ngôn_ngữ lập_trình là một ngôn_ngữ dùng để viết chương_trình 
 cho máy_tính . Ta có_thể_chia ngôn_ngữ lập_trình thành các loại 
 sau : ngôn_ngữ_máy , hợp ngữ và ngôn_ngữ cấp cao . 
 Ngôn_ngữ_máy ( machine language ) : Là các chỉ_thị dưới dạng_nhị 
 phân , can_thiệp trực_tiếp vào trong các mạch điện_tử . Chương 
 trình được viết bằng ngôn_ngữ_máy thì có_thể được thực_hiện 
 ngay không cần qua bước trung_gian nào . Tuy_nhiên chương_trình 
 viết bằng ngôn_ngữ_máy dễ sai_sót , cồng_kềnh và khó đọc , khó 
 hiểu vì toàn những con_số 0 và 1 . 
 Hợp ngữ ( assembly language ) : Bao_gồm tên các câu_lệnh và quy 
 tắc viết các câu_lệnh đó . Tên các câu_lệnh bao_gồm hai phần :

---

## TRANG 14
Lập_trình căn_bản 
 phần mã lệnh ( viết tựa tiếng Anh ) chỉ phép_toán cần thực_hiện và 
 địa_chỉ chứa toán hạng của phép_toán đó . Thí_dụ : 
 INPUT a ; Nhập giá_trị cho a từ bàn_phím 
 LOAD a ; Đọc giá_trị a vào thanh ghi tổng A 
 PRINT a ; Hiển_thị_giá_trị của a ra màn_hình . 
 INPUT b 
 ADD b ; Cộng giá_trị của thanh ghi tổng A với giá_trị b 
 Trong các lệnh trên thì INPUT , LOAD , PRINT , ADD là các 
 mã lệnh còn a , b là địa_chỉ . Để máy thực_hiện được một chương 
 trình viết bằng hợp ngữ thì chương_trình đó phải được dịch sang 
 ngôn_ngữ_máy . Công_cụ thực_hiện việc dịch đó được gọi_là 
 Assembler . 
 Ngôn_ngữ cấp cao ( High level language ) : Ra_đời và phát_triển 
 nhằm phản_ánh cách_thức người lập_trình nghĩ và làm . Rất gần 
 với ngôn_ngữ con_người ( Anh ngữ ) nhưng chính_xác_như_ngôn 
 ngữ toán_học . Cùng với sự phát_triển của các thế_hệ máy_tính , 
 ngôn_ngữ lập_trình cấp cao cũng được phát_triển rất đa_dạng và 
 phong_phú , việc lập_trình cho máy_tính vì_thế_mà cũng có nhiều 
 khuynh_hướng khác nhau : lập_trình cấu_trúc , lập_trình hướng đối 
 tượng , lập_trình logic , lập_trình hàm ... Một chương_trình viết bằng 
 ngôn_ngữ cấp cao được gọi là chương_trình nguồn ( source 
 programs ) . Để máy_tính " hiểu " và thực_hiện được các lệnh trong 
 chương_trình nguồn thì phải có một chương_trình dịch để dịch 
 chuơng trình nguồn ( viết bằng ngôn_ngữ cấp cao ) thành dạng 
 chương_trình có khả_năng thực_thi . 
 III. 2 Chương_trình dịch 
 Muốn chuyển từ_chương_trình nguồn sang chương_trình đích phải 
 có chương_trình dịch . Nói_chung các chương_trình dịch hoạt_động 
 theo 1 trong 2 cơ_chế : 
 Thông_dịch ( interpreter ) : Là cách dịch từng lệnh một , dịch tới 
 đâu thực_hiện tới đó . Chẳng_hạn ngôn_ngữ LISP sử_dụng trình 
 thông_dịch .

---

## TRANG 15
Lập_trình căn_bản 
 Biên_dịch ( compiler ) : Dịch toàn_bộ chương_trình nguồn thành 
 chương_trình đích rồi sau đó mới thực_hiện . Các ngôn_ngữ sử 
_dụng trình biên_dịch như Pascal , C. . . 
 Giữa thông_dịch và biên_dịch có khác nhau ở chỗ : Do thông_dịch 
 là vừa dịch vừa thực_thi chương_trình còn biên_dịch là dịch xong 
 toàn_bộ chương_trình rồi mới thực_thi nên chương_trình viết bằng 
 ngôn_ngữ biên_dịch thực_hiện nhanh hơn chương_trình viết bằng 
 ngôn_ngữ thông_dịch . 
 Một_số ngôn_ngữ ở đó chương_trình dịch sử_dụng kết_hợp giữa 
 thông_dịch và biên_dịch chẳng_hạn như Java . Chương_trình nguồn 
 của Java được biên_dịch tạo thành một chương_trình đối_tượng 
 ( một dạng mã trung_gian ) và khi thực_hiện thì từng lệnh trong 
 chương_trình đối_tượng được thông_dịch thành mã máy . 
 III. 3 Kiểu dữ_liệu 
 Các số_liệu lưu_trữ trong máy_tính gọi là dữ_liệu ( data ) . Mỗi đơn 
 vị dữ_liệu thuộc một kiểu dữ_liệu nào đó . 
 Kiểu dữ_liệu là một tập_hợp các giá_trị có cùng một tính_chất và 
 tập_hợp các phép toán thao_tác trên các giá_trị đó . Người_ta chia 
 kiểu dữ_liệu ra làm 2 loại : kiểu dữ_liệu sơ_cấp và kiểu dữ_liệu có 
 cấu_trúc . 
 III. 3.1 Kiểu dữ_liệu sơ_cấp 
 Kiểu dữ_liệu sơ_cấp là kiểu dữ_liệu mà giá_trị của nó là đơn 
 nhất . 
 Thí_dụ : Trong ngôn_ngữ lập_trình C , kiểu int gọi là kiểu sơ 
 cấp vì kiểu này bao_gồm các số_nguyên từ - 32768 đến 32767 và 
 các phép_toán + , - , * , / , % … 
 III. 3.2 Kiểu dữ_liệu có cấu_trúc 
 Kiểu dữ_liệu có cấu_trúc là kiểu dữ_liệu mà các giá_trị của nó 
 là sự kết_hợp của các giá_trị khác . 
 Thí_dụ : Kiểu chuỗi ký_tự trong ngôn_ngữ lập_trình C là một 
 kiểu dữ_liệu có cấu_trúc . 
 Các ngôn_ngữ lập_trình đều có những kiểu dữ_liệu do ngôn_ngữ 
 xây_dựng sẵn , mà ta gọi là các kiểu chuẩn . Chẳng_hạn như kiểu

---

## TRANG 16
Lập_trình căn_bản 
 int , char … trong C ; integer , array … trong Pascal . Ngoài_ra , hầu 
 hết các ngôn_ngữ đều cung_cấp cơ_chế cho phép người lập_trình 
 định_nghĩa kiểu của riêng mình để phục_vụ cho việc viết chương 
 trình . 
 IV. BÀI_TẬP 
 Bằng ngôn_ngữ tự_nhiên và lưu_đồ , anh ( chị ) hãy mô_tả giải_thuật 
 cho các bài_toán sau : 
 1 . Tính diện_tích của 1 tam_giác theo công_thức Hê - rông : 
 S = p * ( p  a ) * ( p  b ) * ( p  c ) 
 Với a , b , c là chiều dài 3 cạnh được nhập từ bàn_phím . 
 p : Nửa chu_vi . 
 2 . Giải phương_trình bậc 2 dạng ax2 + bx + c = 0 với a , b , c là các 
 số sẽ nhập từ bàn_phím . 
 3 . Tính tổng_bình_phương của n số_nguyên có dạng sau : 
 S = a 2 + a 2 + … + a 2 với n và a ( i = 1 . . n ) là các số sẽ 
 1 2 n i 
 nhập từ bàn_phím .

---

## TRANG 17
Lập_trình căn_bản 
 Chương 2 
 TỔNG_QUAN VỀ NGÔN_NGỮ LẬP 
 TRÌNH C 
 Các vấn_đề được trình_bày trong chương này : 
  Lịch_sử của ngôn_ngữ lập_trình C. 
  Các thành_phần của C. 
 I. SƠ_LƯỢC VỀ NGÔN_NGỮ LẬP_TRÌNH C 
 C_là ngôn_ngữ lập_trình cấp cao , được sử_dụng rất phổ_biến để lập 
 trình hệ_thống cùng với Assembler và phát_triển các ứng_dụng . 
 Vào những năm cuối thập_kỷ 60 đầu thập_kỷ 70 của thế_kỷ XX , 
 Dennish_Ritchie ( làm_việc tại phòng thí_nghiệm Bell ) đã phát 
_triển ngôn_ngữ lập_trình C dựa trên ngôn_ngữ BCPL ( do Martin 
 Richards đưa ra vào năm 1967 ) và ngôn_ngữ B ( do Ken 
 Thompson phát_triển từ ngôn_ngữ BCPL vào năm 1970 khi viết 
 hệ điều_hành UNIX đầu_tiên trên máy PDP - 7 ) và được cài_đặt lần 
 đầu_tiên trên hệ điều_hành UNIX của máy DEC PDP - 11 . 
 Năm 1978 , Dennish_Ritchie và B. W_Kernighan đã cho xuất_bản 
 quyển “ Ngôn_ngữ lập_trình C ” và được phổ_biến rộng_rãi đến nay . 
 Lúc ban_đầu , C được thiết_kế nghiệm Bell và nhanh_chóng 
 nhằm lập_trình trong môi hội_nhập vào thế_giới lập 
 trường của hệ điều_hành_trình để rồi các công_ty lập 
 Unix nhằm mục_đích hỗ_trợ trình sử_dụng một_cách rộng 
 cho các công_việc lập_trình rãi . Sau đó , các công_ty_sản 
 phức_tạp . Nhưng về sau , với xuất phần_mềm lần_lượt đưa 
 những nhu_cầu phát_triển ra các phiên_bản hỗ_trợ cho 
 ngày_một tăng của công_việc việc lập_trình bằng ngôn_ngữ 
 lập_trình , C đã vượt qua C và chuẩn ANSI C cũng 
 khuôn_khổ của phòng thí được khai_sinh từ đó . 
 Ngôn_ngữ lập_trình C là một ngôn_ngữ lập_trình hệ_thống rất 
 mạnh và rất “ mềm_dẻo ” , có một thư_viện gồm rất nhiều các hàm

---

## TRANG 18
Lập_trình căn_bản 
 ( function ) đã được tạo sẵn . Người lập_trình có_thể tận_dụng các 
 hàm này để giải_quyết các bài_toán mà không cần phải tạo mới . 
 Hơn thế nữa , ngôn_ngữ C hỗ_trợ rất nhiều phép_toán nên phù_hợp 
 cho việc giải_quyết các bài_toán kỹ_thuật có nhiều công_thức phức 
 tạp . Ngoài_ra , C cũng cho phép người lập_trình_tự định_nghĩa 
 thêm các kiểu dữ_liệu trừu_tượng khác . Tuy_nhiên , điều mà người 
 mới vừa học lập_trình C thường gặp “ rắc_rối ” là “ hơi khó hiểu ” 
 do sự “ mềm_dẻo ” của C. Dù_vậy , C được phổ_biến khá rộng_rãi 
 và đã trở_thành một công_cụ lập_trình khá mạnh , được sử_dụng 
 như là một ngôn_ngữ lập_trình chủ_yếu trong việc xây_dựng 
 những phần_mềm hiện_nay . 
 Ngôn_ngữ C có những đặc_điểm cơ_bản sau : 
  Tính cô_đọng ( compact ) : C chỉ có 32 từ khóa chuẩn và 40 
 toán_tử chuẩn , nhưng hầu_hết đều được biểu_diễn bằng những 
 chuỗi ký_tự ngắn_gọn . 
  Tính cấu_trúc ( structured ) : C có một tập_hợp những chỉ_thị 
 của lập_trình như cấu_trúc lựa_chọn , lặp … Từ đó các chương 
 trình viết bằng C được tổ_chức rõ_ràng , dễ hiểu . 
  Tính tương_thích ( compatible ) : C có bộ tiền xử_lý và một thư 
 viện chuẩn vô_cùng phong_phú nên khi chuyển từ máy_tính này 
 sang máy_tính khác các chương_trình viết bằng C vẫn hoàn 
 toàn tương_thích . 
  Tính mềm_dẻo ( flexible ) : C là một ngôn_ngữ rất uyển_chuyển 
 về cú_pháp , chấp_nhận nhiều cách thể_hiện , có_thể thu gọn_kích 
 thước của các mã lệnh làm chương_trình chạy nhanh hơn . 
  Biên_dịch ( compile ) : C cho phép biên_dịch nhiều tập_tin 
 chương_trình riêng_rẽ thành các tập_tin đối_tượng ( object ) và 
 liên_kết ( link ) các đối_tượng đó lại với nhau thành một chương 
 trình có_thể thực_thi được ( executable ) thống_nhất . 
 II. BỘ CHỮ_VIẾT TRONG C 
 Bộ chữ_viết trong ngôn_ngữ C bao_gồm những ký_tự , ký_hiệu sau : 
 ( phân_biệt chữ in hoa và in thường ) : 
  Các ký_tự hoa A , B , C. . . Z 
  Các ký_tự thường a , b , c ... z .

---

## TRANG 19
Lập_trình căn_bản 
  Các ký số 0 , 1 , 2 . 
  Các ký_hiệu toán_học : + , - , * , / , = , < , > , ( , ) 
  Các ký_hiệu đặc_biệt : : . , ; " ' _ @ # $ ! ^ [ ] { } ... 
  Dấu cách hay khoảng trống . 
 III. CÁC TỪ KHÓA TRONG C 
 Từ khóa là các từ dành riêng ( reserved words ) của C mà người 
 lập_trình có_thể sử_dụng chúng trong chương_trình tùy theo ý 
 nghĩa của từng từ . Dưới đây là bảng liệt_kê các từ khóa_thông 
_dụng của C để bạn_đọc lướt qua cho có khái_niệm , không nhất 
_thiết phải nhớ ngay : 
 break case const continue 
 default do else for 
 goto if return sizeof 
 struct typedef while 
 IV. TÊN VÀ QUY_CÁCH ĐẶT TÊN 
 Một chương_trình nguồn C sử_dụng khá nhiều tên hay còn gọi_là 
 định_danh ( identifier ) như : tên hàm , tên biến , tên hằng … Mọi tên 
 đều phải được khai_báo trước khi sử_dụng . 
 Tên có hai loại là tên chuẩn và tên do người lập_trình đặt . 
  Tên chuẩn là tên do C đặt sẵn như sin , cos , printf ... 
  Tên do người lập_trình_tự đặt để dùng trong chương_trình 
 của mình . Sử_dụng bộ chữ_cái , chữ_số và dấu gạch dưới ( _ ) để 
 đặt tên , nhưng phải tuân_thủ quy_tắc : 
 o Bắt_đầu bằng một chữ_cái hoặc dấu gạch dưới . 
 o Không có khoảng trống ở giữa tên . 
 o Không được trùng với từ khóa . 
 o Không cấm việc đặt tên trùng với tên chuẩn nhưng khi đó 
 ý_nghĩa của tên chuẩn không còn giá_trị nữa . 
 Thí_dụ : Tên do hợp_lệ : Chieu_dai , Chieu_Rong , Chu_Vi . 
 Tên không hợp_lệ : Do_Dai , 12A2 , …

---

## TRANG 20
Lập_trình căn_bản 
 Chú_ý : C_là ngôn_ngữ phân_biệt ký_tự hoa và ký_tự thường , vì_thế 
 pi và Pi là 2 tên khác nhau . 
 V. CHÚ_THÍCH 
 Khi viết chương_trình đôi lúc ta cần phải có vài lời ghi_chú về 1 
 đoạn chương_trình nào đó để dễ nhớ và làm sáng_sủa_chương 
 trình . Để_ý rằng phần nội_dung ghi_chú này phải không thuộc về 
 chương_trình ( khi biên_dịch phần này bị bỏ_qua ) . Phần ghi_chú 
 như_vậy được gọi là chú_thích . Trong ngôn_ngữ lập_trình C , nội 
 dung chú_thích phải được viết trong cặp dấu / * và * / ( nếu chú 
 thích trên nhiều dòng ) , hoặc đặt sau cặp dấu / / ( nếu chú_thích trên 
 1 dòng ) . 
 Thí_dụ : Chương_trình hiển_thị lên màn_hình câu thông_báo 
 ‘ Hello_World ’ . 
 # include < stdio . h > 
 # include < conio . h > 
 main ( ) { 
 / * Xuat chuoi ra man hinh * / 
 printf ( “ Hello_World ” ) ; 
 / / Cho phim bat ky 
 getch ( ) ; 
 } 
 Ý_nghĩa các dòng trong đoạn chương_trình trên : 
 - Các dòng 
 # include < stdio . h > 
 # include < conio . h > 
 cho phép gộp các tập_tin tiêu_đề stdio . h và conio . h 
 vào tập_tin chương_trình nguồn . Tập_tin stdio . h chứa định_nghĩa 
 về các hàm_xuất nhập chuẩn ( chẳng_hạn printf ) . Tập_tin conio . h 
 chứa các hàm_xuất nhập như getch ( ) . 
 # include là chỉ_thị hướng_dẫn dịch của C , chỉ_thị này thông 
 báo cho chương_trình dịch nạp tập_tin tiêu_đề stdio . h ( và conio . h ) 
 vào để dịch . 
 - Khối 
 main ( ) 
 { 
 … 
 }

---

## TRANG 21
Lập_trình căn_bản 
 gọi là thân chương_trình . Phần này bắt_buộc phải có cho 
 mọi chương_trình C. Phần này còn được gọi là hàm main ( ) hoặc 
 là điểm bắt_đầu thực_hiện của 1 chương_trình C. 
 - Dòng printf ( “ Hello_World ” ) ; cho phép hiển_thị_giá_trị 
 của câu Hello World lên màn_hình . 
 - Dòng getch ( ) ; chờ nhận 1 ký_tự từ bàn_phím . Chương_trình 
 sẽ thực_hiện tiếp_tục sau khi một phím bất_kỳ được ấn . 
 Phần nằm trong / * * / hoặc dòng nằm sau / / là chú_thích 
 VI. CÁC KIỂU DỮ_LIỆU SƠ_CẤP CHUẨN TRONG C 
 Các kiểu dữ_liệu sơ_cấp chuẩn trong C có_thể được chia làm 2 
 dạng : kiểu số_nguyên , kiểu số_thực . Phần này chỉ trình_bày miền 
 giá_trị của các kiểu , các phép_toán trên các giá_trị của các kiểu sẽ 
 được trình_bày ở các phần tiếp_theo . 
 VI. 1 . Kiểu số_nguyên 
 Kiểu số_nguyên là một kiểu dữ_liệu mà tập các giá_trị của nó là 
 tập con của tập số_nguyên trong toán_học . Tùy_thuộc vào kích 
 thước lưu_trữ mà kiểu số_nguyên được chia làm 3 loại : 1 byte , 2 
 bytes hay 4 bytes . Ứng với mỗi loại , người_ta còn định_nghĩa sẵn 
 một_số kiểu khác nhau . Tùy_thuộc vào ứng_dụng của chương_trình 
 mà người lập_trình sẽ sử_dụng 1 kiểu thích_hợp . 
 VI. 1.1 . Kiểu số_nguyên 1 byte ( 8 bits )

| STT | Kiểu dữ liệu | Miền giá trị (Domain) |
| --- | --- | --- |
| 1 | char | Từ -128 đến 127 |
| 2 | unsigned char | Từ 0 đến 255 |


Kiểu số_nguyên một byte gồm có 2 kiểu sau : 
 - Kiểu char : các số_nguyên thuộc kiểu char có giá_trị từ - 128 
 đến 127 . 
 - Kiểu unsgined char : các số_nguyên thuộc kiểu unsigned 
 char có giá_trị từ 0 đến 255 .

---

## TRANG 22
Lập_trình căn_bản 
 Chú_ý : Kiểu char còn có_thể được gọi là kiểu ký_tự vì C cho 
 phép kiểu này được sử_dụng như số_nguyên và ký_tự . 
 VI. 1.2 . Kiểu số_nguyên 2 bytes ( 16 bits ) 
 Kiểu số_nguyên 2 bytes gồm có 4 kiểu sau :

| STT | Kiểu dữ liệu | Miền giá trị (Domain) |
| --- | --- | --- |
| 1 | int | Từ -32,768 đến 32,767 |
| 2 | short | Từ -32,768 đến 32,767 |
| 3 | unsigned int | Từ 0 đến 65,535 |
| 4 | unsigned short | Từ 0 đến 65,535 |


VI. 1.3 . Kiểu số_nguyên 4 byte ( 32 bits ) 
 Kiểu số_nguyên 4 bytes hay còn gọi là số_nguyên dài ( long ) 
 gồm có 2 kiểu sau :

| STT | Kiểu dữ liệu | Miền giá trị (Domain) |
| --- | --- | --- |
| 1 | long | Từ -2,147,483,648 đến 2,147,483,647 |
| 2 | unsigned long | Từ 0 đến 4,294,967,295 |


VI. 2 . Kiểu số_thực 
 Kiểu số_thực là một kiểu dữ_liệu mà tập các giá_trị của nó 
 là tập_hợp_con của tập các số_thực trong toán_học . Người_ta định 
 nghĩa sẵn 3 kiểu số_thực với kích_thước , miền giá_trị và độ chính 
 xác ( số chữ_số thập_phân ) khác nhau . Tùy_thuộc vào ứng_dụng 
 của chương_trình mà người lập_trình lựa_chọn 1 kiểu thích_hợp để 
 sử_dụng .

---

## TRANG 23
Lập_trình căn_bản

| STT | Kiểu dữ liệu | Kích thước | Miền giá trị (Domain) |
| --- | --- | --- | --- |
| 1 | float | 4 bytes | Từ 1.2 * 10-38 đến 3.4 * 1038. Độ chính xác khoảng 7 chữ số |
| 2 | double | 8 bytes | Từ 2.2 * 10-308 đến 3.4 * 10308. Độ chính xác khoảng 15 chữ số |
| 3 | long double | 10 bytes | Từ 3.4 *10-4932 đến 3.4 *104932. Độ chính xác khoảng 19 chữ số. |


Ngoài_ra ta còn có kiểu dữ_liệu void , kiểu này mang ý_nghĩa_là 
 kiểu rỗng không chứa giá_trị gì cả . 
 VII. HẰNG 
 Hằng là một đại_lượng mà giá_trị của nó không thay_đổi trong 
 suốt quá_trình thực_hiện chương_trình . Hằng có_thể được đặt tên 
 ( theo quy_tắc đặt tên trong mục IV ) hoặc là một hằng trực_tiếp . 
 Hằng có_thể là một chuỗi ký_tự , một ký_tự , một con_số xác_định . 
 Chúng có_thể được biểu_diễn hay định_dạng ( Format ) với nhiều 
 dạng_thức khác nhau . 
 VII. 2.1 Hằng_số_thực 
 Là một_số_thực thuộc miền giá_trị của một trong 3 kiểu số 
 thực được trình_bày ở trên . Các giá_trị_số_thực được biểu_diễn 
 theo 2 cách sau : 
  Cách 1 : Sử_dụng cách viết thông_thường gồm 2 phần : phần 
 nguyên và phần thập_phân ; mỗi phần phân_cách nhau bởi dấu 
 chấm ( . ) . 
 Thí_dụ : 0.0 ; 123.34 ; - 223.333 ; 3.00 ; - 56.0 
  Cách 2 : Sử_dụng cách viết theo số_mũ hay số khoa_học . 
 Một_số_thực được tách làm 2 phần , cách nhau bằng ký_tự e hay E 
 Phần giá_trị : là một_số_nguyên hay số_thực được viết theo 
 cách 1 . 
 Phần mũ : là một_số_nguyên 
  Giá_trị của số_thực là : Phần giá_trị nhân với 10 mũ 
 phần mũ .

---

## TRANG 24
Lập_trình căn_bản 
 Thí_dụ : 1234.56 e - 3 = 1.23456 ( là số 1234.56 * 10 - 3 ) 
 - 123.45 E4 = - 1234500 ( là - 123.45 * 104 ) 
 VI. 2.2 Hằng_số_nguyên 
 Một hằng_số_nguyên là một_số_nguyên thuộc miền giá_trị của 
 các số_nguyên 1 byte , 2 bytes và 4 bytes . 
  Hằng_số_nguyên hệ thập_phân : là số_nguyên có giá_trị thuộc 
 kiểu số_nguyên 1 byte / 2 bytes / 4 bytes và được viết như cách viết 
 thông_thường trong toán_học ( sử_dụng các ký số từ 0 đến 9 để 
 biểu_diễn một giá_trị nguyên ) . 
 Thí_dụ : 123 ( một trăm hai mươi ba ) , 
 - 242 ( trừ hai trăm bốn mươi hai ) . 
  Hằng_số_nguyên hệ bát phân : là số_nguyên có giá_trị thuộc 
 kiểu số_nguyên 1 byte / 2 bytes / 4 bytes và được biểu_diễn bởi 8 
 chữ_số từ 0 đến 7 , bắt_đầu bằng số 0 . 
 Cách biểu_diễn : 0 < các ký số từ 0 đến 7 > 
 Thí_dụ : 0345 ( số 345 trong hệ bát phân ) 
 - 020 ( số - 20 trong hệ bát phân ) 
 Cách tính giá_trị thập_phân của số bát phân như sau : 
 Số bát phân : 0d d d … d d ( d có giá_trị từ 0 đến 7 ) 
 n n - 1 n - 2 1 0 i 
 n 
 = > Giá_trị thập_phân =  d * 8i 
 i 
 i  0 
 0345 = 229 , 020 = 16

---

## TRANG 25
Lập_trình căn_bản 
  Hằng_số_nguyên hệ thập_lục phân : là số_nguyên có giá_trị 
 thuộc kiểu số_nguyên 1 byte / 2 bytes / 4 bytes và được biểu_diễn 
 bởi 10 chữ_số từ 0 đến 9 và 6 ký_tự A , B , C , D , E , F 
 Ký_tự Giá_trị 
 A 10 
 B 11 
 C 12 
 D 13 
 E 14 
 F 15 
 Cách biểu_diễn : 
 0x < các ký số từ 0 đến 9 và 6 ký_tự từ A đến F > 
 Thí_dụ : 
 0x345 ( số 345 trong hệ 16 ) 
 0x20 ( số 20 trong hệ 16 ) 
 0x2A9 ( số 2A9 trong hệ 16 ) 
 Cách tính giá_trị thập_phân của số thập_lục phân : 
 Số thập_lục phân : 0xd d d … d d 
 n n - 1 n - 2 1 0 
 ( d từ 0 đến 9 hoặc A đến F ) 
 i 
 n 
 = > Giá_trị thập_phân =  d * 16i 
 i 
 i  0 
 Thí_dụ : 0x345 = 827 , 0x20 = 32 , 0x2A9 = 681 
  Hằng_số_nguyên có định trước kiểu : Đôi_khi ta muốn ghi 
 các hằng_số với kiểu được định trước tường_minh , điều này có_thể 
 được thực_hiện bằng cách thêm một ( một_số ) ký_tự vào cuối dãy 
 số . 
 - U ( hoặc u ) : cho kiểu unsigned int 
 - L ( hoặc l ) : cho kiểu long 
 - UL ( hoặc ul ) : cho kiểu unsigned_long 
 Thí_dụ : 
 65000U : hằng_số_nguyên kiểu unsigned int . 
 123456789L : hằng_số_nguyên kiểu long

---

## TRANG 26
Lập_trình căn_bản 
 VI. 2.3 . Hằng ký_tự 
 Hằng ký_tự là một ký_tự riêng_biệt được viết trong cặp dấu 
 nháy đơn ( ‘ ) . 
 Thí_dụ : ‘ a ’ , ‘ A ’ , ‘ 0 ’ , ‘ 9 ’ 
 Mỗi hằng ký_tự được lưu_trữ đúng 1 byte trong bộ_nhớ . 
 Một giá_trị hằng ký_tự là một phần_tử của 1 tập hữu_hạn các 
 ký_tự được sắp thứ_tự . Các máy_tính đều sử_dụng tập các ký_tự 
 như_vậy để trao_đổi thông_tin với nhau qua các thiết_bị xuất_nhập . 
 Có nhiều cách sắp_xếp bộ chữ khác nhau và có một bộ chữ ( bộ 
 mã ) được sử_dụng phổ_biến để trao_đổi thông_tin giữa các thiết_bị , 
 nhất là trên máy_tính . Đó là bộ mã ASCII ( American_Standard 
 Code for Information_Interchange ) . 
 Mỗi ký_tự được mã_hóa đúng bằng 1 byte , vì_thế bảng mã 
 ASCII có_thể mã_hóa tới 256 ký_tự ( 28 ) . Cách_thức mã_hóa được 
 thực_hiện bằng cách gán cho mỗi ký_tự một giá_trị_số thuộc 
 [ 0 ] gọi là mã ASCII của ký_tự đó . 
 Thí_dụ : Ký_tự ‘ A ’ , ‘ B ’ có mã ASCII lần_lượt là 65 , 66 
 Ký_tự ‘ a ’ , ‘ b ’ có mã ASCII lần_lượt là 97 , 98 . 
 Thực_tế chỉ có 128 giá_trị_số đầu_tiên được sử_dụng để mã_hóa 
 các ký_tự thông_thường , 128 giá_trị tiếp_theo ( từ 128 - 255 ) được 
 sử_dụng để mã_hóa cho các ký_tự riêng của 1 số ngôn_ngữ , các ký 
 tự toán_học … 
 Bảng dưới đây là bảng mã ASCII của 128 ký_tự đầu_tiên ( còn 
 được gọi là bảng mã ASCII chuẩn ) :

---

## TRANG 27
Lập_trình căn_bản 
 Chúng_ta có_thể thực_hiện các phép_toán số_học trên 2 ký_tự 
 ( thực_chất là thực_hiện phép_toán trên giá_trị ASCII của chúng ) 
 VI. 2.4 . Hằng chuỗi ký_tự 
 Hằng chuỗi ký_tự là một chuỗi hay một xâu ký_tự được đặt 
 trong cặp dấu nháy kép ( “ ) . 
 Thí_dụ : “ Ngon ngu lap trinh C ” , “ Khoa CNTT - DHCT ” 
 Chú_ý : 
 1 . Một chuỗi không có nội_dung “ ” được gọi là chuỗi rỗng . 
 2 . Khi lưu_trữ trong bộ_nhớ , một chuỗi được kết_thúc bằng 
 ký_tự NULL ( ‘ \ 0 ’ : mã ASCII là 0 ) . 
 3 . Để biểu_diễn ký_tự đặc_biệt bên trong chuỗi ta phải thêm 
 dấu \ phía trước . 
 Thí_dụ : 
 “ I ’ m a student ” phải viết “ I \ ’ m a student ” 
 Một_số ký_tự đặc_biệt

| Ký tự | Giá trị thập lục phân | Ký tự được hiển thị | Ý nghĩa |
| --- | --- | --- | --- |
| \a | 0x07 | BEL | Phát ra tiếng chuông |
| \b | 0x08 | BS | Di chuyển con trỏ sang trái 1 ký tự và xóa ký tự bên trái (backspace) |
| \f | 0x0C | FF | Sang trang |
| \n | 0x0A | LF | Xuống dòng |
| \r | 0x0D | CR | Trở về đầu dòng |
| \t | 0x09 | HT | Tab theo cột (giống gõ phím Tab) |
| \\ | 0x5C | \ | Dấu \ |
| \’ | 0x2C | ‘ | Dấu nháy đơn (‘) |
| \” | 0x22 | “ | Dấu nháy kép (“) |
| \? | 0x3F | ? | Đấu chấm hỏi (?) |
| \0 | 0x00 |  | Ký tự NULL (rỗng) |



---

## TRANG 28
Lập_trình căn_bản 
 VII. BIẾN 
 VII. 1 . Biến 
 Biến là một đại_lượng được người lập_trình định_nghĩa và được 
 đặt tên thông_qua việc khai_báo biến . Biến dùng để lưu_trữ giá_trị 
 dữ_liệu trong quá_trình thực_hiện chương_trình và giá_trị của biến 
 có_thể bị thay_đổi trong quá_trình này . Việc đặt tên biến phải tuân 
 theo quy_tắc đặt tên trong mục IV. 
 Khi khai_báo biến ta phải xác_định kiểu cho nó . Và khi đó , giá_trị 
 của biến phải thuộc miền giá_trị của kiểu . 
 VII. 1.1 . Cú_pháp khai_báo biến : 
 < Kiểu dữ_liệu > Danh_sách các tên biến_cách nhau 
 bởi dấu_phẩy ; 
 Thí_dụ : 
 int a , b , c ; / / Ba biến a , b , c có kiểu int 
 long n ; / / Biến n có kiểu long 
 float nua_chu_vi ; / * Biến_nua_chu_vi 
 có kiểu float * / 
 double dien_tich ; / * Biến dien_tich có 
 kiểu double * / 
 Lưu_ý : Phải có dấu_chấm_phẩy ở cuối phần khai_báo biến . 
 VII. 1.2 . Vị_trí khai_báo biến trong C 
 Trong ngôn_ngữ lập_trình C , ta phải khai_báo biến đúng vị 
 trí . Nếu khai_báo ( đặt các biến ) không đúng vị_trí sẽ dẫn đến 
 những sai_sót ngoài ý_muốn mà người lập_trình không lường 
 trước ( hiệu_ứng lề ) . Về cơ_bản , ta có 2 cách đặt vị_trí của biến 
 như sau : 
 a ) Khai_báo biến ngoài : Các biến này được đặt bên ngoài 
 tất_cả các hàm và nó có tác_dụng hay ảnh_hưởng đến toàn_bộ 
 chương_trình ( còn gọi là biến toàn_cục ) .

---

## TRANG 29
Lập_trình căn_bản 
 Thí_dụ : 
 int i ; / * Bien ben ngoai * / 
 float pi ; / * Bien ben ngoai * / 
 main ( ) 
 { … 
 } 
 b ) Khai_báo biến trong : Các biến được đặt ở bên trong hàm , 
 hay trong một khối lệnh . Các biến này chỉ có tác_dụng hay ảnh 
 hưởng đến hàm hay khối lệnh chứa nó . Vì_thế chúng còn được 
 gọi là các biến cục_bộ của hàm hay khối lệnh . Vị_trí khai_báo của 
 các biến này là ở đầu mỗi khối lệnh . 
 Thí_dụ 1 : 
 # include < stdio . h > 
 # include < conio . h > 
 int bienngoai ; / * khai bao bien ngoai * / 
 main ( ) 
 { 
 int j , i ; / / khai bao bien cuc bo trong ham main 
 i = 1 ; j = 2 ; 
 bienngoai = 3 ; 
 printf ( " \ n Gia7 tri cua i la % d " , i ) ; 
 / * % d : In một_số_nguyên * / 
 printf ( " \ n Gia tri cua j la % d " , j ) ; 
 printf ( " \ n Gia tri cua bienngoai_la 
 % d " , bienngoai ) ; 
 getch ( ) ; 
 } 
 Thí_dụ 2 : 
 # include < stdio . h > 
 # include < conio . h > 
 main ( ) 
 { int i , j ; / * Bien cuc bo * / 
 i = 4 ; j = 5 ; 
 printf ( " \ n Gia tri cua i la % d " , i ) ; 
 printf ( " \ n Gia tri cua j la % d " , j ) ; 
 if ( j > i ) 
 { 
 int hieu = j - i ; / * Bien cuc bo * / 
 printf ( " \ n j tru i la % d " , hieu ) ; 
 } 
 else

---

## TRANG 30
Lập_trình căn_bản 
 { 
 int hieu = i - j ; / * Bien cuc bo * / 
 printf ( " \ n i tru j la % d " , hieu ) ; 
 } 
 getch ( ) ; 
 } 
 VIII. BIỂU_THỨC 
 Biểu_thức là một sự kết_hợp giữa các toán_tử ( operator ) và các 
 toán hạng ( operand ) theo đúng một trật_tự nhất_định . 
 Mỗi toán hạng có_thể là một hằng , một biến , một hàm hoặc một 
 biểu_thức khác . 
 Mỗi biểu_thức có một giá_trị . Giá_trị của 1 biểu_thức có được bằng 
 cách áp_dụng toán_tử lên các toán hạng . 
 Trong một biểu_thức có nhiều toán_tử có cùng độ ưu_tiên thì thứ 
 tự thực_hiện các phép_toán là từ trái sang phải ( quy_tắc kết_hợp 
 trái ) . 
 Trong một biểu_thức có nhiều toán_tử có độ ưu_tiên khác nhau thì 
 toán_tử nào có độ ưu_tiên cao hơn sẽ được thực_hiện trước ( quy 
 tắc ưu_tiên ) . 
 Nếu cần thay_đổi thứ_tự thực_hiện các toán_tử theo 2 quy_tắc trên , 
 ta dùng cặp dấu ngoặc_đơn ( ) để chỉ_định toán_tử nào sẽ được 
 thực_hiện trước . 
 Thí_dụ : Biểu_thức nghiệm của phương_trình bậc hai : 
 ( - b + sqrt ( Delta ) ) / ( 2 * a ) 
 Trong đó 
 - 2 là hằng ; a , b , Delta là biến . 
 - sqrt : hàm tính căn bậc 2 
 - + , * , / , - là các toán_tử 
 - Biểu_thức có sử_dụng các dấu ngoặc_đơn để tăng độ ưu 
 tiên . 
 VIII. 1 Các toán_tử_số_học 
 Các toán_tử 2 ngôi : gồm có + , - , * , / , % .

---

## TRANG 31
Lập_trình căn_bản

| Toán tử | Miền giá trị của toán hạng | Miền giá trị của kết quả | Ý nghĩa |
| --- | --- | --- | --- |
| + | Nguyên, Thực | Nguyên, Thực | Cộng 2 số |
| - | Nguyên, Thực | Nguyên, Thực | Trừ 2 số |
| * | Nguyên, Thực | Nguyên, Thực | Nhân 2 số |
| / | Nguyên | Nguyên | Chia lấy phần nguyên |
| % | Thực | Thực | Chia 2 số, kết quả là một số thực |


Tăng và giảm ( + + & - - ) 
 Đây là 2 toán_tử 1 ngôi để làm tăng ( + + ) hoặc giảm ( - - ) giá 
 trị của biến . 
 Chẳng_hạn : 
 + + x giống như x = x + 1 
 x - - giống như x = x – 1 
 Cả 2 toán_tử tăng và giảm đều có_thể tiền_tố ( đặt trước ) 
 hay hậu_tố ( đặt sau ) toán hạng . Thí_dụ : x = x + 1 có_thể viết 
 x + + ( hay + + x ) 
 Tuy_nhiên giữa tiền_tố và hậu_tố có sự khác_biệt khi sử 
_dụng trong 1 biểu_thức . 
 Đối_với toán_tử + + , cả 2 trường_hợp đều làm tăng_giá_trị 
 của biến . Nhưng + + x sẽ làm tăng_giá_trị của x lên 1 đơn_vị trước 
 khi giá_trị của x được sử_dụng trong khi x + + sẽ sử_dụng giá_trị 
 của x trước , sau đó x mới tăng_giá_trị lên 1 đơn_vị . 
 Thí_dụ : 
 x = 10 
 y = + + x / / y = 11 
 Tuy_nhiên : 
 x = 10 
 y = x + + / / y = 10 
 Tương_tự đối_với toán_tử - - . 
 Thứ_tự ưu_tiên của các toán_tử_số_học : 
 + + - - sau đó là * / % rồi mới đến + -

---

## TRANG 32
Lập_trình căn_bản 
 VIII. 2 Các toán_tử quan_hệ và các toán_tử Logic 
 Trong C , mọi giá_trị khác 0 được xem là đúng còn 0 là sai . 
 Các biểu_thức sử_dụng các toán_tử quan_hệ và Logic gọi là các 
 biểu_thức logic và giá_trị của 1 biểu_thức logic là 1 hoặc 0 . 
 Các toán_tử quan_hệ

| Toán tử | Miền giá trị của toán hạng | Miền giá trị của kết quả | Ý nghĩa |
| --- | --- | --- | --- |
| > | Số, ký tự | 0, 1 | Lớn hơn |
| >= | Số, ký tự | 0, 1 | Lớn hơn hoặc bằng |
| < | Số, ký tự | 0, 1 | Nhỏ hơn |
| <= | Số, ký tự | 0, 1 | Nhỏ hơn hoặc bằng |
| == | Số, ký tự | 0, 1 | Bằng |
| != | Số, ký tự | 0, 1 | Khác |


Các toán_tử logic

| Toán tử | Miền giá trị của toán hạng | Miền giá trị của kết quả | Ý nghĩa |
| --- | --- | --- | --- |
| && | 0, 1 | 0, 1 | AND |
| ||| | 0, 1 | 0, 1 | OR |
| ! | 0, 1 | 0, 1 | NOT |


Bảng chân trị cho các toán_tử Logic :

| p | q | p&&q | p||q | !p |
| --- | --- | --- | --- | --- |
| 0 | 0 | 0 | 0 | 1 |
| 0 | 1 | 0 | 1 | 1 |
| 1 | 0 | 0 | 1 | 0 |
| 1 | 1 | 1 | 1 | 0 |


Các toán_tử quan_hệ và Logic đều có độ ưu_tiên thấp hơn 
 các toán_tử_số_học . Do đó một biểu_thức như : 10 > 1 + 12 sẽ được 
 xem là 10 > ( 1 + 12 ) và kết_quả là sai ( 0 ) . 
 Ta có_thể kết_hợp vài toán_tử lại với nhau thành biểu_thức 
 như sau : 
 10 > 5 & & ! ( 10 < 9 ) | | 3 < = 4 Kết_quả là đúng

---

## TRANG 33
Lập_trình căn_bản 
 Thứ_tự ưu_tiên của các toán_tử quan_hệ và Logic 
 Cao nhất : ! 
 > > = < < = 
 = = ! = 
 & & 
 Thấp nhất : | | 
 VIII. 3 Các toán_tử thao_tác bit 
 Đây là các toán_tử cho phép thao_tác trên từng bit nhị_phân 
 của các toán hạng là các số_nguyên .

| Toán tử | Ý nghĩa |
| --- | --- |
| & | AND theo từng bit |
| | | OR theo từng bit |
| ^ | XOR theo từng bit |
| ~ | Đảo bit |


Thí_dụ : 
 - Với số_nguyên 3 , dạng nhị_phân là : 
 3 = 0000 0000 0000 0011 
 ~ 3 = 1111 1111 1111 1100 
 - 3 & 5 sẽ có kết_quả : 
 0000 0000 0000 0011 3 
 0000 0000 0000 0110 6 
 Kết_quả : 0000 0000 0000 0010 4 
 Bảng chân trị của toán_tử ^ ( XOR )

| p | q | p^q |
| --- | --- | --- |
| 0 | 0 | 0 |
| 0 | 1 | 1 |
| 1 | 0 | 1 |
| 1 | 1 | 0 |



---

## TRANG 34
Lập_trình căn_bản 
 Phép_toán dịch trái và dịch phải : 
 Phép_tính nhân một_số_nguyên với một_số là lũy thừa của 2 
 có_thể thực_hiện nhanh hơn nếu dùng >> ( dịch phải ) hoặc < < 
 ( dịch trái ) . 
 - N < < M : dịch sang trái số_nguyên N đi M bit , tương 
 đương N * 2M . 
 - N >> M : dịch sang phải số_nguyên N đi M bit , tương 
 đương N / 2M . 
 Thí_dụ : 4 < < 3 , kết_quả là 32 ( 4 * 23 ) . 
 VIII. 4 Toán_tử ? cùng với : 
 C có một toán_tử rất mạnh và trong 1 số trường_hợp có_thể 
 dùng để thay_thế cho các câu_lệnh của If - Then - Else . Cú_pháp của 
 việc sử_dụng toán_tử ? là : 
 E1 ? E2 : E3 
 Trong đó E1 , E2 , E3 là các biểu_thức . 
 Ý_nghĩa : Trước_tiên E1 được ước_lượng , nếu đúng E2 được 
 ước_lượng và nó trở_thành giá_trị của biểu_thức ; nếu E1 sai , E2 
 được ước_lượng và trở_thành giá_trị của biểu_thức . 
 Thí_dụ : 
 X = 10 
 Y = X > 9 ? 100 : 200 
 Thì Y được gán giá_trị 100 , nếu X nhỏ hơn 9 thì Y 
 sẽ nhận giá_trị là 200 . Đoạn mã này tương_đương cấu_trúc if 
 như sau : 
 X = 10 
 if ( X < 9 ) Y = 100 
 else Y = 200 
 VIII. 5 Toán_tử con_trỏ & và * 
 Một con_trỏ là địa_chỉ trong bộ_nhớ của một biến . Một biến 
 con_trỏ là một biến được khai_báo riêng để chứa một con_trỏ đến 
 một đối_tượng của kiểu đã chỉ ra nó . Ta sẽ tìm_hiểu kỹ hơn về con

---

## TRANG 35
Lập_trình căn_bản 
 trỏ trong chương về con_trỏ . Phần này chỉ đề_cập ngắn_gọn đến 
 hai toán_tử thường được sử_dụng để thao_tác với các con_trỏ . 
 Toán_tử thứ nhất là & , là một toán_tử trả về địa_chỉ bộ_nhớ của 
 1 biến . 
 Thí_dụ : 
 m = & count 
 Đặt vào biến m địa_chỉ bộ_nhớ của biến count . 
 Chẳng_hạn , biến count ở vị_trí bộ_nhớ 2000 , giả_sử 
 count có giá_trị là 100 . Sau câu_lệnh trên m sẽ nhận giá_trị 
 2000 . 
 Toán_tử thứ hai là * , là một bổ_sung cho & ; đây là một toán_tử 
 trả về giá_trị của biến được cấp_phát tại địa_chỉ theo sau đó . 
 Thí_dụ : 
 q = * m 
 Sẽ đặt giá_trị của count vào q . Bây_giờ q sẽ có_giá 
 trị là 100 vì 100 được lưu_trữ tại địa_chỉ 2000 . 
 VIII. 6 Toán_tử dấu_phẩy , 
 Toán_tử dấu , được sử_dụng để kết_hợp các biểu_thức lại với 
 nhau . Bên trái của toán_tử dấu , luôn được xem là kiểu void . Điều 
 đó có_nghĩa_là biểu_thức bên phải trở_thành giá_trị của tổng_các 
 biểu_thức được phân_cách bởi dấu_phẩy . 
 Thí_dụ : x = ( y = 3 , y + 1 ) ; 
 Trước_hết gán 3 cho y rồi gán 4 cho x . Cặp dấu_ngoặc 
 đơn là cần_thiết vì toán_tử dấu , có độ ưu_tiên thấp hơn toán_tử 
 gán . 
 VIII. 7 Xem các dấu ngoặc_đơn và cặp dấu ngoặc_vuông là toán 
_tử 
 Trong C , cặp dấu ngoặc_đơn là toán_tử và chúng được dùng để 
 tăng độ ưu_tiên của các biểu_thức bên trong nó .

---

## TRANG 36
Lập_trình căn_bản 
 Các cặp dấu ngoặc_vuông thực_hiện thao_tác truy_xuất phần_tử 
 trong mảng ( sẽ được trình_bày rõ_ràng hơn trong chương Mảng ) . 
 VIII. 8 Tổng_kết về độ ưu_tiên

| Cao nhất | () [] |
| --- | --- |
|  | ! ~ ++ -- (Kiểu) * & |
|  | * / % |
|  | + - |
|  | << >> |
|  | < <= > >= |
|  | & |
|  | ^ |
|  | | |
|  | && |
|  | || |
|  | ?: |
|  | = += -= *= /= |
| Thấp nhất | , |


VIII. 9 Phép gán mở_rộng trong C 
 Trong một_số trường_hợp , ta có_thể viết tắt như sau : x + = 10 . 
 Thực_chất của cách viết này là tương_đương với cách viết x = x + 
 10 . 
 Cách viết như trong thí_dụ vừa nêu có_thể thực_hiện trên tất_cả 
 các toán_tử hai ngôi của C. Tổng_quát : 
 ( Biến ) = ( Biến ) ( Toán_tử ) ( Biểu_thức ) 
 có_thể được viết : 
 ( Biến ) ( Toán_tử ) = Biểu_thức ) 
 IX. CẤU_TRÚC CỦA 1 CHƯƠNG_TRÌNH C 
 IX. 1 . Tiền xử_lý và biên_dịch 
 Trong C , việc dịch một tập_tin nguồn được tiến_hành trên hai 
 bước hoàn_toàn độc_lập với nhau :

---

## TRANG 37
Lập_trình căn_bản 
 - Tiền xử_lý . 
 - Biên_dịch . 
 Hai bước này trong phần_lớn thời_gian được nối_tiếp với nhau 
 một_cách tự_động theo cách_thức mà ta có ấn_tượng rằng nó đã 
 được thực_hiện như là một xử_lý duy_nhất . Nói_chung , ta thường 
 nói đến việc tồn_tại của một bộ tiền xử_lý ( preprocessor ) nhằm 
 chỉ rõ chương_trình thực_hiện việc xử_lý trước . Ngược_lại , các 
 thuật_ngữ trình biên_dịch hay sự biên_dịch vẫn còn nhập_nhằng 
 bởi_vì nó chỉ ra khi thì toàn_bộ hai giai_đoạn , khi thì lại là giai 
 đoạn thứ hai . 
 Bước tiền xử_lý tương_ứng với việc cập_nhật trong văn_bản của 
 chương_trình nguồn , chủ_yếu dựa trên việc diễn_giải các mã_lệnh 
 rất đặc_biệt gọi là các chỉ_thị dẫn hướng của bộ tiền xử_lý 
 ( destination directive of preprocessor ) ; các chỉ_thị này được nhận 
 biết bởi chúng bắt_đầu bằng ký_hiệu ( symbol ) # . 
 Hai chỉ_thị quan_trọng nhất là : 
 - Chỉ_thị sự gộp vào các tập_tin nguồn khác : # include 
 - Chỉ_thị việc định_nghĩa các macros hoặc ký_hiệu : # define 
 Chỉ_thị đầu_tiên được sử_dụng trước_hết là nhằm gộp vào 
 nội_dung của các tập_tin cần có ( tập_tin thư_viện ) . Chỉ_thị này 
 thường sử_dụng vì bởi các hàm của thư_viện chuẩn của C được 
 định_nghĩa trong các tập_tin thư_viện ; do đó , muốn sử_dụng các 
 hàm này , tập_tin thư_viện định_nghĩa chúng phải được gộp vào . 
 Thí_dụ : # include < stdio . h > 
 Chỉ_thị thứ hai rất hay được sử_dụng trong các tập_tin thư 
 viện ( header file ) đã được định_nghĩa trước đó và thường được 
 khai_thác bởi các lập_trình_viên trong việc định_nghĩa các ký_hiệu 
 như là : 
 # define NB_COUPS_MAX 100 
 # define SIZE 25

---

## TRANG 38
Lập_trình căn_bản 
 IX. 2 Cấu_trúc một chương_trình C 
 Một chương_trình C bao_gồm các phần như : Các chỉ_thị 
 tiền xử_lý , khai_báo biến ngoài , các hàm tự tạo , chương_trình 
 chính ( hàm main ) . 
 Cấu_trúc có_thể như sau :

|  | Các chỉ thị tiền xử lý (Preprocessor directives) #include <Tên tập tin thư viện> #define …. Thí dụ: #include<stdio.h> #define MAXINT 32767 |
| --- | --- |
| Các chỉ thị tiền xử lý (Preprocessor directives) #include <Tên tập tin thư viện> #define …. Thí dụ: #include<stdio.h> #define MAXINT 32767 | Các chỉ thị tiền xử lý (Preprocessor directives) #include <Tên tập tin thư viện> #define …. Thí dụ: #include<stdio.h> #define MAXINT 32767 |



|  | Định nghĩa kiểu dữ liệu (phần này không bắt buộc): dùng để đặt tên lại cho một kiểu dữ liệu nào đó để gợi nhớ hay đặt 1 kiểu dữ liệu cho riêng mình dựa trên các kiểu dữ liệu đã có. Cú pháp: typedef <Tên kiểu cũ> <Tên kiểu mới>; Thí dụ: typedef int SoNguyen; // Kiểu SoNguyen là kiểu int |
| --- | --- |
| Định nghĩa kiểu dữ liệu (phần này không bắt buộc): dùng để đặt tên lại cho một kiểu dữ liệu nào đó để gợi nhớ hay đặt 1 kiểu dữ liệu cho riêng mình dựa trên các kiểu dữ liệu đã có. Cú pháp: typedef <Tên kiểu cũ> <Tên kiểu mới>; Thí dụ: typedef int SoNguyen; // Kiểu SoNguyen là kiểu int | Định nghĩa kiểu dữ liệu (phần này không bắt buộc): dùng để đặt tên lại cho một kiểu dữ liệu nào đó để gợi nhớ hay đặt 1 kiểu dữ liệu cho riêng mình dựa trên các kiểu dữ liệu đã có. Cú pháp: typedef <Tên kiểu cũ> <Tên kiểu mới>; Thí dụ: typedef int SoNguyen; // Kiểu SoNguyen là kiểu int |



|  | Khai báo các prototype (tên hàm, các tham số, kiểu kết quả trả về,… của các hàm sẽ cài đặt trong phần sau, phần này không bắt buộc): phần này chỉ là các khai báo đầu hàm, không phải là phần định nghĩa hàm. |  |
| --- | --- | --- |
|  | Khai báo các prototype (tên hàm, các tham số, kiểu kết quả trả về,… của các hàm sẽ cài đặt trong phần sau, phần này không bắt buộc): phần này chỉ là các khai báo đầu hàm, không phải là phần định nghĩa hàm. |  |
| Khai báo các biến ngoài (các biến toàn cục) phần này không bắt buộc: phần này khai báo các biến toàn cục được sử dụng trong cả chương trình. | Khai báo các biến ngoài (các biến toàn cục) phần này không bắt buộc: phần này khai báo các biến toàn cục được sử dụng trong cả chương trình. |  |



|  | Chương trình chính (hàm main), phần này bắt buộc phải có main() { Các khai báo cục bộ trong hàm main: Các khai báo này chỉ tồn tại trong hàm mà thôi, có thể là khai báo biến hay khai báo kiểu. Các câu lệnh dùng để định nghĩa hàm main } |
| --- | --- |
| Chương trình chính (hàm main), phần này bắt buộc phải có main() { Các khai báo cục bộ trong hàm main: Các khai báo này chỉ tồn tại trong hàm mà thôi, có thể là khai báo biến hay khai báo kiểu. Các câu lệnh dùng để định nghĩa hàm main } | Chương trình chính (hàm main), phần này bắt buộc phải có main() { Các khai báo cục bộ trong hàm main: Các khai báo này chỉ tồn tại trong hàm mà thôi, có thể là khai báo biến hay khai báo kiểu. Các câu lệnh dùng để định nghĩa hàm main } |



---

## TRANG 39

|  | ập trình căn bản Cài đặt các hàm <Kiểu dữ liệu trả về> <Tên hàm>( các tham số) { Các khai báo cục bộ trong hàm. Các câu lệnh dùng để định nghĩa hàm [return <kết quả trả về>;] } … |
| --- | --- |
| Cài đặt các hàm <Kiểu dữ liệu trả về> <Tên hàm>( các tham số) { Các khai báo cục bộ trong hàm. Các câu lệnh dùng để định nghĩa hàm [return <kết quả trả về>;] } … | Cài đặt các hàm <Kiểu dữ liệu trả về> <Tên hàm>( các tham số) { Các khai báo cục bộ trong hàm. Các câu lệnh dùng để định nghĩa hàm [return <kết quả trả về>;] } … |


Một chương_trình C được thực_thi từ hàm main ( thông_thường là 
 từ câu_lệnh đầu_tiên đến câu_lệnh cuối_cùng ) . 
 IX. 3 Cú_pháp khai_báo các phần bên trong môt chương_trình 
 C 
 IX. 3.1 . Chỉ_thị # include để sử_dụng tập_tin thư_viện 
 Cú_pháp : 
 # include < Tên tập_tin > 
 hay # include “ Tên đường_dẫn ” 
 Thí_dụ : # include < stdio . h > 
 Nếu ta dùng # include ” Tên đường_dẫn ” thì ta phải chỉ rõ 
 tên ở đâu , tên thư_mục và tập_tin thư_viện . 
 Thí_dụ : # include ” C : \ \ TC \ \ math . h ” 
 Trong trường_hợp tập_tin thư_viện nằm trong thư_mục_hiện 
 hành thì ta chỉ cần đưa tên tập_tin thư_viện . Thí_dụ : 
 # include ” math . h ” . 
 IXI. 3.2 . Chỉ_thị # define để định_nghĩa một tên 
 Chỉ_thị này có cú_pháp dạng đơn_giản như sau : 
 # define < Tên > < Giá_trị > 
 Ví_dụ : 
 # define MAXINT 32767

---

## TRANG 40
Lập_trình căn_bản 
 Trong thí_dụ trên , chỉ_thị define định_nghĩa một tên 
 MAXINT ; tên này có_thể sử_dụng như một hằng nguyên có giá_trị 
 là 32767 . 
 IX. 3.3 Khai_báo các prototype của hàm 
 Cú_pháp : 
 < Kiểu kết_quả trả về > Tên hàm ( danh_sách đối_số ) 
 Thí_dụ : 
 long giaithua ( int n ) ; 
 double x_mu_y ( float x , float y ) ; 
 IX. 3.4 . Cấu_trúc của hàm_main 
 Hàm_main chính là chương_trình chính , gồm các khai_báo , các 
 lệnh xử_lý , các lời gọi các hàm khác . 
 Cú_pháp : 
 main ( đối_số ) 
 { 
 Các khai_báo và các câu_lệnh định_nghĩa hàm 
 } 
 Thí_dụ : 
 main ( ) 
 { 
 int a = 5 , b = 6 , c ; 
 float x = 3.5 , y = 4.5 , z ; 
 printf ( “ Day la chuong trinh chinh ” ) ; 
 c = a + b ; 
 printf ( “ \ n % d + % d = % d ” , a , b , c ) ; 
 z = x + y ; 
 printf ( “ \ n % f + % f = % f ” , x , y , z ) ; 
 getch ( ) ; 
 }

---

## TRANG 41
Lập_trình căn_bản 
 Chương 3 
 CÁC CÂU_LỆNH ĐƠN TRONG C 
 Các vấn_đề được trình_bày trong chương này : 
  Khái_niệm và phân_loại câu_lệnh 
  Các lệnh đơn trong C : 
 o Gán . 
 o Nhập dữ_liệu từ bàn_phím . 
 o Hiển_thị kết_quả lên màn_hình . 
 I. CÂU_LỆNH 
 I. 1 . Khái_niệm câu_lệnh 
 Một câu_lệnh ( statement ) xác_định một công_việc mà_chương 
 trình phải thực_hiện để xử_lý dữ_liệu đã được mô_tả và khai_báo . 
 Trong C , các câu_lệnh được ngăn_cách với nhau bởi dấu_chấm 
 phẩy ( ; ) . 
 I. 2 . Phân_loại 
 Có hai loại câu_lệnh : lệnh đơn và lệnh có cấu_trúc . 
 Lệnh đơn là một lệnh không chứa các lệnh khác . Các lệnh 
 đơn gồm : lệnh gán , các câu_lệnh nhập xuất dữ_liệu … 
 Lệnh có cấu_trúc là lệnh trong đó chứa các lệnh khác . 
 Lệnh có cấu_trúc bao_gồm : cấu_trúc điều_kiện rẽ nhánh , cấu_trúc 
 điều_kiện lựa_chọn , cấu_trúc lặp và cấu_trúc lệnh hợp_thành . Lệnh 
 hợp_thành ( khối lệnh ) là một nhóm bao_gồm nhiều khai_báo biến 
 và các lệnh được gom vào trong cặp dấu { } . 
 II. CÁC LỆNH ĐƠN 
 II. 1 . Lệnh_gán 
 Lệnh gán ( assignment statement ) dùng để gán giá_trị của một 
 biểu_thức cho một biến . 
 Cú_pháp : < Tên biến > = < biểu_thức >

---

## TRANG 42
Lập_trình căn_bản 
 Thí_dụ : 
 main ( ) { 
 float Dai , Rong , Chu_Vi ; 
 Dai = 10.0 ; / / Gán 10.0 cho biến Dai 
 Rong = 5.0 ; / / Gán 5.0 cho biến Rong 
 / / Tính chu_vi hình chữ_nhật 
 Chu_Vi = 2 * ( Dai + Rong ) ; 
 } 
 Nguyên_tắc khi dùng lệnh gán là kiểu của biến và kiểu của biểu_thức 
 phải giống nhau , gọi là có sự tương_thích giữa các kiểu dữ_liệu . Chẳng 
 hạn thí_dụ sau cho thấy một sự không tương_thích về kiểu : 
 main ( ) { 
 int x ; 
 x = 10 ; / / Gán hằng_số 10 cho biến x 
 y = “ Xin chao ” ; 
 / / y có kiểu int , còn “ Xin chao ” có kiểu char * 
 } 
 Khi biên_dịch chương_trình này , C sẽ báo lỗi " Cannot 
 convert ‘ char * ’ to ‘ int ’ " tức_là C không_thể tự_động chuyển_đổi 
 kiểu từ char * ( chuỗi ký_tự ) sang int . 
 Tuy_nhiên trong đa_số trường_hợp sự tự_động biến_đổi kiểu 
 để sự tương_thích về kiểu sẽ được thực_hiện . Thí_dụ : 
 main ( ) { 
 float Dai , Rong , Chu_Vi ; 
 Dai = 10 ; / / Gán 10 cho biến Dai 
 Rong = 5 ; / / Gán 5 cho biến Rong 
 / / Tính chu_vi hình chữ_nhật 
 Chu_Vi = 2 * ( Dai + Rong ) ; 
 } 
 Trong thí_dụ trên , 10 là 1 hằng int được gán cho biến Dai 
 kiểu float ( tương_tự 5 được gán cho Rong ) . Ở đây có một sự 
 chuyển_đổi kiểu tự_động từ int sang float để cuối_cùng biến Dai 
 ( Rong ) lưu những giá_trị là các số float .

---

## TRANG 43
Lập_trình căn_bản 
 Trong nhiều trường_hợp để tạo ra sự tương_thích về kiểu , 
 ta phải sử_dụng đến cách_thức chuyển_đổi kiểu một cách tường 
 minh . Cú_pháp của phép_toán này như sau : 
 ( Tên kiểu ) < Biểu_thức > 
  Ý_nghĩa : Chuyển_đổi kiểu của < Biểu_thức > 
 thành kiểu mới < Tên kiểu > . Chẳng_hạn như : 
 float f ; 
 f = ( float ) 10 / 4 ; / / f lúc này là 2.5 
 Chú_ý : 
 - Khi một biểu_thức được gán cho một biến thì giá_trị của 
 nó sẽ thay_thế giá_trị cũ mà biến đã lưu_giữ trước đó . 
 - Trong câu_lệnh gán , dấu = là một toán_tử ; do đó nó có_thể 
 được sử_dụng là một thành_phần của biểu_thức . Trong trường_hợp 
 này giá_trị của biểu_thức gán chính là giá_trị của biến . 
 Thí_dụ : 
 int x , y ; 
 y = ( x = 3 , x + 1 ) ; / / y lúc này là 4 
 - Ta có_thể gán trị cho biến lúc biến được khai_báo theo 
 cách_thức sau : 
 < Tên kiểu > < Tên biến > = < Biểu_thức > ; 
 Thí_dụ : float Dai = 10.0 , Rong = 5.0 ; 
 II. 2 . Nhập giá_trị từ bàn_phím cho biến ( hàm scanf ( ) ) 
 Thực_chất đây là việc đọc dữ_liệu từ bàn_phím và gán cho các 
 biến trong chương_trình khi chương_trình thực_thi . Để thực_hiện 
 được việc này , ngôn_ngữ C hỗ_trợ hàm scanf được định_nghĩa 
 trong thư_viện stdio . h . 
 Cú_pháp : 
 scanf ( “ Chuỗi định_dạng ” , Địa_chỉ của các biến ) ; 
 Giải_thích : 
 - Chuỗi định_dạng : dùng để quy_định kiểu dữ_liệu , cách 
 biểu_diễn , độ rộng , số chữ_số thập_phân ... Bảng dưới đây là một 
 số định_dạng khi nhập biến thuộc kiểu số_nguyên , số_thực , ký 
 tự , … :

---

## TRANG 44
Lập_trình căn_bản

| Định dạng |  | Ý nghĩa |
| --- | --- | --- |
| %[số ký số]d |  | Nhập số nguyên có tối đa <số ký số> |
| %[số ký số] f |  | Nhập số thực có tối đa <số ký số> tính cả dấu chấm |
| %c |  | Nhập một ký tự |
| Thí dụ: |  |  |
| %d | Nhập số nguyên |  |
| %4d | Nhập số nguyên tối đa 4 ký số, nếu nhập nhiều hơn 4 ký số thì chỉ nhận được 4 ký số đầu tiên |  |
| %f | Nhập số thực |  |
| %6f | Nhập số thực tối đa 6 ký số (tính luôn dấu chấm thập phân), nếu nhập nhiều hơn 6 ký số thì chỉ nhận được 6 ký số đầu tiên (hoặc 5 ký số với dấu chấm) |  |


- Địa_chỉ của các biến : là địa_chỉ của các biến mà ta cần 
 nhập giá_trị cho biến đó . Thông_thường các địa_chỉ này được viết 
 như sau : & < tên biến > . 
 Thí_dụ : 
 / / Doc_gia tri cho bien1 co kieu nguyen 
 scanf ( “ % d ” , & bien1 ) ; 
 / / Doc_gia tri cho bien2 co kieu thưc 
 scanf ( “ % f ” , & bien2 ) ; 
 / / Doc_gia tri cho Dai và Rong_co thuc 
 scanf ( “ % f % f ” , & Dai , & Rong ) ; 
 / / bien3 nhận giá_trị là 1 ký_tự 
 scanf ( “ % c ” , & bien3 ) ; 
 Lưu_ý : 
 o Chuỗi định_dạng phải đặt trong cặp dấu nháy kép ( “ ” ) . 
 o Các địa_chỉ biến phải cách nhau bởi dấu_phẩy ( , ) . 
 o Có bao_nhiêu biến thì phải có bấy_nhiêu định_dạng . 
 o Thứ_tự của các định_dạng phải phù_hợp với thứ_tự của các 
 biến . 
 o Để nhập giá_trị ký_tự ( hoặc chuỗi ký_tự ) được chính_xác , 
 hàm fflush ( stdin ) nên được sử_dụng để loại_bỏ các ký_tự 
 còn nằm trong vùng_đệm bàn_phím trước khi sử_dụng hàm 
 scanf ( ) .

---

## TRANG 45
Lập_trình căn_bản 
 o Để nhập vào một chuỗi ký_tự ( không chứa khoảng trắng 
 hay kết_thúc bằng khoảng trắng ) , chúng_ta có_thể khai_báo 
 kiểu mảng ký_tự , sử_dụng định_dạng % s và tên biến thay 
 cho địa_chỉ biến . 
 o Để đọc vào một chuỗi ký_tự có chứa khoảng trắng ( kết 
 thúc bằng phím Enter ) thì phải dùng hàm gets ( ) . 
 Ví_dụ : 
 int biennguyen ; 
 float bienthuc ; 
 char bienchar ; 
 char chuoi1 [ 20 ] , chuoi2 [ 20 ] ; 
 Nhập giá_trị cho các biến : 
 scanf ( “ % 3d ” , & biennguyen ) ; 
 Nếu ta nhập 1234455 thì giá_trị của biennguyen là 3 ký_số 
 đầu_tiên ( 123 ) . Các ký số còn lại sẽ còn nằm lại trong vùng_đệm . 
 scanf ( “ % 5f ” , & bienthuc ) ; 
 Nếu ta nhập 123.446 thì giá_trị của bienthuc là 123.4 , các 
 ký số còn lại sẽ còn nằm trong vùng_đệm . 
 scanf ( “ % 2d % 5f ” , & biennguyen , & bienthuc ) ; 
 Nếu ta nhập liên_tiếp 2 số cách nhau bởi khoảng trắng như 
 sau : 1223 3.142325 
 - 2 ký số đầu_tiên ( 12 ) sẽ được đọc vào cho biennguyen . 
 - 2 ký số tiếp_theo trước khoảng trắng ( 23 ) sẽ được đọc 
 vào cho bienthuc . 
 scanf ( “ % 2d % 5f % c ” , & biennguyen , & bienthuc , 
 & bienchar ) ; 
 Nếu ta nhập liên_tiếp 2 số cách nhau bởi khoảng trắng như 
 sau : 12345 3.142325 : 
 - 2 ký số đầu_tiên ( 12 ) sẽ được đọc vào cho biennguyen . 
 - 3 ký số tiếp_theo trước khoảng trắng ( 345 ) sẽ được đọc 
 vào cho bienthuc . 
 - Khoảng trắng sẽ được đọc cho bienchar .

---

## TRANG 46
Lập_trình căn_bản 
 Nếu ta chỉ nhập 1 số gồm nhiều ký số như sau : 
 123456789 : 
 - 2 ký số đầu_tiên ( 12 ) sẽ được đọc vào cho biennguyen . 
 - 5 ký số tiếp_theo ( 34567 ) sẽ được đọc vào cho bienthuc . 
 - bienchar sẽ có giá_trị là ký số tiếp_theo ‘ 8 ’ . 
 scanf ( “ % s ” , chuoi1 ) ; 
 hoặc scanf ( “ % s ” , chuoi2 ) ; 
 Nếu ta nhập chuỗi như sau : Nguyen_Van_Linh  thì giá_trị 
 của biến chuoi1 hay chuoi2 chỉ là Nguyen . 
 scanf ( “ % s % s ” , chuoi1 , chuoi2 ) ; 
 Nếu ta nhập chuỗi như sau : Duong Van_Hieu  thì giá_trị 
 của biến chuoi1 là Duong và giá_trị của biến chuoi2 là Van . 
 Vì_sao như_vậy ? C sẽ đọc từ đầu đến khi gặp khoảng trắng 
 và gán giá_trị cho biến đầu_tiên , phần còn lại sau khoảng trắng là 
 giá_trị của các biến tiếp_theo . 
 gets ( chuoi1 ) ; 
 Nếu nhập chuỗi : Nguyen_Van_Linh  thì giá_trị của biến 
 chuoi1 là Nguyen_Van_Linh 
 II. 3 . Hiển_thị_giá_trị của biểu_thức lên màn_hình ( hàm printf ) 
 Hàm_printf ( ) ( nằm trong thư_viện stdio . h ) dùng để hiển_thị 
 ( in ) giá_trị của các biểu_thức lên màn_hình . 
 Cú_pháp : 
 printf ( “ Chuỗi định_dạng ” , Các biểu_thức ) ;

---

## TRANG 47
Lập_trình căn_bản 
 Giải_thích : 
 - Chuỗi định_dạng : dùng để quy_định kiểu dữ_liệu , cách 
 biểu_diễn , độ rộng , số chữ_số thập_phân ... Bảng dưới đây là một 
 số định_dạng khi hiển_thị các biểu_thức số_nguyên , số_thực , ký 
 tự , ... :

| Định dạng |  | Ý nghĩa |
| --- | --- | --- |
| %d |  | In số nguyên |
| %[.số chữ số thập phân] f |  | In số thực có <số chữ số thập phân> theo quy tắc làm tròn số. |
| %o |  | In số nguyên hệ bát phân |
| %x |  | In số nguyên hệ thập lục phân |
| %c |  | In một ký tự |
| %s |  | In chuỗi ký tự |
| %e hoặc %E hoặc %g hoặc %G |  | In số nguyên dạng khoa học (nhân 10 mũ x) |
| Thí dụ |  |  |
| %d | In ra số nguyên |  |
| %4d | In số nguyên tối đa 4 ký số, nếu số cần in nhiều hơn 4 ký số thì in hết |  |
| %f | In số thực |  |
| %6f | In số thực tối đa 6 ký số (tính luôn dấu chấm), nếu số cần in nhiều hơn 6 ký số thì in hết |  |
| %.3f | In số thực có 3 số lẻ, nếu số cần in có nhiều hơn 3 số lẻ thì làm tròn. |  |


- Các biểu_thức : là các biểu_thức mà chúng_ta cần hiển_thị 
 giá_trị của nó lên màn_hình , mỗi biểu_thức phân_cách nhau bởi 
 dấu_phẩy ( , ) . 
 Thí_dụ : 
 include < stdio . h > 
 main ( ) { 
 int bien_nguyen = 1234 , i = 65 ; 
 float bien_thuc = 123.456703 ; 
 printf ( “ Gia tri nguyen cua bien nguyen 
 = % d \ n ” , bien_nguyen ) ;

---

## TRANG 48
Lập_trình căn_bản 
 printf ( “ Gia tri thuc cua bien thuc 
 = % f \ n ” , bien_thuc ) ; 
 printf ( “ Truoc khi lam tron = % f \ n 
 Sau khi lam tron = % . 2f ” , 
 bien_thuc , bien_thuc ) ; 
 } 
 Kết_quả in ra màn_hình_như sau : 
 Nếu ta thêm vào dòng sau trong chương_trình : 
 printf ( “ \ n Ky_tu co ma ASCII % d la % c ” , i , i ) ; 
 Kết_quả ta nhận được thêm : 
 printf ( “ So nguyen la % d \ n 
 So thuc la % f ” , i , ( float ) i ) ; 
 printf ( “ \ n So thuc la % f \ n 
 So nguyen la % d ” , bien_thuc , ( int ) bien_thuc ) ; 
 printf ( “ \ n Viet_binh thuong = % f \ n 
 Viet kieu khoa hoc = % e ” , bien_thuc , bien_thuc ) ; 
 Kết_quả in ra màn_hình : 
 Lưu_ý : Đối_với các ký_tự điều_khiển , ta không_thể sử_dụng cách 
 viết thông_thường để hiển_thị chúng . 
 Ký_tự điều_khiển là các ký_tự dùng để điều_khiển các thao 
 tác xuất , nhập dữ_liệu .

---

## TRANG 49
Lập_trình căn_bản 
 Một_số ký_tự điều_khiển :

| Ký tự điều khiển | Giá trị thập lục phân | Ký tự được hiển thị | Ý nghĩa |
| --- | --- | --- | --- |
| \a | 0x07 | BEL | Phát ra tiếng chuông |
| \b | 0x08 | BS | Di chuyển con trỏ sang trái 1 ký tự và xóa ký tự bên trái (backspace) |
| \f | 0x0C | FF | Sang trang |
| \n | 0x0A | LF | Xuống dòng |
| \r | 0x0D | CR | Trở về đầu dòng |
| \t | 0x09 | HT | Tab theo cột (giống gõ phím Tab) |
| \\ | 0x5C | \ | Dấu \ |
| \’ | 0x2C | ‘ | Dấu nháy đơn (‘) |
| \” | 0x22 | “ | Dấu nháy kép (“) |
| \? | 0x3F | ? | Đấu chấm hỏi (?) |
| \ddd | ddd | Ký tự có mã ACSII trong hệ bát phân là số ddd |  |
| \xHHH | 0xHHH | Ký tự có mã ACSII trong hệ thập lục phân là HHH |  |


Thí_dụ : 
 # include < stdio . h > 
 # include < conio . h > 
 main ( ) { 
 printf ( " \ n Tieng Beep \ a " ) ; 
 printf ( " \ n Doi con tro sang trai 1 ky tu \ b " ) ; 
 printf ( " \ n Dau Tab \ tva dau backslash \ \ " ) ; 
 printf ( " \ n Dau nhay don \ ' 
 va dau nhay kep \ " " ) ; 
 printf ( " \ n Dau_cham hoi \ ? " ) ; 
 printf ( " \ n Ky_tu co ma bat phan 101 
 la \ 101 " ) ; 
 printf ( " \ n Ky_tu co ma thap luc phan 41 
 la \ x041 " ) ; 
 printf ( " \ n Dong_hien tai , xin go enter " ) ; 
 getch ( ) ; 
 printf ( " \ rVe dau dong " ) ; 
 getch ( ) ; 
 }

---

## TRANG 50
Lập_trình căn_bản 
 Kết_quả trước khi gõ phím Enter : 
 Kết_quả sau khi gõ phím Enter : 
 III. MỘT THÍ_DỤ 
 Viết chương_trình cho phép nhận từ bàn_phím 2 số_thực biểu_diễn 
 cho chiều dài và chiều rộng của 1 hình chữ_nhật . Tính chu_vi và 
 diện_tích của hình chữ_nhật đó và hiển_thị kết_quả lên màn_hình . 
 Với yêu_cầu của chương_trình này thì đầu_vào và đầu_ra của 
 chương_trình là : 
 Đầu_vào : 2 số_thực chiều dài và chiều rộng . 
 Đầu_ra : chu_vi và diện_tích của hình chữ_nhật . 
 Chương_trình sau giải_quyết được vấn_đề trên : 
 # include < stdio . h > 
 # include < conio . h > 
 main ( ) 
 { 
 float Dai , Rong , Chu_Vi , Dien_Tich ; 
 / / 1 . Nhập chiều dài và chiều rộng 
 printf ( " Chieu dai : " ) ; scanf ( " % f " , & Dai ) ; 
 printf ( " Chieu rong : " ) ; scanf ( " % f " , & Rong ) ;

---

## TRANG 51
Lập_trình căn_bản 
 / / 2 . Tính chu_vi và diện_tích hình chữ_nhật 
 Chu_Vi = 2 * ( Dai + Rong ) ; 
 Dien_Tich = Dai * Rong ; 
 / / 3 . Hiển_thị kết_quả 
 printf ( " Chu_vi la % . 3f \ n 
 Dien tich la % . 3f " , Chu_Vi , Dien_Tich ) ; 
 getch ( ) ; 
 } 
 IV. BÀI_TẬP 
 1 . Viết chương_trình in lên màn_hình một thiệp mời dự sinh_nhật 
 có dạng : 
 * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * 
 THIEP MOI 
 Thân mời bạn : Nguyễn_Mạnh_Hùng 
 Tới dự lễ sinh_nhật của mình 
 Vào lúc 19h ngày 12 / 10 / 2009 
 Tại 05 / 42 Trần_Phú - Cần_Thơ 
 Rất mong được đón_tiếp ! 
 Hồ_Thu_Hương 
 * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * 
 2 . Viết chương_trình nhập vào bán_kính r của một hình_tròn . Tính 
 chu_vi và diện_tích của hình_tròn theo công_thức : 
 Chu_vi CV = 2 * Pi * r 
 Diện_tích S = Pi * r * r 
 In các kết_quả lên màn_hình

---

## TRANG 52
Lập_trình căn_bản 
 3 . Viết chương_trình nhập vào độ dài 3 cạnh a , b , c của một tam 
 giác . Tính chu_vi và diện_tích của tam_giác theo công_thức : 
 Chu_vi CV = a + b + c 
 Diện_tích S = sqrt ( p * ( p - a ) * ( p - b ) * ( p - c ) ) 
 Trong đó : p = CV / 2 
 In các kết_quả lên màn_hình 
 4 . Viết chương_trình tính log x với a , x là các số_thực nhập vào từ 
 a 
 bàn_phím với giả_thiết x > 0 , a > 0 , a ! = 1 . ( dùng log x = lnx / lna ) 
 a 
 5 . Viết chương_trình nhập vào tọa_độ của hai điểm ( x1 , y1 ) và 
 ( x2 , y2 ) 
 a ) Tính hệ_số góc của đường_thẳng đi qua hai điểm đó theo 
 công_thức : 
 Hệ_số góc = ( y2 - y1 ) / ( x2 - x1 ) 
 b ) Tính khoảng_cách giữa hai điểm theo công_thức : 
 Khoảng_cách =  y  y  2   x  x  2 
 2 1 2 1 
 6 . Viết chương_trình nhập vào một ký_tự : 
 a ) In ra mã Ascii của ký_tự đó . 
 b ) In ra ký_tự kế_tiếp của nó . 
 7 . Viết chương_trình nhập vào các giá_trị điện_trở R1 , R2 , R3 của 
 một_mạch điện : 
 1 1 1 1 
 Tính tổng_trở theo công_thức :    
 R R R_R 
 1 2 3 
 8 . Viết chương_trình nhập vào điểm ba môn Toán , Lý , Hóa của 
 một học_sinh . In ra điểm trung_bình của học_sinh đó với hai số_lẻ 
 thập_phân . 
 9 . Viết chương_trình nhập vào ngày , tháng , năm . In ra ngày_tháng 
 năm theo dạng dd / mm / yy . ( dd : ngày , mm : tháng , yy : năm . Thí 
 dụ : 20 / 11 / 99 ) 
 10 . Viết chương_trình đảo_ngược một_số_nguyên dương có đúng 3 
 chữ_số .

---

## TRANG 53
Lập_trình căn_bản 
 Chương 4 
 CÁC LỆNH CÓ CẤU_TRÚC 
 Chương này trình_bày về các câu_lệnh có cấu_trúc trong C. 
 Nội_dung chính của chương này gồm : 
  Khối lệnh trong C. 
  Cấu_trúc rẽ nhánh . 
  Cấu_trúc lựa_chọn . 
  Cấu_trúc vòng_lặp 
  . Các câu_lệnh “ đặc_biệt ” . 
 I. KHỐI LỆNH 
 Một dãy các khai_báo cùng với các câu_lệnh nằm trong cặp 
 dấu ngoặc móc { và } được gọi là một khối lệnh . 
 Thí_dụ 1 : 
 { 
 char ten [ 30 ] ; 
 printf ( “ \ n Nhap vao ten cua ban : ” ) ; 
 scanf ( “ % s ” , ten ) ; 
 printf ( “ \ n Chao_Ban % s ” , ten ) ; 
 } 
 Thí_dụ 2 : 
 # include < stdio . h > 
 # include < conio . h > 
 main ( ) 
 { / * đây là đầu khối * / 
 char ten [ 50 ] ; 
 printf ( " Xin cho biet ten cua ban ! " ) ; 
 scanf ( " % s " , ten ) ; 
 getch ( ) ; 
 } / * đây là cuối khối * /

---

## TRANG 54
Lập_trình căn_bản 
 Một khối lệnh có_thể chứa bên trong nó nhiều khối lệnh 
 khác gọi là khối lệnh lồng nhau . Sự lồng nhau của các khối lệnh 
 là không hạn_chế . 
 Minh_họa : 
 { 
 … lệnh ; 
 { 
 … lệnh ; 
 { 
 … lệnh ; 
 } 
 … lệnh ; 
 } 
 … lệnh ; 
 } 
 Lưu_ý về phạm_vi tác_động của biến trong khối lệnh 
 lồng nhau : 
 - Trong các khối lệnh khác nhau hay các khối lệnh lồng 
 nhau có_thể khai_báo các biến cùng tên . 
 Thí_dụ 1 : 
 { 
 … lệnh ; 
 { 
 int a , b ; / * biến a , b trong khối lệnh thứ nhất * / 
 … lệnh ; 
 } 
 … lệnh ; 
 { 
 int a , b ; / * biến a , b trong khối lệnh thứ hai * / 
 … lệnh ; 
 } 
 }

---

## TRANG 55
Lập_trình căn_bản 
 Thí_dụ 2 : 
 { 
 int a , b ; / * biến a , b trong khối lệnh “ bên ngoài ” * / 
 … lệnh ; 
 { 
 int a , b ; / * biến a , b bên trong khối lệnh con * / 
 } 
 } 
 - Nếu một biến được khai_báo bên ngoài khối lệnh và 
 không trùng tên với biến bên trong khối lệnh thì nó cũng được sử 
_dụng bên trong khối lệnh . 
 - Một khối lệnh con có_thể sử_dụng các biến bên ngoài , các 
 lệnh bên ngoài không_thể sử_dụng các biến bên trong khối lệnh 
 con . 
 Thí_dụ : 
 { 
 int a , b , c ; 
 … lệnh ; 
 { 
 int c , d ; 
 … lệnh ; 
 } 
 } 
 II. CẤU_TRÚC RẼ NHÁNH 
 Cấu_trúc rẽ nhánh là một cấu_trúc được dùng rất phổ_biến 
 trong các ngôn_ngữ lập_trình nói_chung . Cấu_trúc này thể_hiện 
 suy_nghĩ dạng nếu … thì của con_người . Cấu_trúc rẽ nhánh có 
 hai dạng : dạng không đầy_đủ và dạng đầy_đủ .

---

## TRANG 56
Lập_trình căn_bản 
 II. 1 . Dạng không đầy_đủ 
 Cú_pháp : 
 if ( < Biểu_thức điều_kiện > ) 
 < Công_việc > 
 Lưu_đồ cú_pháp : 
 Giải_thích : 
 < Công_việc > được thể_hiện bằng 1 câu_lệnh 
 hay 1 khối lệnh . 
 Đầu_tiên Điều_kiện được kiểm_tra . 
 Nếu điều_kiện đúng ( ! = 0 ) thì thực_hiện câu 
 lệnh hoặc khối lệnh ( Công_việc ) liền sau 
 điều_kiện . 
 Nếu điều_kiện sai thì bỏ_qua lệnh hoặc khối 
 lệnh liền sau điều_kiện ( những lệnh và khối 
 lệnh sau đó vẫn được thực_hiện bình_thường 
 vì nó không phụ_thuộc vào điều_kiện sau if ) . 
 Thí_dụ 1 : Nhập vào một_số_thực a từ bàn_phím . In ra màn 
 hình kết_quả nghịch_đảo của a khi a  0 . 
 # include < stdio . h > 
 # include < conio . h > 
 main ( ) { 
 float a ; 
 printf ( " Nhap a = " ) ; scanf ( " % f " , & a ) ; 
 if ( a ! = 0 ) 
 printf ( " Nghich dao cua % f la % f " , a , 1 / a ) ; 
 getch ( ) ; 
 } 
 Giải_thích : 
 - Nếu giá_trị nhập vào a  0 thì câu_lệnh printf ( " Nghich 
 dao cua % f la % f " , a , 1 / a ) được thực_hiện , ngược_lại câu_lệnh 
 này không được thực_hiện . 
 - Lệnh getch ( ) luôn_luôn được thực_hiện vì nó không phải 
 là “ lệnh liền sau ” điều_kiện if .

---

## TRANG 57
Lập_trình căn_bản 
 Thí_dụ 2 : Nhập vào giá_trị của 2 số a và b từ bàn_phím , nếu 
 a lớn hơn b thì in ra thông_báo “ Gia_trị của a lớn hơn giá_trị của 
 b ” , sau đó hiển_thị_giá_trị cụ_thể của 2 số lên màn_hình . 
 # include < stdio . h > 
 # include < conio . h > 
 main ( ) { 
 int a , b ; 
 printf ( " Nhap vao gia tri cua 2 so a , b ! " ) ; 
 scanf ( " % d % d " , & a , & b ) ; 
 if ( a > b ) { 
 printf ( " \ n Gia tri cua a lon hon 
 gia tri cua b " ) ; 
 printf ( " \ n a = % d , b = % d " , a , b ) ; 
 } 
 getch ( ) ; 
 } 
 Giải_thích : 
 Nếu ta nhập vào giá_trị của a lớn hơn giá_trị của b thì khối 
 lệnh : 
 { 
 printf ( " \ n Gia tri cua a lon hon 
 gia tri cua b " ) ; 
 printf ( " \ n a = % d , b = % d " , a , b ) ; 
 } 
 sẽ được thực_hiện , ngược_lại khối lệnh này không được 
 thực_hiện . 
 II. 2 . Dạng đầy_đủ 
 Cú_pháp : 
 if ( < Biểu_thức điều_kiện > ) 
 < Công_việc 1 > 
 else 
 < Công_việc 2 >

---

## TRANG 58
Lập_trình căn_bản 
 Lưu_đồ cú_pháp : 
 Giải_thích : 
 Công_việc 1 , công_việc 2 được_thể 
 hiện là 1 câu_lệnh hay 1 khối lệnh . 
 Đầu_tiên Biểu_thức điều_kiện được 
 kiểm_tra trước . 
 Nếu điều_kiện đúng thì thực_hiện 
 công_việc 1 . 
 Nếu điều_kiện sai thì thực_hiện công 
 việc 2 . 
 Các lệnh phía sau công_việc 2 không 
 phụ_thuộc vào điều_kiện . 
 Thí_dụ 1 : Viết chương_trình nhập vào một_số_thực a từ bàn 
 phím . In ra màn_hình kết_quả nghịch_đảo của a khi a  0 , khi a = 0 
 in ra thông_báo “ Khong the tim duoc nghich dao cua a ” 
 # include < stdio . h > 
 # include < conio . h > 
 main ( ) { 
 float a ; 
 printf ( " Nhap a = " ) ; scanf ( " % f " , & a ) ; 
 if ( a ! = 0 ) 
 printf ( " Nghich dao cua % f la % f " , a , 1 / a ) ; 
 else 
 printf ( “ Khong the tim duoc nghich dao 
 cua a ” ) ; 
 getch ( ) ; 
 } 
 Giải_thích : 
 - Nếu ta nhập vào giá_trị a  0 thì câu_lệnh 
 printf ( " Nghich dao cua % f la % f " , a , 1 / a ) được thực_hiện , 
 ngược_lại câu_lệnh printf ( “ Khong the tim duoc nghich 
 dao cua a ” ) được thực_hiện . 
 - Lệnh getch ( ) luôn_luôn được thực_hiện .

---

## TRANG 59
Lập_trình căn_bản 
 Thí_dụ 2 : Viết chương_trình cho phép nhập vào giá_trị của 
 2 số a và b từ bàn_phím . nếu a lớn hơn b thì in ra thông_báo “ a_lon 
 hon b ” và hiển_thị_giá_trị của 2 số lên màn_hình , ngược_lại thì in 
 ra màn_hình câu thông_báo “ a nho hon hoặc bang b ” và hiển_thị 
 giá_trị của 2 số lên màn_hình . 
 # include < stdio . h > 
 # include < conio . h > 
 main ( ) { 
 int a , b ; 
 printf ( " Nhap vao gia tri cua 2 so a va b ! " ) ; 
 scanf ( " % d % d " , & a , & b ) ; 
 if ( a > b ) { 
 printf ( " \ n a lon hon b ” ) ; 
 printf ( " \ n a = % d b = % d " , a , b ) ; 
 } 
 else { 
 printf ( " \ n a nho hon hoac bang b " ) ; 
 printf ( " \ n a = % d b = % d " , a , b ) ; 
 } 
 printf ( " \ n Thuc hien xong lenh if " ) ; 
 getch ( ) ; 
 } 
 Giải_thích : 
 - Nếu ta nhập vào 40 30  thì kết_quả hiển_thị trên màn 
 hình là 
 a lon hon b 
 a = 40 b = 30 
 Thuc hien xong lenh if 
 - Còn nếu ta nhập 40 50  thì kết_quả hiển_thị trên màn 
 hình là 
 a nho hon hoac bang b 
 a = 40 b = 50 
 Thuc hien xong lenh if

---

## TRANG 60
Lập_trình căn_bản 
 Thí_dụ 3 : Viết chương_trình nhập vào một_số_nguyên 
 dương là tháng trong năm . Hiển_thị và số ngày của tháng đó lên 
 màn_hình . 
 Gợi_ý : - Tháng có 31 ngày : 1 , 3 , 5 , 7 , 8 , 10 , 12 
 - Tháng có 30 ngày : 4 , 6 , 9 , 10 
 - Tháng có 28 hoặc 29 ngày : 2 
 # include < stdio . h > 
 # include < conio . h > 
 main ( ) { 
 int thg ; 
 printf ( " Nhap vao thang trong nam ! " ) ; 
 scanf ( " % d " , & thg ) ; 
 if ( thg = = 1 | | thg = = 3 | | thg = = 5 | | thg = = 7 | | thg = = 8 
 | | thg = = 10 | | thg = = 12 ) 
 printf ( " \ n Thang % d co 31 ngay " , thg ) ; 
 else if ( thg = = 4 | | thg = = 6 | | thg = = 9 | | thg = = 11 ) 
 printf ( " \ n Thang % d co 30 ngay " , thg ) ; 
 else if ( thg = = 2 ) 
 printf ( " \ n Thang % d co 28 hoac 
 29 ngay " , thg ) ; 
 else printf ( " Khong co thang % d " , thg ) ; 
 printf ( " \ n Thuc hien xong lenh if " ) ; 
 getch ( ) ; 
 } 
 Giải_thích : 
 - Nếu ta nhập vào một trong các số 1 , 3 , 5 , 7 , 8 , 10 , 12 thì 
 kết_quả xuất_hiện trên màn_hình sẽ là : 
 Thang < số > co 31 ngay 
 Thuc hien xong lenh if 
 - Nếu chúng_ta nhập vào một trong các số 4 , 6 , 9 , 11 thì 
 kết_quả xuất_hiện trên màn_hình sẽ là 
 Thang < số > co 30 ngay 
 Thuc hien xong lenh if

---

## TRANG 61
Lập_trình căn_bản 
 - Nếu ta nhập vào số 2 thì kết_quả xuất_hiện trên màn_hình 
 sẽ là 
 Thang 2 co 28 hoac 29 ngay 
 Thuc hien xong lenh if 
 - Nếu ta nhập vào số nhỏ hơn 0 hoặc lớn hơn 12 thì kết 
 quả xuất_hiện trên màn_hình sẽ là 
 Khong co thang < số > 
 Thuc hien xong lenh if 
 Trong đó < số > là con_số mà chúng_ta đã nhập vào . 
 Lưu_ý : 
 - Ta có_thể sử_dụng các câu_lệnh if … else lồng nhau . Trong 
 trường_hợp if … else lồng nhau thì else sẽ kết_hợp với if gần nhất 
 chưa có else . 
 - Trong trường_hợp câu_lệnh if “ bên trong ” không có else 
 thì phải viết nó trong cặp dấu { } ( coi như là khối lệnh ) để tránh 
 sự kết_hợp else if sai . 
 Thí_dụ 1 : 
 if ( so1 > 0 ) 
 if ( so2 > so3 ) 
 a = so2 ; 
 else / * else của if ( so2 > so3 ) * / 
 a = so3 ; 
 Thí_dụ 2 : 
 if ( so1 > 0 ) 
 { 
 if ( so2 > so3 ) / * lệnh if này không 
 có else * / 
 a = so2 ; 
 } 
 else / * else của if ( so1 > 0 ) * / 
 a = so3 ;

---

## TRANG 62
Lập_trình căn_bản 
 III. CẤU_TRÚC LỰA_CHỌN 
 Cấu_trúc lựa_chọn cho phép lựa_chọn một trong nhiều trường 
 hợp . Trong C , đó là câu_lệnh switch . 
 Cú_pháp : 
 switch ( < Biến > ) 
 { 
 case giá_trị 1 : 
 Khối lệnh thực_hiện công_việc 1 ; 
 break ; 
 … 
 case giá_trị n : 
 Khối lệnh thực_hiện công_việc n ; 
 break ; 
 [ default : 
 Khối lệnh thực_hiện công_việc mặc_định ; 
 } 
 Giải_thích : 
 - Trước_tiên Biến được ước_lượng giá_trị . 
 - Nếu giá_trị của biểu_thức bằng giá_trị 1 thì thực_hiện 
 công_việc 1 rồi thoát . 
 - Nếu giá_trị của biểu_thức khác giá_trị 1 thì so_sánh với 
 giá_trị 2 , nếu bằng giá_trị 2 thì thực_hiện công_việc 2 rồi thoát . 
 - Cứ như thế , so_sánh tới giá_trị n . 
 - Nếu tất_cả các phép so_sánh trên đều sai thì thực_hiện 
 công_việc mặc_định của trường_hợp default . 
 Lưu_ý : 
 - Biểu_thức trong switch ( ) phải có kết_quả là giá_trị kiểu số 
 nguyên ( int , char , long , … ) . 
 - Các giá_trị sau case cũng phải là kiểu số_nguyên . 
 - Không bắt_buộc phải có default .

---

## TRANG 63
Lập_trình căn_bản 
 Thí_dụ 1 : Nhập vào một_số_nguyên , chia số_nguyên này 
 cho 2 lấy phần dư . Kiểm_tra nếu phần dư bằng 0 thì in ra_thông 
 báo “ số_chẵn ” , nếu số_dư bằng 1 thì in thông_báo “ số_lẻ ” . 
 # include < stdio . h > 
 # include < conio . h > 
 main ( ) { 
 int songuyen , phandu ; 
 printf ( " \ n Nhap vao so nguyen " ) ; 
 scanf ( " % d " , & songuyen ) ; 
 phandu = ( songuyen % 2 ) ; 
 switch ( phandu ) { 
 case 0 : 
 printf ( " % d la so chan " , songuyen ) ; 
 break ; 
 case 1 : 
 printf ( " % d la so_le " , songuyen ) ; 
 break ; 
 } 
 getch ( ) ; 
 } 
 Thí_dụ 2 : Nhập vào 2 số_thực và 1 phép_toán . 
 - Nếu phép_toán là ‘ + ’ , ‘ - ‘ , ‘ * ’ thì in ra kết qua là tổng , 
 hiệu , tích của 2 số . 
 - Nếu phép_toán là ‘ / ’ thì kiểm_tra xem số thứ 2 có khác 
 không hay không ? Nếu khác không thì in ra thương của chúng , 
 ngược_lại thì in ra thông_báo “ khong chia cho 0 ” . 
 # include < stdio . h > 
 # include < conio . h > 
 main ( ) { 
 float a , b ; 
 char pt ; 
 printf ( " Nhap a = " ) ; scanf ( " % f " , & a ) ; 
 printf ( " Nhap b = " ) ; scanf ( " % f " , & b ) ; 
 fflush ( stdin ) ; 
 printf ( " Phep toan = " ) ; scanf ( " % c " , & pt ) ; 
 switch ( pt ) {

---

## TRANG 64
Lập_trình căn_bản 
 case ' + ' : 
 printf ( " % f + % f = % f " , a , b , a + b ) ; 
 break ; 
 case ' - ' : 
 printf ( " % f - % f = % f " , a , b , a - b ) ; 
 break ; 
 case ' * ' : 
 printf ( " % f * % f = % f " , a , b , a * b ) ; 
 break ; 
 case ' / ' : 
 if ( b = = 0 ) printf ( " Khong chia dc " ) ; 
 else printf ( " % f / % f = % f " , 
 a , b , a / b ) ; 
 break ; 
 default : 
 printf ( " Khong co phep toan % c " , pt ) ; 
 } 
 getch ( ) ; 
 } 
 Trong cấu_trúc lựa_chọn switch … case , từ khóa break là 
 không bắt_buộc . Tuy_nhiên , nếu không có từ khóa break ở cuối 
 mỗi case ; khi biến trong phần switch bằng với 1 giá_trị nào đó , 
 phần công_việc sau case tương_ứng được thực_hiện , sau đó các 
 phần công_việc sau case kế_tiếp cũng được thực_hiện . 
 Thí_dụ 3 : Yêu_cầu người thực_hiện chương_trình nhập vào 
 một_số_nguyên dương là tháng trong năm và in ra số ngày của 
 tháng đó . 
 - Tháng có 31 ngày : 1 , 3 , 5 , 7 , 8 , 10 , 12 
 - Tháng có 30 ngày : 4 , 6 , 9 , 10 
 - Tháng có 28 hoặc 29 ngày : 2 
 - Nếu nhập vào số < 1 hoặc > 12 thì in ra câu thông_báo 
 “ không có tháng này “ .

---

## TRANG 65
Lập_trình căn_bản 
 # include < stdio . h > 
 # include < conio . h > 
 main ( ) { 
 int thang ; 
 printf ( " \ n Nhap vao thang trong nam " ) ; 
 scanf ( " % d " , & thang ) ; 
 switch ( thang ) { 
 case 1 : 
 case 3 : 
 case 5 : 
 case 7 : 
 case 8 : 
 case 10 : 
 case 12 : 
 printf ( " \ n Thang % d co 31 ngay " , thang ) ; 
 break ; 
 case 4 : 
 case 6 : 
 case 9 : 
 case 11 : 
 printf ( " \ n Thang % d co 30 ngay " , thang ) ; 
 break ; 
 case 2 : 
 printf ( " \ Thang 2 co 28 hoac 29 ngay " ) ; 
 break ; 
 default : 
 printf ( " \ n Khong co thang % d " , thang ) ; 
 break ; 
 } 
 getch ( ) ; 
 }

---

## TRANG 66
Lập_trình căn_bản 
 IV. VÒNG_LẶP 
 Cấu_trúc vòng lặp cho phép lặp lại nhiều lần 1 công_việc 
 ( được thể_hiện bằng 1 câu_lệnh hay 1 khối lệnh ) nào đó cho đến 
 khi thỏa_mãn 1 điều_kiện cụ_thể . 
 IV. 1 . Vòng_lặp_for 
 Vòng_lặp_này cho phép lặp lại công_việc trong khi điều 
 kiện còn đúng . 
 Cú_pháp : 
 for ( Biểu_thức 1 ; biểu_thức 2 ; biểu_thức 3 ) 
 < Công_việc > 
 Lưu_đồ : 
 Giải_thích : 
 < Công_việc > : được thể_hiện là 1 câu_lệnh hay 1 khối lệnh . 
 Thứ_tự thực_hiện của câu_lệnh for như sau : 
 Bước 1 : Tính giá_trị của biểu_thức 1 . 
 Bước 2 : Tính giá_trị của biểu_thức 2 .

---

## TRANG 67
Lập_trình căn_bản 
 - Nếu giá_trị của biểu_thức 2 là sai ( = 0 ) : thoát khỏi 
 câu_lệnh for . 
 - Nếu giá_trị của biểu_thức 2 là đúng ( ! = 0 ) : < Công 
 việc > được thực_hiện . 
 Bước 3 : Tính giá_trị của biểu_thức 3 và quay lại bước 2 . 
 Một_số lưu_ý khi sử_dụng câu_lệnh for : 
 - Khi biểu_thức 2 vắng_mặt thì nó được coi là luôn_luôn 
 đúng 
 - Biểu_thức 1 : thông_thường là một_phép gán để khởi tạo 
 giá_trị ban_đầu cho biến điều_kiện . 
 - Biểu_thức 2 : là một biểu_thức kiểm_tra điều_kiện đúng sai 
 để tiếp_tục hay dừng vòng lặp . 
 - Biểu_thức 3 : thông_thường là một_phép gán để thay_đổi 
 giá_trị của biến điều_kiện . 
 - Trong mỗi biểu_thức có_thể có nhiều biểu_thức con . Các 
 biểu_thức con được phân_biệt bởi dấu_phẩy . 
 Thí_dụ 1 : Viết chương_trình in dãy số_nguyên từ 1 đến 10 . 
 # include < stdio . h > 
 # include < conio . h > 
 main ( ) { 
 int i ; 
 printf ( " \ n Day so tu 1 den 10 : " ) ; 
 for ( i = 1 ; i < = 10 ; i + + ) 
 printf ( " % d " , i ) ; 
 getch ( ) ; 
 } 
 Kết_quả chương_trình như sau :

---

## TRANG 68
Lập_trình căn_bản 
 Thí_dụ 2 : Viết chương_trình nhập vào một_số_nguyên n . 
 Tính tổng của các số_nguyên từ 1 đến n . 
 # include < stdio . h > 
 # include < conio . h > 
 main ( ) { 
 unsigned int n , i , tong ; 
 printf ( " Nhap vao so nguyen duong n : " ) ; 
 scanf ( " % u " , & n ) ; 
 tong = 0 ; 
 for ( i = 1 ; i < = n ; i + + ) 
 tong + = i ; 
 printf ( " \ n Tong tu 1 den % u = % u " , n , tong ) ; 
 getch ( ) ; 
 } 
 Nếu chúng_ta nhập vào số 9 thì kết_quả như sau : 
 Thí_dụ 3 : Viết chương_trình in ra trên màn_hình một ma 
 trận có n dòng m cột như sau : 
 1 2 3 4 5 6 7 
 2 3 4 5 6 7 8 
 3 4 5 6 7 8 9 
 … 
 # include < stdio . h > 
 # include < conio . h > 
 main ( ) { 
 unsigned int dong , cot , n , m ; 
 printf ( " \ n Nhap vao so dong va so cot : " ) ; 
 scanf ( " % u % u " , & n , & m ) ; 
 for ( dong = 0 ; dong < n ; dong + + ) { 
 printf ( " \ n " ) ; 
 for ( cot = 1 ; cot < = m ; cot + + ) 
 printf ( " % u \ t " , dong + cot ) ; 
 } 
 getch ( ) ; 
 }

---

## TRANG 69
Lập_trình căn_bản 
 Kết_quả khi nhập 3 dòng 6 cột như sau 
 III. 2 . Vòng_lặp_while 
 Vòng_lặp_while giống như vòng lặp_for , dùng để lặp_lại 
 một công_việc nào đó trong khi điều_kiện còn đúng . 
 Cú_pháp : 
 while ( Biểu_thức điều_kiện ) 
 < Công_việc > 
 Lưu_đồ : 
 Giải_thích : 
 - Công_việc : được thể_hiện bằng 1 
 câu_lệnh hay 1 khối lệnh . 
 - Trước_tiên điều_kiện được kiểm 
 tra . 
 - Nếu điều_kiện sai ( = 0 ) thì thoát 
 khỏi lệnh while . 
 - Nếu điều_kiện đúng ( ! = 0 ) thì 
 thực_hiện công_việc rồi quay lại 
 kiểm_tra điều_kiện tiếp . 
 Lưu_ý : 
 - Lệnh while gồm có biểu_thức điều_kiện và thân vòng_lặp 
 ( khối lệnh thực_hiện công_việc ) 
 - Vòng_lặp dừng lại khi điều_kiện sai . 
 - Khối lệnh thực_hiện công_việc có_thể rỗng , có_thể làm 
 thay_đổi điều_kiện .

---

## TRANG 70
Lập_trình căn_bản 
 Thí_dụ 1 : Viết chương_trình in dãy số_nguyên từ 1 đến 10 . 
 # include < stdio . h > 
 # include < conio . h > 
 main ( ) { 
 int i ; 
 printf ( " \ n Day so tu 1 den 10 : " ) ; 
 i = 1 ; 
 while ( i < = 10 ) { 
 printf ( " % d " , i ) ; 
 i + + ; 
 } 
 getch ( ) ; 
 } 
 Kết_quả chương_trình như sau : 
 Thí_dụ 2 : Viết chương_trình nhập vào một_số_nguyên n . 
 Tính tổng của các số_nguyên từ 1 đến n . 
 # include < stdio . h > 
 # include < conio . h > 
 main ( ) { 
 unsigned int n , i , tong ; 
 printf ( " \ n Nhap vao so nguyen duong n : " ) ; 
 scanf ( " % u " , & n ) ; 
 tong = 0 ; 
 i = 1 ; 
 while ( i < = n ) { 
 tong + = i ; 
 i + + ; 
 } 
 printf ( " \ n Tong tu 1 den % u = % u " , n , tong ) ; 
 getch ( ) ; 
 } 
 Nếu chúng_ta nhập vào số 9 thì kết_quả như sau :

---

## TRANG 71
Lập_trình căn_bản 
 Thí_dụ 3 : Viết chương_trình in ra trên màn_hình một ma 
 trận có n dòng m cột như sau : 
 1 2 3 4 5 6 7 
 2 3 4 5 6 7 8 
 3 4 5 6 7 8 9 
 … 
 # include < stdio . h > 
 # include < conio . h > 
 main ( ) { 
 unsigned int dong , cot , n , m ; 
 printf ( " \ n Nhap vao so dong va so cot : " ) ; 
 scanf ( " % u % u " , & n , & m ) ; 
 dong = 0 ; 
 while ( dong < n ) { 
 printf ( " \ n " ) ; 
 cot = 1 ; 
 while ( cot < = m ) { 
 printf ( " % u \ t " , dong + cot ) ; 
 cot + + ; 
 } 
 dong + + ; 
 } 
 getch ( ) ; 
 } 
 Kết_quả khi nhập 3 dòng 6 cột như sau : 
 IV. 3 . Vòng_lặp_do … while 
 Vòng_lặp_do … while giống như vòng lặp_for , while , dùng 
 để lặp lại một công_việc nào đó trongkhi điều_kiện còn đúng . 
 Cú_pháp : 
 do 
 < Công_việc > 
 while ( < Biểu_thức điều_kiện > )

---

## TRANG 72
Lập_trình căn_bản 
 Lưu_đồ : 
 Giải_thích : 
 - < Công_việc > : được thể_hiện bằng 1 câu 
 lệnh hay 1 khối lệnh . 
 - Trước_tiên công_việc được thực_hiện 
 trước , sau đó mới kiểm_tra điều_kiện mới 
 được kiểm_tra . 
 - Nếu điều_kiện sai thì thoát khỏi lệnh do 
 … while . 
 - Nếu điều_kiện còn đúng thì thực_hiện 
 công_việc rồi quay lại kiểm_tra điều_kiện 
 tiếp ... 
 Lưu_ý : 
 - Lệnh do … while thực_hiện công_việc ít_nhất 1 lần . 
 - Vòng_lặp dừng lại khi điều_kiện sai . 
 - Khối lệnh thực_hiện công_việc có_thể rỗng , có_thể làm 
 thay_đổi điều_kiện . 
 Thí_dụ 1 : Viết chương_trình in dãy số_nguyên từ 1 đến 10 . 
 # include < stdio . h > 
 # include < conio . h > 
 main ( ) { 
 int i ; 
 printf ( " \ n Day so tu 1 den 10 : " ) ; 
 i = 1 ; 
 do { 
 printf ( " % d " , i ) ; 
 i + + ; 
 } while ( i < = 10 ) ; 
 getch ( ) ; 
 } 
 Kết_quả chương_trình như sau :

---

## TRANG 73
Lập_trình căn_bản 
 Thí_dụ 2 : Viết chương_trình nhập vào một_số_nguyên n . 
 Tính tổng của các số_nguyên từ 1 đến n . 
 # include < stdio . h > 
 # include < conio . h > 
 main ( ) { 
 unsigned int n , i , tong ; 
 printf ( " \ n Nhap vao so nguyen duong n : " ) ; 
 scanf ( " % u " , & n ) ; 
 tong = 0 ; 
 i = 1 ; 
 do { 
 tong + = i ; 
 i + + ; 
 } while ( i < = n ) ; 
 printf ( " \ n Tong tu 1 den % u = % u " , n , tong ) ; 
 getch ( ) ; 
 } 
 Nếu chúng_ta nhập vào số 9 thì kết_quả như sau : 
 Thí_dụ 3 : Viết chương_trình in ra trên màn_hình một ma 
 trận có n dòng m cột như sau ( n , m > = 1 ) : 
 1 2 3 4 5 6 7 
 2 3 4 5 6 7 8 
 3 4 5 6 7 8 9 
 … 
 # include < stdio . h > 
 # include < conio . h > 
 main ( ) { 
 unsigned int dong , cot , n , m ; 
 printf ( " \ n Nhap vao so dong va so cot : " ) ; 
 scanf ( " % u % u " , & n , & m ) ; 
 dong = 0 ; 
 do { 
 printf ( " \ n " ) ; 
 cot = 1 ; 
 do {

---

## TRANG 74
Lập_trình căn_bản 
 printf ( " % u \ t " , dong + cot ) ; 
 cot + + ; 
 } while ( cot < = m ) ; 
 dong + + ; 
 } while ( dong < n ) ; 
 getch ( ) ; 
 } 
 Kết_quả khi nhập 3 dòng 6 cột như sau 
 IV. 4 . So_sánh các vòng_lặp 
 Vòng_lặp_for , while : 
 - Kiểm_tra điều_kiện trước thực_hiện công_việc sau nên 
 đoạn lệnh thực_hiện công_việc có_thể không được thực_hiện . 
 - Vòng_lặp kết_thúc khi điều_kiện sai . 
 Vòng_lặp_do … while : 
 - Thực_hiện công_việc trước kiểm_tra điều_kiện sau nên 
 đoạn lệnh thực_hiện công_việc được thực_hiện ít_nhất 1 lần . 
 - Vòng_lặp kết_thúc khi điều_kiện sai . 
 V. CÁC CÂU_LỆNH ĐẶC_BIỆT 
 V. 1 . Lệnh_break 
 Cú_pháp : break ; 
 Dùng để thoát khỏi vòng lặp . Khi gặp câu_lệnh này trong 
 vòng lặp , chương_trình sẽ thoát ra khỏi vòng lặp và chỉ đến câu 
 lệnh liền sau nó . Nếu nhiều vòng lặp thì break sẽ thoát ra khỏi 
 vòng lặp gần nhất . 
 Bên cạnh đó , break còn được dùng trong cấu_trúc lựa_chọn 
 switch .

---

## TRANG 75
Lập_trình căn_bản 
 Thí_dụ : Viết chương_trình nhập một_số_nguyên dương n từ 
 bàn_phím . Kiểm_tra n có là số_nguyên_tố hay không ? 
 # include < stdio . h > 
 # include < conio . h > 
 main ( ) { 
 unsigned int n , i ; 
 printf ( " Nhap n = " ) ; scanf ( " % u " , & n ) ; 
 for ( i = 2 ; i < = n - 1 ; i + + ) 
 if ( n % i = = 0 ) break ; 
 if ( i = = n ) printf ( " % u_la so nguyen to " , n ) ; 
 else printf ( " % u khong la so nguyen to " , n ) ; 
 getch ( ) ; 
 } 
 IV. 2 . Lệnh_continue 
 Cú_pháp : continue ; 
 - Khi gặp lệnh này trong các vòng lặp , chương_trình sẽ bỏ 
 qua phần còn lại trong vòng lặp và tiếp_tục thực_hiện lần lặp_tiếp 
 theo . 
 - Ðối với lệnh for , biểu_thức 3 sẽ được tính trị và quay lại 
 bước 2 . 
 - Ðối với lệnh while , do while ; biểu_thức điều_kiện sẽ được 
 tính và xét xem có_thể tiếp_tục thực_hiện < Công_việc > nữa hay 
 không ? ( dựa vào kết_quả của biểu_thức điều_kiện ) . 
 Thí_dụ : Nhập vào một_số_nguyên dương n từ bàn_phím . 
 Hiển_thị các số_lẻ từ 1 đến n . 
 # include < stdio . h > 
 # include < conio . h > 
 int main ( ) { 
 unsigned int n , i ;

---

## TRANG 76
Lập_trình căn_bản 
 printf ( " Nhap n = " ) ; scanf ( " % u " , & n ) ; 
 for ( i = 1 ; i < = n ; i + + ) { 
 if ( i % 2 = = 0 ) continue ; 
 printf ( " % d " , i ) ; 
 } 
 getch ( ) ; 
 } 
 VI. BÀI_TẬP 
 1 . Viết chương_trình nhập 3 số từ bàn_phím , tìm số lớn nhất trong 
 3 số đó , in kết_quả lên màn_hình . 
 2 . Viết chương_trình tính chu_vi , diện_tích của tam_giác với yêu 
 cầu sau khi nhập 3 số a , b , c phải kiểm_tra lại xem a , b , c có tạo 
 thành một tam_giác không ? Nếu có thì tính chu_vi và diện_tích . 
 Nếu không thì in ra câu " Không tạo thành tam_giác " . 
 3 . Viết chương_trình giải phương_trình bậc nhất ax + b = 0 với a , b 
 nhập từ bàn_phím . 
 4 . Viết chương_trình giải phương_trình bậc hai ax2 + bx + c = 0 với 
 a , b , c nhập từ bàn_phím . 
 5 . Viết chương_trình nhập từ bàn_phím 2 số a , b và một ký_tự ch . 
 Nếu : ch là “ + “ thì thực_hiện phép_tính a + b và in_kết 
 quả lên màn_hình . 
 ch là “ – “ thì thực_hiện phép_tính a - b và in kết_quả 
 lên màn_hình . 
 ch là “ * ” thì thực_hiện phép_tính a * b và in_kết 
 quả lên màn_hình . 
 ch là “ / ” thì thực_hiện phép_tính a / b và in kết_quả 
 lên màn_hình . 
 6 . Viết chương_trình nhập vào 2 số là tháng và năm của một 
 năm . Xét xem tháng đó có bao_nhiêu ngày ? Biết rằng : 
 Nếu tháng là 4 , 6 , 9 , 11 thì số ngày là 30 .

---

## TRANG 77
Lập_trình căn_bản 
 Nếu tháng là 1 , 3 , 5 , 7 , 8 , 10 , 12 thì số ngày là 31 . 
 Nếu tháng là 2 và năm nhuận thì số ngày 29 , ngược_lại thì 
 số ngày là 28 . 
 7 . Viết chương_trình tính tiền điện gồm các khoản sau : 
 Tiền thuê_bao điện_kế : 1000 đồng / tháng . 
 Định_mức sử_dụng điện cho mỗi hộ là 50 Kw 
 Phần định_mức tính giá 450 đồng / Kwh 
 Nếu phần vượt định mức < = 50 Kw tính giá phạt cho phần 
 này là 700 đồng / Kwh . 
 Nếu phần vượt định_mức lớn 50 Kw và nhỏ hơn 100Kw 
 tính giá phạt cho phần này là 910 đồng / Kwh 
 Nếu phần vượt định_mức lớn hơn hay bằng 100 Kw_tính 
 giá phạt cho phần này là 1200 đồng / Kwh . 
 Với : chỉ_số điện_kế cũ và chỉ_số điện_kế mới nhập vào từ 
 bàn_phím . In ra màn_hình số tiền trả trong định_mức , vượt_định 
 mức và tổng của chúng . 
 8 . Kiểm_tra một ký_tự nhập vào thuộc tập_hợp nào trong các tập 
 ký_tự sau : 
 Các ký_tự chữ hoa : ' A ' ... ' Z ' 
 Các ký_tự chữ thường : ' a ' ... ' z ' 
 Các ký_tự chữ_số : ' 0 ' ... ' 9 ' 
 Các ký_tự khác . 
 9 . Hệ thập_lục phân dùng 16 ký số bao_gồm các ký_tự 0 và A , 
 B , C , D , E , F. 
 Các ký số A , B , C , D , E , F có giá_trị tương_ứng trong hệ 
 thập_phân như sau : 
 A 10 
 B 11 
 C 12 
 D 13 
 E 14 
 F 15 
 Hãy viết chương_trình cho nhập vào ký_tự biểu_diễn một 
 ký số của hệ thập_lục phân và cho biết giá_trị thập_phân tương

---

## TRANG 78
Lập_trình căn_bản 
 ứng . Trường_hợp ký_tự nhập vào không thuộc các ký số trên , đưa 
 ra thông_báo lỗi : 
 " Hệ thập_lục phân không dùng ký số này " 
 10 . Viết chương_trình nhập vào ngày_tháng năm của ngày hôm 
 nay , in ra ngày_tháng năm của ngày_mai . 
 11 . Viết chương_trình tính các tổng sau : 
 a ) S = 1 + 2 + ... + n 
 b ) S = 1 / 2 + 2 / 3 + ... + n / ( n + 1 ) 
 c ) S = - 1 + 2 - 3 + 4 - ... + ( - 1 ) nn 
 12 . Viết chương_trình tính P = 2 * 4 * 6 * ... * ( 2n ) , n nhập từ bàn_phím . 
 13 . Viết chương_trình nhập vào một dãy n số , tìm số lớn nhất của 
 dãy và xác_định vị_trí của số lớn nhất trong dãy . 
 14 . Tính giá_trị trung_bình của một dãy số_thực_nhập từ bàn_phím , 
 kết_thúc dãy nhập khi nhập - 1 . 
 15 . Fibonacci là một dãy số được định_nghĩa như sau : 
  1 , nnÕếuu n =  00 h hooặÆc = c n1  1 
 F n =  
 F  F , n  1 
  
 n - 1 n  2 
 Viết chương_trình in ra màn_hình dãy Fibonacci có n_số 
 hạng , n nhập từ bàn_phím khi cho chạy chương_trình . 
 16 . Viết chương_trình đếm số chữ_số của một_số_nguyên n . 
 17 . Viết chương_trình in ra số đảo_ngược của một_số_nguyên n , 
 với n nhập từ bàn_phím . 
 18 . Tìm số_nguyên dương k nhỏ nhất sao cho 2k > n với n là một 
 số_nguyên dương nhập từ bàn_phím . 
 19 . Viết chương_trình mô_phỏng phép chia nguyên DIV 2 số 
 nguyên a và b như sau : để chia nguyên a và b ta tính trị a - b , sau 
 đó lấy hiệu tìm được lại trừ cho b ... tiếp_tục cho đến khi hiệu của 
 nó nhỏ hơn b . Số lần thực_hiện được các phép trừ ở trên sẽ bằng 
 trị của phép chia nguyên . 
 20 . Tìm số_nguyên dương N nhỏ nhất sao cho 
 1 + 1 / 2 + ... + 1 / N > S , với S_nhập từ bàn_phím . 
 21 . Viết chương_trình tìm UCLN và BCNN của hai số a và b theo 
 thuật_toán sau ( Ký_hiệu UCLN của a , b là ( a , b ) còn BCNN là 
 [ a , b ] )

---

## TRANG 79
Lập_trình căn_bản 
 - Nếu a chia hết cho b thì ( a , b ) = b 
 - Nếu a = b * q + r thì ( a , b ) = ( b , r ) 
 - [ a , b ] = a * b / ( b , r ) 
 22 . Viết chương_trình nhập vào một_số_nguyên dương n , in ra 
 màn_hình các số_nguyên_tố p < = n . Số_nguyên p gọi là số_nguyên 
 tố nếu p chỉ chia hết cho một và chia hết cho bản_thân nó . 
 23 . Viết chương_trình tính gần đúng căn bậc hai của một_số 
 dương a theo phương_pháp Newton : 
 Trước_hết cho x = ( 1 + a ) / 2 sau đó là công_thức truy hồi : 
 0 
 x = ( x + a / x ) / 2 
 n + 1 n n 
 x - x 
 Nếu : n + 1 n < e thì căn bậc hai của a bằng 
 x 
 n 
 x 
 Trong đó e là một hằng_số cho trước làm độ chính_xác . 
 24 . Viết chương_trình tính gần đúng căn bậc n của một_số_dương 
 a theo phương_pháp Newton : 
 Trước_hết cho x = a / n sau đó là công_thức truy hồi : 
 0 
 ( n - 1 ) x n + a 
 x = k 
 k + 1 
 nx n - 1 
_k 
 Nếu | a - x n | < e thì x là căn bậc n của a . Trong đó e là một 
 n n 
 hằng_số cho trước làm độ chính_xác . Nếu a < 0 và n chẵn thì 
 không tồn_tại căn .

---

## TRANG 80
Lập_trình căn_bản 
 Chương 5 
 CHƯƠNG_TRÌNH CON ( HÀM ) 
 Chương này trình_bày về chương_trình con ( hàm ) trong C._Các 
 nội_dung chính của chương này như sau : 
  Khái_niệm về hàm ( function ) trong C. 
  Cách xây_dựng và cách sử_dụng hàm trong C. 
 I. KHÁI_NIỆM HÀM 
 Trong những chương_trình lớn , có_thể có những đoạn chương 
 trình viết lặp_đi lặp lại nhiều lần , để tránh rườm_rà và mất thời 
 gian khi viết chương_trình ; người_ta thường phân_chia_chương 
 trình thành nhiều module , mỗi module giải_quyết một công_việc 
 nào đó . Các module như vậy gọi là các chương_trình con . 
 Một tiện_lợi khác của việc sử_dụng chương_trình con là ta có_thể 
 dễ_dàng kiểm_tra xác_định_tính đúng_đắn của nó trước khi ráp_nối 
 vào chương_trình chính và do đó việc xác_định sai_sót để tiến 
 hành hiệu_đính trong chương_trình chính sẽ thuận_lợi hơn . 
 Trong C , chương_trình con được gọi là hàm . Hàm trong C có_thể 
 trả về kết_quả thông_qua tên hàm hay có_thể không trả về kết_quả . 
 Hàm có hai loại : hàm chuẩn và hàm tự định_nghĩa ( hàm_người 
 dùng ) . Trong chương này , ta chú_trọng đến cách định_nghĩa hàm 
 và cách sử_dụng các hàm đã được định_nghĩa . 
 Một hàm khi được định_nghĩa thì có_thể sử_dụng bất_cứ đâu trong 
 chương_trình . Để_ý rằng trong C , một chương_trình bắt_đầu thực 
 thi bằng hàm main . 
 Thí_dụ 1 : Ta có hàm max để tìm số lớn nhất giữa 2 số 
 nguyên a , b như sau : 
 int max ( int a , int b ) { 
 return ( a > b ) ? a : b ; 
 }

---

## TRANG 81
Lập_trình căn_bản 
 Thí_dụ 2 : Ta có chương_trình chính ( hàm main ) dùng để 
 nhập vào 2 số_nguyên a , b và in ra màn_hình số lớn trong 2 số 
 # include < stdio . h > 
 # include < conio . h > 
 int max ( int a , int b ) { 
 return ( a > b ) ? a : b ; 
 } 
 main ( ) { 
 int a , b , c ; 
 printf ( " \ n Nhap vao 3 so a , b , c " ) ; 
 scanf ( " % d % d % d " , & a , & b , & c ) ; 
 printf ( " \ n So lon la % d " , max ( a , max ( b , c ) ) ) ; 
 getch ( ) ; 
 } 
 I. 1 . Hàm_chuẩn 
 Hàm_chuẩn là những hàm đã được định_nghĩa sẵn trong 
 một thư_viện nào đó . Để sử_dụng các hàm thư_viện thì các thư 
 viện định_nghĩa chúng phải được tham_chiếu đến nhờ chỉ_thị tiền 
 xử_lý # include < tên thư_viện . h > 
 Một_số thư_viện thường dùng : 
 1 . stdio . h : Thư_viện chứa các hàm vào / ra chuẩn 
 ( standard input / output ) . Gồm các hàm printf ( ) , scanf ( ) , getc ( ) , 
 putc ( ) , gets ( ) , puts ( ) , fflush ( ) , fopen ( ) , fclose ( ) , fread ( ) , 
 fwrite ( ) , getchar ( ) , putchar ( ) , getw ( ) , putw ( ) … 
 2 . conio . h : Thư_viện chứa các hàm vào ra trong chế_độ 
 DOS ( DOS console ) . Gồm các hàm getch ( ) , getche ( ) , getpass ( ) , 
 cgets ( ) , cputs ( ) , putch ( ) , , … 
 3 . math . h : Thư_viện chứa các hàm tính_toán gồm các hàm 
 abs ( ) , sqrt ( ) , log ( ) . log10 ( ) , sin ( ) , cos ( ) , tan ( ) , acos ( ) , asin ( ) , 
 atan ( ) , pow ( ) , exp ( ) , … 
 4 . malloc . h : Thư_viện chứa các hàm liên_quan đến việc 
 quản_lý bộ_nhớ . Gồm các hàm calloc ( ) , realloc ( ) , malloc ( ) , 
 free ( ) , farmalloc ( ) , farcalloc ( ) , farfree ( ) , …

---

## TRANG 82
Lập_trình căn_bản 
 5 . io . h : Thư_viện chứa các hàm vào ra cấp thấp . Gồm các 
 hàm open ( ) , _open ( ) , read ( ) , _read ( ) , close ( ) , _close ( ) , creat ( ) , 
 _creat ( ) , creatnew ( ) , eof ( ) , filelength ( ) , lock ( ) , … 
 … 
 I. 2 . Hàm người dùng 
 Hàm người dùng là những hàm do người lập_trình_tự tạo ra 
 nhằm đáp_ứng nhu_cầu xử_lý của mình . 
 II. ĐỊNH_NGHĨA VÀ SỬ_DỤNG HÀM 
 II. 1 Định_nghĩa hàm 
 Cấu_trúc của một hàm tự thiết_kế : 
 < kiểu kết_quả > Tên hàm ( [ < kiểu t số > < tham_số > ] 
 [ , < kiểu t số > < tham_số > ] [ … ] ) 
 { 
 [ Khai_báo biến cục_bộ và các câu_lệnh thực_hiện hàm ] 
 [ return [ < Biểu_thức > ] ; ] 
 } 
 Giải_thích : 
 - Kiểu kết_quả : là kiểu dữ_liệu của kết_quả trả về , có_thể là : 
 int , byte , char , float , void … Một hàm có_thể có hoặc không có 
 kết_quả trả về . Trong trường_hợp hàm không có kết_quả trả về ta 
 nên sử_dụng kiểu kết_quả là void . 
 - Kiểu t số : là kiểu dữ_liệu của tham_số . 
 - Tham_số : là tham_số truyền dữ_liệu vào cho hàm , một 
 hàm có_thể có hoặc không có tham_số . Tham_số này gọi là tham 
 số hình_thức , khi gọi hàm chúng_ta phải truyền cho nó các giá 
 trị thực_tế ( tham_số thực_tế ) . Nếu có nhiều tham_số , mỗi tham_số 
 phân_cách nhau dấu_phẩy ( , ) . 
 - Bên trong thân hàm ( phần giới_hạn bởi cặp dấu { } ) là các 
 khai_báo cùng các câu_lệnh xử_lý . Các khai_báo bên trong hàm 
 được gọi là các khai_báo cục_bộ trong hàm và các khai_báo này 
 chỉ tồn_tại bên trong hàm mà thôi .

---

## TRANG 83
Lập_trình căn_bản 
 - Khi định_nghĩa hàm , ta thường sử_dụng câu_lệnh return 
 để trả về kết_quả thông_qua tên hàm . 
 Lệnh return dùng để thoát khỏi một hàm và có 
 thể trả về một giá_trị nào đó . 
 Cú_pháp : 
 return ; / * không trả về giá_trị * / 
 return < biểu_thức > ; / / Trả về giá_trị của biểu_thức 
 return ( < biểu_thức > ) ; / / Trả về giá_trị của biểu_thức 
 Nếu hàm có kết_quả trả về , ta bắt_buộc phải sử_dụng 
 câu_lệnh return để trả về kết_quả cho hàm . 
 Thí_dụ 1 : Viết hàm tìm số lớn giữa 2 số_nguyên a và b 
 int max ( int a , int b ) { 
 return ( a > b ) ? a : b ; 
 } 
 Thí_dụ 2 : Viết hàm tìm ước_chung lớn nhất giữa 2 số 
 nguyên a , b . 
 Cách tìm : đầu_tiên ta giả_sử UCLN của hai số là số nhỏ 
 nhất trong hai số đó . Nếu điều đó không đúng thì ta giảm đi một 
 đơn_vị và cứ giảm như_vậy cho tới khi nào tìm thấy UCLN. 
 usigned int ucln ( unsigned int a , 
 unsigned int b ) { 
 unsgined int u ; 
 if ( a < b ) 
 u = a ; 
 else 
 u = b ; 
 while ( ( a % u ! = 0 ) | | ( b % u ! = 0 ) ) 
 u - - ; 
 return u ; 
 } 
 II. 2 Sử_dụng hàm 
 Một hàm khi định_nghĩa thì chúng vẫn chưa được thực_thi 
 trừ khi ta có một lời gọi đến hàm đó .

---

## TRANG 84
Lập_trình căn_bản 
 Cú_pháp gọi hàm : < Tên hàm > ( [ Danh_sách các tham_số ] ) 
 Thí_dụ : Viết chương_trình cho phép tìm ước_số chung lớn 
 nhất của hai số tự_nhiên . 
 # include < stdio . h > 
 unsigned int ucln ( unsigned int a , 
 unsigned int b ) 
 { 
 unsigned int u ; 
 if ( a < b ) 
 u = a ; 
 else 
 u = b ; 
 while ( ( a % u ! = 0 ) | | ( b % u ! = 0 ) ) 
 u - - ; 
 return u ; 
 } 
 main ( ) { 
 unsigned int A , B , UC ; 
 printf ( “ Nhap a , b : ” ) ; scanf ( “ % u % u ” , & A , & B ) ; 
 UC = ucln ( A , B ) ; 
 printf ( “ Uoc chung lon nhat la : % u ” , UC ) ; 
 } 
 Lưu_ý : 
 - Khi 1 hàm có giá_trị trả về , lời gọi hàm là một biểu_thức , 
 không phải là một câu_lệnh . 
 - Khi 1 hàm không có giá_trị trả về ( void ) , lời gọi hàm 
 được coi tương_đương như 1 câu_lệnh . 
 II. 3 Nguyên_tắc hoạt_động của hàm 
 Trong chương_trình , khi gặp một lời gọi hàm thì hàm_bắt 
 đầu thực_hiện bằng cách chuyển các lệnh thi_hành đến hàm được 
 gọi . Quá_trình_diễn ra như sau :

---

## TRANG 85
Lập_trình căn_bản 
 - Nếu hàm có tham_số , trước_tiên các tham_số sẽ được gán 
 giá_trị thực_tế tương_ứng ( giá_trị thực_tế chính là giá_trị chỉ ra 
 trong lời gọi hàm ) . 
 - Chương_trình sẽ thực_hiện tiếp các câu_lệnh trong thân 
 hàm bắt_đầu_từ lệnh đầu_tiên đến câu_lệnh cuối_cùng . 
 Thí_dụ : Lời gọi hàm ucln ( A , B ) trong hàm main ở trên : 
  A , B chính là các giá_trị thực_tế ( tham_số thực_tế ) . 
  a , b trong định_nghĩa của hàm ucln ( dòng unsigned 
 int ucln ( unsigned int a , unsigned int b ) ) 
 là tham_số hình_thức . 
  Khi có lời gọi hàm ucln ( A , B ) thì a sẽ nhận giá_trị 
 của A , b sẽ nhận giá_trị của B ; hàm ucln sẽ thực_hiện 
 từ đầu đến cuối hàm với các giá_trị a , b đã nhận được . 
 - Khi gặp lệnh return hoặc dấu } cuối_cùng trong thân 
 hàm , chương_trình sẽ thoát khỏi hàm để trở về chương_trình gọi 
 nó và thực_hiện tiếp_tục những câu_lệnh của chương_trình này . 
 III. TRUYỀN THAM_SỐ CHO HÀM 
 Mặc_nhiên , việc truyền tham_số cho hàm trong C là truyền 
 theo giá_trị ; nghĩa_là tham_số hình_thức sẽ chỉ nhận giá_trị là giá 
 trị của tham_số thực_tế tương_ứng . Như_vậy , về cơ_bản tham_số 
 hình_thức và tham_số thực_tế là hoàn_toàn khác nhau ; do đó tham 
 số thực_tế không bị thay_đổi giá_trị sau khi hàm vừa được thực_thi 
 xong . 
 Thí_dụ 1 : Giả_sử ta muốn in ra nhiều dòng , mỗi dòng 50 ký 
 tự nào đó . Để đơn_giản ta viết một hàm , nhiệm_vụ của hàm này là 
 in ra trên một dòng 50 ký_tự nào đó . Hàm này có tên là InKT . 
 # include < stdio . h > 
 # include < conio . h > 
 void InKT ( char ch ) { 
 int i ; 
 for ( i = 1 ; i < = 50 ; i + + ) 
 printf ( “ % c ” , ch ) ; 
 printf ( “ \ n ” ) ; 
 }

---

## TRANG 86
Lập_trình căn_bản 
 main ( ) { 
 char c ; 
 InKT ( ‘ * ’ ) ; / / In ra 50 dau * 
 InKT ( ‘ + ’ ) ; 
 c = ‘ A ’ ; 
 InKT ( c ) ; 
 } 
 Lưu_ý : 
 - Trong hàm InKT ở trên , biến ch gọi là tham_số hình_thức 
 được truyền bằng giá_trị ( gọi là tham trị của hàm ) . Các tham_trị 
 của hàm coi như là một biến cục_bộ trong hàm và chúng được sử 
_dụng như là dữ_liệu đầu_vào của hàm . 
 - Khi chương_trình con được gọi để thi_hành , tham trị được 
 cấp ô nhớ và nhận giá_trị là bản_sao giá_trị của tham_số_thực . Do 
 đó , mặc_dù tham trị cũng là biến , nhưng việc thay_đổi giá_trị của 
 chúng không có ý_nghĩa gì đối_với bên ngoài hàm , không ảnh 
 hưởng đến chương_trình chính , nghĩa_là không làm ảnh_hưởng 
 đến tham_số_thực tương_ứng . 
 Thí_dụ 2 : Xét chương_trình sau đây : 
 # include < stdio . h > 
 # include < conio . h > 
 void hoanvi ( int a , int b ) { 
 int t ; 
 t = a ; / / Hoán_vị giá_trị của 2 biến a , b 
 a = b ; 
 b = t ; 
 printf ( " \ Ben trong ham a = % d , b = % d " , a , b ) ; 
 } 
 main ( ) { 
 int a , b ; 
 printf ( " \ nNhap vao 2 so nguyen a , b : " ) ; 
 scanf ( " % d % d " , & a , & b ) ; 
 printf ( " \ nTruoc khi goi ham hoan_vi a = % d , 
 b = % d " , a , b ) ; 
 hoanvi ( a , b ) ; 
 printf ( " \ nSau khi goi ham hoan_vi a = % d , 
 b = % d " , a , b ) ; 
 getch ( ) ; 
 }

---

## TRANG 87
Lập_trình căn_bản 
 Kết_quả_thực_hiện chương_trình : 
 Tương_tự như thí_dụ trên , các tham_số thực_tế ( a , b trong 
 hàm main ) không thay_đổi giá_trị sau khi gọi hàm hoanvi . 
 IV. HÀM ĐỆ QUY 
 IV. 1 . Định_nghĩa 
 Một hàm được gọi là đệ quy nếu bên trong thân hàm có 
 lệnh gọi đến chính nó . 
 Thí_dụ : Người_ta định_nghĩa giai thừa của một_số_nguyên 
 dương n như sau : 
  1 , nÕu n  0 
 n ! =  
  n * ( n - 1 ) ! , nÕu n  0 
 Với định_nghĩa trên thì hàm đệ quy tính n ! được viết : 
 long giaithua_dequy ( int n ) { 
 if ( n = = 0 ) 
 return 1L ; 
 else 
 return n * giaithua_dequy ( n - 1 ) ; 
 } 
 / * Hàm_tính n ! không đệ quy * / 
 long giaithua_khongdequy ( int n ) { 
 long kq ; 
 int i ; 
 kq = 1L ; 
 for ( i = 1 ; i < = n ; i + + ) 
 kq = kq * i ; 
 return kq ; 
 }

---

## TRANG 88
Lập_trình căn_bản 
 main ( ) { 
 int n ; 
 printf ( " Nhap so n = " ) ; scanf ( " % d " , & n ) ; 
 printf ( " \ nGoi ham de quy : % d ! = % ld " , 
 n , giaithua_dequy ( n ) ) ; 
 printf ( " \ nGoi ham khong de quy : % d ! = % ld " , 
 n , giaithua_khongdequy ( n ) ) ; 
 getch ( ) ; 
 } 
 IV. 2 . Lưu_ý khi viết hàm đệ quy 
 - Hàm_đệ quy phải có 2 phần : 
 o Phần dừng ( hay trường_hợp nguyên_tố ) . Trong thí_dụ 
 ở trên thì trường_hợp n = 0 là trường_hợp nguyên_tố . 
 o Phần_đệ quy : là phần có gọi lại hàm đang được định 
 nghĩa . Trong thí_dụ trên thì phần đệ quy là n > 0 thì n ! = n * ( n - 1 ) ! 
 - Sử_dụng hàm đệ quy trong chương_trình sẽ làm chương 
 trình dễ đọc , dễ hiểu và vấn_đề được nêu bật rõ_ràng hơn . Tuy 
 nhiên trong đa_số trường_hợp thì hàm đệ quy tốn bộ_nhớ nhiều 
 hơn và tốc_độ thực_hiện chương_trình chậm hơn không đệ quy . 
 - Tùy từng bài_toán cụ_thể mà người lập_trình quyết_định 
 có nên dùng đệ quy hay không ( có những trường_hợp không dùng 
 đệ quy thì không giải_quyết được bài_toán ) . 
 V. BÀI_TẬP 
 1 . Viết hàm tìm số lớn nhất trong hai số . Áp_dụng tìm số lớn nhất 
 trong ba số a , b , c với a , b , c nhập từ bàn_phím . 
 2 . Viết hàm tìm UCLN của hai số a và b . Áp_dụng : Nhập vào tử 
 và mẫu_số của một phân_số , kiểm_tra xem phân_số đó đã tối_giản 
 hay chưa . 
 3 . Viết hàm in n ký_tự c trên một dòng . Viết chương_trình cho 
 nhập 5 số_nguyên cho biết số_lượng hàng bán được của mặt_hàng 
 A ở 5 cửa_hàng khác nhau . Dùng hàm trên thể_hiện biểu_đồ so 
 sánh 5 giá_trị đó , mỗi trị dùng một ký_tự riêng .

---

## TRANG 89
Lập_trình căn_bản 
 4 . Viết một hàm tính tổng_các chữ_số của một_số_nguyên . Viết 
 chương_trình nhập vào một_số_nguyên , dùng hàm trên kiểm_tra 
 xem số đó có chia hết cho 3 không . Một_số chia hết cho 3 khi 
 tổng_các chữ_số của nó chia hết cho 3 . 
 5 . Viết chương_trình phân_tích một_số_nguyên dương n thành các 
 thừa_số nguyên_tố . 
 6 . Viết chương_trình tính các tổng sau : 
 a ) S = 1 + x + x2 + x3 + ... + xn 
 b ) S = 1 - x + x2 - x3 + ... ( - 1 ) n xn 
 c ) S = 1 + x / 1 ! + x2 / 2 ! + x3 / 3 ! + ... + xn / n ! 
 Trong đó n là một_số_nguyên dương và x là một_số bất_kỳ 
 được nhập từ bàn_phím khi chạy chương_trình . 
 7 . Tam_giác Pascal là một bảng_số , trong đó hàng thứ 0 bằng 1 , 
 mỗi một_số_hạng của hàng thứ n + 1 là một tổ_hợp chập k của n 
 n ! 
 ( Ck = ) 
 n k ! ( n  k ) ! 
 Tam_giác Pascal có dạng sau : 
 1 ( hàng 0 ) 
 1 1 ( hàng 1 ) 
 1 2 1 ( hàng 2 ) 
 1 3 3 1 
 1 4 6 4 1 
 1 5 10 10 5 1 
 1 6 15 20 15 6 1 ( hàng 6 ) 
 ... ... ... ... ... ... ... ... ... ... ... ... ... ... ... ... ... ... 
 Viết chương_trình hiển_thị lên màn_hình tam_giác Pascal có 
 n hàng ( n nhập vào khi chạy chương_trình ) bằng cách tạo hai hàm 
 tính giai thừa và tính tổ_hợp . 
 8 . Yêu_cầu như câu 7 nhưng dựa công_thức truy hồi của tổ_hợp 
 mà viết thành 1 hàm đệ quy để tính số tổ_hợp chập k của n_phần 
 tử . 
  1 , nÕu k  0 hoÆc k  n 
 Ck   
 n Ck - 1  Ck , nÕu 1  k  n 
  
 n - 1 n - 1

---

## TRANG 90
Lập_trình căn_bản 
 9 . Viết chương_trình in dãy Fibonacci đã nêu trong bằng phương 
 pháp dùng một hàm Fibonacci F có tính đệ quy . 
  1 , nÕu n  0 hoÆc n  1 
 F n =  
 F  F , nÕu n  1 
  
 n - 2 n - 1 
 10 . Bài_toán tháp Hà_Nội : Có một cái tháp gồm n tầng , tầng trên 
 nhỏ hơn tầng dưới ( hình_vẽ ) . Hãy tìm cách chuyển cái tháp này từ 
 vị_trí thứ nhất sang vị_trí thứ hai thông_qua vị_trí trung_gian thứ 
 ba . Biết rằng chỉ được chuyển mỗi lần một tầng và không được 
 để tầng lớn trên tầng nhỏ . 
 VT1 VT2 VT3

---

## TRANG 91
Lập_trình căn_bản 
 Chương 6 
 MẢNG 
 Chương này trình_bày về kiểu dữ_liệu mảng - một kiểu dữ_liệu có 
 cấu_trúc được sử_dụng phổ_biến khi lập_trình . Nội_dung chính của 
 chương này gồm : 
  Khái_niệm về kiểu dữ_liệu mảng cũng như ứng_dụng của 
 kiểu dữ_liệu này . 
  Cách khai_báo biến kiểu mảng và các phép_toán trên các 
 phần_tử của mảng . 
 I. GIỚI_THIỆU KIỂU DỮ_LIỆU MẢNG TRONG C 
 Mảng là một tập_hợp các phần_tử cố_định có cùng một kiểu , gọi_là 
 kiểu phần_tử . Kiểu phần_tử có_thể là có các kiểu bất_kỳ : ký_tự , số , 
 chuỗi ký_tự … ; cũng có khi ta sử_dụng kiểu mảng để làm kiểu 
 phần_tử cho một mảng ( trong trường_hợp này ta gọi là mảng của 
 mảng hay mảng nhiều chiều ) . 
 Ta có_thể chia mảng làm 2 loại : mảng 1 chiều và mảng nhiều 
 chiều . 
 Mảng là kiểu dữ_liệu được sử_dụng rất thường_xuyên . Chẳng_hạn 
 người_ta cần quản_lý một danh_sách họ và tên của khoảng 100 
 sinh_viên trong một lớp . Nhận thấy rằng mỗi họ và tên để lưu_trữ 
 ta cần 1 biến kiểu chuỗi , như vậy 100 họ và tên thì cần khai_báo 
 100 biến kiểu chuỗi . Nếu khai_báo như thế này thì đoạn khai_báo 
 cũng như các thao_tác trên các họ tên sẽ rất dài_dòng và rắc_rối . 
 Vì_thế , kiểu dữ_liệu mảng giúp_ích ta trong trường_hợp này ; chỉ 
 cần khai_báo 1 biến , biến này có_thể coi như là tương_đương với 
 100 biến chuỗi ký_tự ; đó là 1 mảng mà các phần_tử của nó là 
 chuỗi ký_tự . Hoặc 1 thí_dụ khác là việc lưu_trữ các từ khóa của 
 ngôn_ngữ lập_trình C , ta cũng có_thể dùng đến một mảng để lưu 
 trữ chúng .

---

## TRANG 92
Lập_trình căn_bản 
 II. MẢNG 1 CHIỀU 
 Xét dưới góc_độ toán_học , mảng 1 chiều giống như một vector . 
 Mỗi phần_tử của mảng một chiều có giá_trị không phải là một 
 mảng khác . 
 II. 1 . Khai_báo 
 II. 1.1 . Khai_báo mảng với số phần_tử xác_định ( khai báo_tường 
 minh ) 
 Cú_pháp : < Kiểu > < Tên mảng > < [ số phần_tử ] > 
 Ý_nghĩa : 
 - Tên mảng : đây là một tên đặt đúng theo quy_tắc đặt tên 
 của danh biểu . Tên này cũng mang ý_nghĩa_là tên biến mảng . 
 - Số phần_tử : là một hằng_số_nguyên , cho biết số_lượng 
 phần_tử tối_đa trong mảng là bao_nhiêu ( hay nói khác đi_kích 
 thước của mảng là gì ) . 
 - Kiểu : mỗi phần_tử của mảng có dữ_liệu thuộc kiểu gì . 
 - Ở đây , ta khai_báo một biến mảng gồm có số phần_tử 
 phần_tử , phần_tử thứ nhất là tên mảng [ 0 ] , phần_tử cuối_cùng là 
 tên mảng [ số phần_tử - 1 ] 
 Thí_dụ : 
 int a [ 10 ] ; / * Khai_báo biến mảng tên a , phần_tử 
 thứ nhất_là a [ 0 ] , phần_tử cuối_cùng là a [ 9 ] . * / 
  Ta có_thể coi mảng a là một dãy liên_tiếp các 
 phần_tử trong bộ_nhớ như sau : 
 Vị_trí 0 1 2 3 4 5 6 7 8 9

Tên phần_tử a [ 0 ] a [ 1 ] a [ 2 ] a [ 3 ] a [ 4 ] a [ 5 ] a [ 6 ] a [ 7 ] a [ 8 ] a [ 9 ] 
 II. 1.2 . Khai_báo mảng với số phần_tử không xác_định ( khai_báo 
 không tường_minh ) 
 Cú_pháp : < Kiểu > < Tên mảng > < [ ] > 
 Khi khai_báo , không cho biết rõ số phần_tử của mảng , kiểu 
 khai_báo này thường được áp_dụng trong các trường_hợp : vừa

---

## TRANG 93
Lập_trình căn_bản 
 khai_báo vừa gán giá_trị , khai_báo mảng là tham_số hình_thức của 
 hàm . 
 a . Vừa khai_báo vừa gán giá_trị 
 Cú_pháp : 
 < Kiểu > < Tên mảng > [ ] = { Các giá_trị cách nhau 
 bởi dấu_phẩy } ; 
 Nếu vừa khai_báo vừa gán giá_trị thì mặc_nhiên C sẽ hiểu 
 số phần_tử của mảng là số giá_trị mà chúng_ta gán cho mảng 
 trong cặp dấu { } . Chúng_ta có_thể sử_dụng hàm sizeof ( ) để lấy 
 số phần_tử của mảng như sau : 
 Số phần_tử = sizeof ( tên mảng ) / sizeof ( kiểu ) 
 b . Khai_báo mảng là tham_số hình_thức của hàm , trong 
 trường_hợp này ta không cần chỉ_định cụ_thể số phần_tử của 
 mảng . 
 II. 2 Truy_xuất từng phần_tử của mảng 
 Mỗi phần_tử của mảng được truy_xuất thông_qua Tên_biến 
 mảng theo sau là chỉ_số nằm trong cặp dấu ngoặc_vuông [ ] . 
 Chẳng_hạn a [ 0 ] là phần_tử đầu_tiên của mảng a được khai_báo ở 
 trên . Chỉ_số của phần_tử mảng là một biểu_thức mà giá_trị là kiểu 
 số_nguyên . 
 Với cách truy_xuất theo kiểu này , Tên biến mảng [ Chỉ_số ] 
 có_thể coi như là một biến có kiểu dữ_liệu là kiểu được chỉ ra 
 trong khai_báo biến mảng . 
 Thí_dụ 1 : 
 int a [ 10 ] ; 
 - Phần_tử đầu_tiên trong mảng là a [ 0 ] 
 - Phần_tử kế_tiếp trong mảng là a [ 1 ] 
 … 
 - Phần_tử cuối_cùng trong mảng là a [ 9 ] .

---

## TRANG 94
Lập_trình căn_bản 
 Thí_dụ 2 : Vừa khai_báo vừa gán trị cho 1 mảng 1 chiều các 
 số_nguyên . In mảng số_nguyên này lên màn_hình . 
 # include < stdio . h > 
 # include < conio . h > 
 main ( ) { 
 int n , i ; 
 int dayso [ ] = { 66,65,69,68,67,70 } ; 
 n = sizeof ( dayso ) / sizeof ( int ) ; / / số phần_tử 
 printf ( " \ n Noi dung cua mang " ) ; 
 for ( i = 0 ; i < n ; i + + ) 
 printf ( " % d " , dayso [ i ] ) ; 
 } 
 Thí_dụ 3 : Đổi một_số_nguyên dương thập_phân thành số 
 nhị_phân . Việc chuyển_đổi này được thực_hiện bằng cách lấy số 
 đó chia liên_tiếp cho 2 cho tới khi bằng 0 và lấy các số_dư theo 
 chiều ngược_lại để tạo thành số nhị_phân . Trong thí_dụ này , mảng 
 một chiều được sử_dụng để lưu lại các số_dư đó . Chương_trình_cụ 
 thể như sau : 
 # include < conio . h > 
 # include < stdio . h > 
 main ( ) { 
 unsigned int N , Du ; 
 unsigned int NhiPhan [ 20 ] ; 
 int K = 0 , i ; 
 printf ( " Nhap vao so nguyen N = " ) ; 
 scanf ( " % u " , & N ) ; 
 do { 
 Du = N % 2 ; 
 NhiPhan [ K ] = Du ; / / Lưu số_dư vào mảng ở vị_trí K 
 K + + ; / / Tăng K lên để lần kế lưu vào vị_trí_kế 
 N = N / 2 ; 
 } while ( N > 0 ) ; 
 printf ( " Dang nhi phan la : " ) ; 
 for ( i = K - 1 ; i > = 0 ; i - - ) 
 printf ( " % u " , NhiPhan [ i ] ) ; 
 getch ( ) ; 
 }

---

## TRANG 95
Lập_trình căn_bản 
 Thí_dụ 4 : Nhập vào một dãy n số và sắp_xếp các số theo 
 thứ tự tăng . 
 Bài_toán sắp_xếp là 1 bài_toán có ứng_dụng rộng_rãi trong 
 nhiều lĩnh_vực . Để sắp_xếp một dãy n số , có rất nhiều giải_thuật 
 để thực_hiện . Một trong số đó được mô_tả như sau : 
 Đầu_tiên đưa phần_tử thứ nhất so_sánh với các phần_tử còn 
 lại , nếu nó lớn hơn một phần_tử đang so_sánh thì đổi chỗ hai phần 
 tử cho nhau . Sau đó tiếp_tục so_sánh phần_tử thứ hai với các phần 
 tử từ thứ ba trở_đi ... cứ tiếp_tục như_vậy cho đến phần_tử thứ n - 1 . 
 Chương_trình sẽ được chia thành các hàm Nhap ( Nhập các 
 số ) , SapXep ( Sắp_xếp ) và InMang ( In các số ) ; các tham_số hình 
 thức của các hàm này là 1 mảng không chỉ_định rõ số phần_tử_tối 
 đa , nhưng ta cần có thêm số phần_tử thực_tế được sử_dụng của 
 mảng là bao_nhiêu , đây là một giá_trị nguyên . 
 # include < conio . h > 
 # include < stdio . h > 
 void Nhap ( int a [ ] , int N ) { 
 int i ; 
 for ( i = 0 ; i < N ; i + + ) { 
 printf ( " Phan_tu thu % d : " , i ) ; 
 scanf ( " % d " , & a [ i ] ) ; 
 } 
 } 
 void InMang ( int a [ ] , int N ) { 
 int i ; 
 for ( i = 0 ; i < N ; i + + ) 
 printf ( " % d " , a [ i ] ) ; 
 printf ( " \ n " ) ; 
 } 
 void SapXep ( int a [ ] , int N ) { 
 int t , i , j ; 
 for ( i = 0 ; i < N - 1 ; i + + ) 
 for ( j = i + 1 ; j < N ; j + + ) 
 if ( a [ i ] > a [ j ] ) { 
 t = a [ i ] ; 
 a [ i ] = a [ j ] ; 
 a [ j ] = t ; 
 } 
 }

---

## TRANG 96
Lập_trình căn_bản 
 main ( ) { 
 int b [ 20 ] , N ; 
 printf ( " So phan tu thuc te N = " ) ; 
 scanf ( " % d " , & N ) ; 
 Nhap ( b , N ) ; 
 printf ( " Mang vua nhap : " ) ; 
 InMang ( b , N ) ; 
 SapXep ( b , N ) ; / / Gọi hàm sắp_xếp 
 printf ( " Mang sau khi sap xep : " ) ; 
 InMang ( b , N ) ; 
 getch ( ) ; 
 } 
 Kết_quả chạy chương_trình có_thể là : 
 III. MẢNG NHIỀU CHIỀU 
 Mảng nhiều chiều là 1 mảng mà mỗi phần_tử của mảng là 1 mảng 
 khác . 
 Người_ta thường sử_dụng mảng nhiều chiều để lưu các ma_trận , 
 các tọa_độ 2 chiều , 3 chiều … 
 Phần dưới đây là các vấn_đề liên_quan đến mảng 2 chiều ; các 
 mảng 3 , 4 , … chiều thì tương_tự ( chỉ cần tổng_quát_hóa lên ) . 
 III. 1 Khai_báo 
 III. 1.1 . Khai_báo mảng 2 chiều tường_minh 
 Cú_pháp : 
 < Kiểu > < Tên mảng > < [ Số phần_tử chiều 1 ] > < [ Số phần_tử chiều 2 ] >

---

## TRANG 97
Lập_trình căn_bản 
 Thí_dụ : Người_ta cần lưu_trữ thông_tin của một ma_trận 
 gồm các số_thực . Lúc này ta có_thể khai_báo một mảng 2 chiều 
 như sau : 
 float m [ 5 ] [ 6 ] ; / / Khai_báo mảng 2 chiều có 5 * 6 
 phần_tử là số_thực 
 Trong trường_hợp này , ta đã khai_báo cho một ma_trận có 
 tối_đa là 5 dòng , mỗi dòng có tối_đa là 6 cột . Hình_ảnh của ma 
 trận này được thể_hiện trong hình bên dưới : 
 Dòng \ Cột 0 1 2 3 4 5

| m[0][0] | m[0][1] | m[0][2] | m[0][3] | m[0][4] | m[0][5] |
| --- | --- | --- | --- | --- | --- |
| m[1][0] | m[1][1] | m[1][2] | m[1][3] | m[1][4] | m[1][5] |
| m[2][0] | m[2][1] | m[2][2] | m[2][3] | m[2][4] | m[2][5] |
| m[3][0] | m[3][1] | m[3][2] | m[3][3] | m[3][4] | m[3][5] |
| m[4][0] | m[4][1] | m[4][2] | m[4][3] | m[4][4] | m[4][5] |


III. 1.2 . Khai_báo mảng 2 chiều không tường_minh 
 Để khai_báo mảng 2 chiều không tường_minh , ta vẫn phải 
 chỉ ra số phần_tử của chiều thứ hai ( chiều cuối_cùng ) . 
 Cú_pháp : 
 < Kiểu > < Tên mảng > < [ ] > < [ Số phần_tử chiều 2 ] > 
 Cách khai_báo này cũng được áp_dụng trong trường_hợp 
 vừa khai_báo , vừa gán trị hay đặt mảng 2 chiều là tham_số hình 
 thức của hàm . 
 III. 2 Truy_xuất từng phần_tử của mảng 2 chiều 
 Ta có_thể truy_xuất một phần_tử của mảng hai chiều bằng 
 cách viết ra tên mảng theo sau là hai chỉ_số đặt trong hai cặp dấu 
 ngoặc_vuông . Chẳng_hạn ta viết m [ 2 ] [ 3 ] . 
 Với cách truy_xuất theo cách này , Tên mảng [ Chỉ_số 
 1 ] [ Chỉ_số 2 ] có_thể coi là 1 biến có kiểu được chỉ ra trong khai 
 báo biến mảng .

---

## TRANG 98
Lập_trình căn_bản 
 Thí_dụ 1 : Viết chương_trình cho phép nhập 2 ma_trận a , b 
 có m dòng n cột , thực_hiện phép_toán cộng hai ma_trận a , b và in 
 ma_trận kết_quả lên màn_hình . 
 Trong thí_dụ này , ta sẽ sử_dụng hàm để chương_trình ngắn 
 gọn hơn . Trong trường_hợp này , các hàm sau được định_nghĩa : 
 nhập 1 ma_trận từ bàn_phím , hiển_thị ma_trận lên màn_hình , cộng 
 2 ma_trận . 
 # include < conio . h > 
 # include < stdio . h > 
 void Nhap ( float a [ ] [ 10 ] , int M , int N ) { 
 int i , j ; 
 for ( i = 0 ; i < M ; i + + ) 
 for ( j = 0 ; j < N ; j + + ) { 
 printf ( " Phan_tu o dong % d cot % d : " , i , j ) ; 
 scanf ( " % f " , & a [ i ] [ j ] ) ; 
 } 
 } 
 void InMaTran ( float a [ ] [ 10 ] , int M , int N ) { 
 int i , j ; 
 for ( i = 0 ; i < M ; i + + ) 
 { 
 for ( j = 0 ; j < N ; j + + ) 
 printf ( " % . 3f " , a [ i ] [ j ] ) ; 
 printf ( " \ n " ) ; 
 } 
 } 
 / / Cong 2 ma tran A & B ket qua la ma tran C 
 void CongMaTran ( float a [ ] [ 10 ] , float b [ ] [ 10 ] , 
 int M , int N , float c [ ] [ 10 ] ) 
 { 
 int i , j ; 
 for ( i = 0 ; i < M ; i + + ) 
 for ( j = 0 ; j < N ; j + + ) 
 c [ i ] [ j ] = a [ i ] [ j ] + b [ i ] [ j ] ; 
 } 
 main ( ) 
 { 
 float a [ 10 ] [ 10 ] , b [ 10 ] [ 10 ] , c [ 10 ] [ 10 ] ; 
 int M , N ; 
 printf ( " So dong M = " ) ; scanf ( " % d " , & M ) ;

---

## TRANG 99
Lập_trình căn_bản 
 printf ( " So cot M = " ) ; scanf ( " % d " , & N ) ; 
 printf ( " Nhap ma tran A \ n " ) ; 
 Nhap ( a , M , N ) ; 
 printf ( " Nhap ma tran B \ n " ) ; 
 Nhap ( b , M , N ) ; 
 printf ( " Ma_tran A : \ n " ) ; 
 InMaTran ( a , M , N ) ; 
 printf ( " Ma_tran B : \ n " ) ; 
 InMaTran ( b , M , N ) ; 
 CongMaTran ( a , b , M , N , c ) ; 
 printf ( " Ma_tran tong C : \ n " ) ; 
 InMaTran ( c , M , N ) ; 
 getch ( ) ; 
 } 
 Thí_dụ 2 : Nhập vào một ma_trận 2 chiều gồm các số_thực , 
 in ra tổng của các phần_tử trên đường_chéo chính của ma_trận 
 này . 
 Ta nhận thấy rằng nếu ma_trận a có M dòng , N cột thì các 
 phần_tử của đường_chéo chính là các phần_tử có dạng : a [ i ] [ i ] với i 
  [ 1 … min ( M , N ) ] . 
 # include < conio . h > 
 # include < stdio . h > 
 main ( ) { 
 float a [ 10 ] [ 10 ] ; 
 int M , N , i , j , Min ; 
 float T ; 
 printf ( " So_dong ? " ) ; scanf ( " % d " , & M ) ; 
 printf ( " So cot ? " ) ; scanf ( " % d " , & N ) ; 
 for ( i = 0 ; i < M ; i + + ) 
 for ( j = 0 ; j < N ; j + + ) { 
 printf ( " Phan_tu ( % d , % d ) : " , i , j ) ; 
 scanf ( " % f " , & a [ i ] [ j ] ) ; 
 } 
 printf ( " Ma_tran vua nhap : \ n " ) ; 
 for ( i = 0 ; i < M ; i + + ) { 
 for ( j = 0 ; j < N ; j + + ) 
 printf ( " % . 2f " , a [ i ] [ j ] ) ; 
 printf ( " \ n " ) ;

---

## TRANG 100
Lập_trình căn_bản 
 } 
 T = 0.0 ; 
 Min = ( M > N ) ? N : M ; / * Tìm giá_trị nhỏ nhất 
 của M & N * / 
 for ( i = 0 ; i < Min ; i + + ) 
 T = T + a [ i ] [ i ] ; 
 printf ( " Tong cac phan tu o duong cheo 
 chinh la : % . 2f " , T ) ; 
 getch ( ) ; 
 } 
 IV. BÀI_TẬP 
 1 . Viết chương_trình nhập vào một dãy n số_thực a [ 0 ] , a [ 1 ] , ... , 
 a [ n - 1 ] , sắp_xếp dãy số theo thứ_tự giảm dần . In dãy số sau khi sắp 
 xếp . 
 2 . Giả_sử mảng a ban_đầu đã được sắp thứ tự tăng dần . Viết 
 chương_trình cho phép loại_bỏ các phần_tử trùng nhau trong mảng 
 a . 
 Thí_dụ : Mảng a - 1 0 0 2 2 3 
 Mảng sau khi loại các phần_tử trùng nhau : 
 - 1 0 2 3 
 3 . Viết chương_trình nhập vào một mảng , hãy xuất ra màn_hình : 
 - Phần_tử lớn nhất của mảng . 
 - Phần_tử nhỏ nhất của mảng . 
 - Tính tổng của các phần_tử trong mảng . 
 - Tính tổng_bình_phương các số_âm trong mảng . 
 4 . Viết chương_trình nhập vào một mảng số tự_nhiên . Hãy xuất ra 
 màn_hình : 
 - Dòng 1 : gồm các số_lẻ , tổng_cộng có bao_nhiêu số_lẻ . 
 - Dòng 2 : gồm các số_chẵn , tổng_cộng có bao_nhiêu số_chẵn . 
 - Dòng 3 : gồm các số_nguyên_tố , tổng_cộng có bao_nhiêu 
 số_nguyên_tố .

---

## TRANG 101
Lập_trình căn_bản 
 - Dòng 4 : gồm các số không phải là số_nguyên_tố , tổng 
 cộng có bao_nhiêu số không nguyên_tố . 
 5 . Viết chương_trình thực_hiện việc đảo một mảng một_chiều . 
 Thí_dụ : 1 2 3 4 5 7 9 đảo thành 9 7 5 4 3 2 1 . 
 6 . Viết chương_trình nhập vào một dãy các số theo thứ tự tăng , 
 nếu nhập sai quy_cách thì yêu_cầu nhập lại . In dãy số sau khi đã 
 nhập xong . Nhập thêm một_số mới và chèn số đó vào dãy đã có 
 sao cho dãy vẫn đảm_bảo thứ tự tăng . In lại dãy số để kiểm_tra . 
 7 . Viết chương_trình thực_hiện việc trộn hai mảng có thứ tự thành 
 một mảng có thứ_tự . Yêu_cầu không được gộp 2 mảng lại rồi mới 
 sắp thứ tự nhờ vào 1 hàm sắp_xếp . 
 8 . Viết chương_trình nhập vào một ma_trận ( mảng hai chiều ) các 
 số_nguyên , gồm m hàng , n cột . In ma_trận đó lên màn_hình . Nhập 
 một_số_nguyên khác vào và xét xem có phần_tử nào của ma_trận 
 trùng với số này không ? Ở vị_trí nào ? Có bao_nhiêu phần_tử ? 
 9 . Viết chương_trình để chuyển_đổi vị_trí từ dòng thành cột của 
 một ma_trận ( ma_trận chuyển vị ) vuông 4 hàng 4 cột . 
 Thí_dụ : 
 1 2 3 4 1 2 9 1 
 2 5 5 8 2 5 4 5 
 9 4 2 0 3 5 2 8 
 1 5 8 6 4 8 0 6 
 Viết chương_trình cho ma_trận trong trưởng hợp tổng_quát 
 ( cấp m * n : m dòng , n cột ) . 
 10 . Viết chương_trình nhập vào hai ma_trận A có cấp m , k và B 
 có cấp k , n . In hai ma_trận lên màn_hình . Tích hai ma_trận A và B 
 là ma_trận C được tính bởi công_thức : 
 c = a * b + a * b + a * b + ... + a * b 
 ij i1 1j i2 2j i3 3j ik kj 
 ( i = 0,1,2 , ... m - 1 ; j = 0,1,2 ... n - 1 ) 
 Tính ma_trận tích C và in kết_quả lên màn_hình . 
 11 . Xét ma_trận A vuông cấp n , các phần_tử a [ i , i ] ( i = 1 ... n ) 
 được gọi là đường_chéo chính của ma_trận vuông A. Ma_trận

---

## TRANG 102
Lập_trình căn_bản 
 vuông A được gọi là ma_trận tam_giác nếu tất_cả các phần_tử dưới 
 đường_chéo chính đều bằng 0 . Định_thức của ma_trận tam_giác 
 bằng tích các phần_tử trên đường_chéo chính . 
 Ta có_thể chuyển một ma_trận vuông bất_kỳ về ma_trận tam_giác 
 bằng thuật_toán : 
 - Xét cột i ( i = 0,1 ... n - 2 ) 
 - Trong cột i xét các phần_tử a [ k , i ] ( k = i + 1 ... n - 1 ) 
 + Nếu a [ k , i ] = 0 thì tăng k lên xét phần_tử khác 
 + Nếu a [ k , i ] < > 0 thì làm như sau : 
 Nhân toàn_bộ hàng k với - a [ i , i ] / a [ k , i ] 
 Lấy hàng k cộng vào hàng i sau khi thực_hiện_phép 
 nhân trên . 
 Đổi chỗ hai hàng i và k cho nhau 
 Nhân toàn_bộ hàng k với - 1 sau khi đã đổi chỗ với 
 hàng i 
 Tăng k lên xét phần_tử khác . 
 Viết chương_trình tính định_thức cấp n thông_qua các bước_nhập 
 ma_trận , in ma_trận , đưa ma_trận về dạng tam_giác , in ma_trận_tam 
 giác , in kết_quả tính định_thức .

---

## TRANG 103
Lập_trình căn_bản 
 Chương 7 
 CON_TRỎ 
 Các vấn_đề được trình_bày trong chương này : 
  Khái_niệm về kiểu dữ_liệu “ con_trỏ ” . 
  Cách khai_báo và cách sử_dụng biến kiểu con_trỏ . 
  Mối quan_hệ giữa mảng và con_trỏ . 
 I. GIỚI_THIỆU KIỂU DỮ_LIỆU CON_TRỎ 
 Các biến chúng_ta đã biết và sử_dụng trước đây đều là biến có 
 kích_thước và kiểu dữ_liệu xác_định . Người_ta gọi các biến kiểu 
 này là biến tĩnh . Khi khai_báo biến tĩnh , một lượng ô nhớ cho các 
 biến này sẽ được cấp_phát mà không cần biết trong quá_trình thực 
 thi chương_trình có sử_dụng hết lượng ô nhớ này hay không . Mặt 
 khác , các biến tĩnh dạng này sẽ tồn_tại trong suốt thời_gian thực 
 thi chương_trình dù có những biến mà chương_trình chỉ sử_dụng 1 
 lần rồi bỏ . 
 Do đó , một_số vấn_đề có_thể gặp phải khi sử_dụng các biến 
 tĩnh : 
 o Cấp_phát ô nhớ dư , gây ra lãng_phí ô nhớ . 
 o Cấp_phát ô nhớ thiếu , chương_trình thực_thi bị lỗi . 
 Để tránh những hạn_chế trên , người lập_trình được cung_cấp một 
 loại biến đặc_biệt gọi là biến_động với các đặc_điểm sau : 
 o Chỉ phát_sinh trong quá_trình thực_hiện chương_trình 
 chứ không phát_sinh lúc bắt_đầu chương_trình . 
 o Khi chạy chương_trình , kích_thước của biến , vùng nhớ 
 và địa_chỉ vùng nhớ được cấp_phát cho biến có_thể thay_đổi . 
 o Sau khi sử_dụng xong có_thể giải_phóng để tiết_kiệm 
 chỗ trong bộ_nhớ . 
 Tuy_nhiên một_số ngôn_ngữ lập_trình chẳng_hạn như C không 
 cung_cấp 1 cách_thức trực_tiếp để thao_tác với biến_động . Vì_thế ,

---

## TRANG 104
Lập_trình căn_bản 
 ngôn_ngữ C cung_cấp cho ta một loại biến đặc_biệt là biến con_trỏ 
 ( pointer ) với các đặc_điểm : 
 o Biến con_trỏ không chứa dữ_liệu mà chỉ chứa địa_chỉ 
 của dữ_liệu hay chứa địa_chỉ của ô nhớ chứa dữ_liệu . Lúc đó ô 
 nhớ chứa dữ_liệu có_thể coi như là 1 biến_động . 
 o Kích_thước của biến con_trỏ không phụ_thuộc vào kiểu 
 dữ_liệu , luôn có kích_thước cố_định là 2 byte ( giá_trị nguyên để 
 chứa địa_chỉ ) . 
 Như_vậy thực_chất vai_trò của biến con_trỏ chính là hỗ_trợ cho 
 người lập_trình cách thức thao_tác với các biến_động . 
 II. KHAI_BÁO VÀ SỬ_DỤNG BIẾN CON_TRỎ 
 II. 1 . Khai_báo biến con_trỏ 
 Cú_pháp : < Kiểu > * < Tên con_trỏ > 
 Ý_nghĩa : Khai_báo một biến có tên là Tên con_trỏ dùng để 
 chứa địa_chỉ của các biến có kiểu Kiểu . 
 Thí_dụ 1 : Khai_báo 2 biến a , b có kiểu int và 2 biến pa , pb 
 là 2 biến con_trỏ kiểu int . 
 int a , b , * pa , * pb ; 
 Thí_dụ 2 : Khai_báo biến f kiểu float và biến pf là con_trỏ 
 float 
 float f , * pf ; 
 Ghi_chú : Nếu chưa muốn khai_báo kiểu dữ_liệu mà con_trỏ 
 ptr đang chỉ đến , ta sử_dụng con_trỏ void : 
 void * ptr ; 
 Sau đó , nếu ta muốn con_trỏ ptr chỉ đến kiểu dữ_liệu gì 
 cũng được . Tác_dụng của khai_báo này là chỉ dành ra 2 bytes 
 trong bộ_nhớ để cấp_phát cho biến con_trỏ ptr .

---

## TRANG 105
Lập_trình căn_bản 
 II. 2 . Các thao_tác trên con_trỏ 
 II. 2.1 Gán địa_chỉ của biến cho biến con_trỏ 
 Toán_tử & dùng để trả về địa_chỉ của 1 biến ( định_vị con 
 trỏ đến địa_chỉ của một biến ) . 
 Cú_pháp : < Tên biến con_trỏ > = & < Tên biến > 
 Giải_thích : Ta gán địa_chỉ của biến Tên biến cho con_trỏ 
 Tên biến con_trỏ . 
 Thí_dụ : Gán địa_chỉ của biến a cho con_trỏ pa , gán địa_chỉ 
 của biến b cho con_trỏ pb . 
 pa = & a ; pb = & b ; 
 Lúc này , hình_ảnh của các biến trong bộ_nhớ được mô_tả :

| a | b |
| --- | --- |


pa pb 2 2 
 byte byte 
 Lưu_ý : 
 Khi gán địa_chỉ của 1 biến cho 1 con_trỏ cần phải lưu_ý 
 kiểu dữ_liệu của chúng . Ví_dụ sau đây không đúng do không 
 tương_thích kiểu : 
 int Bien_Nguyen ; 
 float * Con_Tro_Thuc ; 
 ... 
 Con_Tro_Thuc = & Bien_Nguyen ; 
 Phép gán ở đây là sai vì Con_Tro_Thuc là một con_trỏ 
 kiểu float ( nó chỉ có_thể chứa được địa_chỉ của biến kiểu float ) ; 
 trong khi đó , Bien_Nguyen có kiểu int , nghĩa_là & Bien_Nguyen 
 chính là địa_chỉ của 1 biến int . .

---

## TRANG 106
Lập_trình căn_bản 
 II. 2.2 Nội_dung của ô nhớ con_trỏ chỉ tới 
 Để truy_cập đến nội_dung của ô nhớ mà con_trỏ chỉ tới , ta 
 sử_dụng cú_pháp : 
 * < Tên biến con_trỏ > 
 Với cách truy_cập này thì * < Tên biến con_trỏ > có_thể coi 
 là một biến có kiểu được mô_tả trong phần khai_báo biến con_trỏ . 
 Để_ý rằng cách viết như trên chính là cách thức thao_tác với các 
 biến_động . 
 Thí_dụ : Khai_báo , gán địa_chỉ cũng như lấy nội_dung vùng 
 nhớ của biến con_trỏ : 
 int x = 100 ; 
 int * ptr ; 
 ptr = & x ; 
 int y = * ptr ; 
 Lưu_ý : Khi gán địa_chỉ của một biến cho một biến con_trỏ , 
 mọi sự thay_đổi trên nội_dung ô nhớ con_trỏ chỉ tới sẽ làm giá_trị 
 của biến thay_đổi theo ( thực_chất nội_dung ô nhớ và biến chỉ là 
 một ) . 
 Thí_dụ : Đoạn chương_trình sau thấy rõ sự thay_đổi này : 
 # include < stdio . h > 
 main ( ) { 
 int a , b , * pa , * pb ; 
 a = 2 ; 
 b = 3 ; 
 printf ( " \ nGia tri cua bien a = % d \ n 
 Gia tri cua bien b = % d " , a , b ) ; 
 pa = & a ; 
 pb = & b ; 
 printf ( " \ nNoi dung cua o nho con tro_pa 
 tro toi = % d " , * pa ) ; 
 printf ( " \ nNoi dung cua o nho con tro pb 
 tro toi = % d " , * pb ) ; 
 * pa = 20 ; / / Thay_đổi giá_trị của * pa 
 * pb = 20 ; / / Thay_đổi giá_trị của * pb 
 printf ( " \ nGia tri moi cua bien a = % d \ n 
 Gia tri moi cua bien b = % d " , a , b ) ; 
 }

---

## TRANG 107
Lập_trình căn_bản 
 Kết_quả_thực_hiện chương_trình : 
 II. 2.3 Cấp_phát vùng nhớ để biến con_trỏ quản_lý địa_chỉ 
 Thực_chất của con_trỏ là chứa địa_chỉ trong bộ_nhớ của 1 
 biến khác ( thông_thường gọi là 1 biến_động ) . Đặc_trưng của biến 
 động chính là chúng được cấp_phát 1 cách động trong quá_trình 
 thực_hiện của chương_trình . Ngôn_ngữ C hỗ_trợ một_số hàm để 
 cấp_phát vùng nhớ cho các biến_động này ; kết_quả trả về của các 
 hàm_cấp_phát này là địa_chỉ bắt_đầu ( con_trỏ ) của vùng nhớ được 
 cấp_phát . Đó là các hàm malloc ( ) , calloc ( ) trong thư_viện 
 malloc . h . 
 Cú_pháp các hàm : 
 - void * malloc ( size_t size ) : Cấp_phát vùng nhớ có kích 
 thước là size . 
 - void * calloc ( size_t nitems , size_t size ) : Cấp_phát_vùng 
 nhớ có kích_thước là nitems * size . 
 Thí_dụ : Giả_sử ta có khai_báo : 
 int a , * pa , * pb ; 
 pa = ( int * ) malloc ( sizeof ( int ) ) ; / * Cấp_phát_vùng 
 nhớ có kích_thước bằng với kích_thước của một_số_nguyên * / 
 pb = ( int * ) calloc ( 10 , sizeof ( int ) ) ; / * Cấp_phát_vùng 
 nhớ có_thể chứa được 10 số_nguyên * / 
 Lúc này hình_ảnh trong bộ_nhớ như sau : 
 0 1 2 3 4 5 6 7 8 9

pa 2 byte pb 2 byte

---

## TRANG 108
Lập_trình căn_bản 
 Lưu_ý : Khi sử_dụng hàm malloc ( ) hay calloc ( ) , ta phải ép 
 kiểu vì nguyên_mẫu ( prototype ) của các hàm này trả về con_trỏ 
 kiểu void . 
 II. 3.4 Cấp_phát lại vùng nhớ cho biến con_trỏ 
 Trong quá_trình thao_tác trên biến con_trỏ , nếu ta cần_cấp 
 phát thêm vùng nhớ có kích_thước lớn hơn vùng nhớ đã cấp_phát , 
 ta sử_dụng hàm realloc ( ) . 
 Cú_pháp : void * realloc ( void * block , size_t size ) 
 Ý_nghĩa : 
 - Cấp_phát lại 1 vùng nhớ cho con_trỏ block quản_lý , vùng 
 nhớ này có kích_thước mới là size ; khi cấp_phát lại thì nội_dung 
 vùng nhớ trước đó vẫn tồn_tại . 
 - Kết_quả trả về của hàm là địa_chỉ đầu_tiên của vùng nhớ 
 mới . Địa_chỉ này có_thể khác với địa_chỉ được chỉ ra khi cấp_phát 
 ban_đầu . 
 Thí_dụ : Trong thí_dụ trên ta có_thể cấp_phát lại vùng nhớ 
 do con_trỏ pa quản_lý như sau : 
 int a , * pa ; 
 pa = ( int * ) malloc ( sizeof ( int ) ) ; / * Cấp_phát_vùng 
 nhớ có kích_thước 2 byte * / 
 pa = realloc ( pa , 6 ) ; / * Cấp_phát lại vùng nhớ có 
 kích_thước 6 byte * / 
 II. 3.5 Giải_phóng vùng nhớ cho biến con_trỏ 
 Một vùng nhớ đã cấp_phát được quản_lý bởi 1 biến con_trỏ , 
 khi không còn sử_dụng nữa , ta sẽ thu_hồi lại vùng nhớ này nhờ 
 hàm free ( ) . 
 Cú_pháp : void free ( void * block ) 
 Ý_nghĩa : Giải_phóng vùng nhớ được quản_lý bởi con_trỏ 
 block . 
 Thí_dụ : Ở thí_dụ trên , sau khi thực_hiện xong , ta giải_phóng 
 vùng nhớ cho 2 biến con_trỏ pa & pb : 
 free ( pa ) ; free ( pb ) ;

---

## TRANG 109
Lập_trình căn_bản 
 II. 3.6 Một_số phép_toán trên con_trỏ 
 a . Phép gán con_trỏ : Hai con_trỏ cùng kiểu có_thể gán cho 
 nhau . 
 Thí_dụ : int a , * p , * a ; float * f ; 
 a = 5 ; p = & a ; q = p ; / * đúng * / 
 f = p ; / * sai do khác kiểu * / 
 Ta cũng có_thể ép kiểu con_trỏ theo cú_pháp : 
 ( < Kiểu kết_quả > * ) < Tên con_trỏ > 
 Chẳng_hạn , thí_dụ trên được viết lại : 
 int a , * p , * a ; float * f ; 
 a = 5 ; p = & a ; q = p ; / * đúng * / 
 f = ( float * ) p ; / / Đúng nhờ ép kiểu 
 b . Cộng , trừ con_trỏ với một_số_nguyên : Ta có_thể cộng 
 ( + ) , trừ ( - ) 1 con_trỏ với 1 số_nguyên N nào đó ; kết_quả trả về là 1 
 con_trỏ . Con_trỏ này chỉ đến vùng nhớ cách vùng nhớ của con_trỏ 
 hiện_tại N phần_tử . 
 Thí_dụ : Cho đoạn chương_trình sau : 
 int * pa ; 
 pa = ( int * ) malloc ( 20 ) ; / * Cấp_phát vùng nhớ 20 
 byte = 10 số_nguyên * / 
 int * pb , * pc ; 
 pb = pa + 7 ; 
 pc = pb - 3 ; 
 Lúc này hình_ảnh của pa , pb , pc như sau : 
 0 1 2 3 4 5 6 7 8 9

pa pc pb 
 c . Con_trỏ NULL : là con_trỏ không chứa địa_chỉ nào cả . Ta 
 có_thể gán giá_trị NULL cho 1 con_trỏ có kiểu bất_kỳ . 
 d . Lưu_ý : 
 - Ta không_thể cộng 2 con_trỏ với nhau . 
 - Phép_trừ 2 con_trỏ cùng kiểu sẽ trả về 1 giá_trị_nguyên 
 ( int ) . Đây chính là khoảng_cách ( số phần_tử ) giữa 2 con_trỏ đó . 
 Chẳng_hạn , trong ví_dụ trên pc - pa = 4 .

---

## TRANG 110
Lập_trình căn_bản 
 III. CON_TRỎ VÀ MẢNG 
 Giữa mảng và con_trỏ có một sự liên_hệ rất chặt_chẽ . Trong C , 
 thực_chất tên mảng chính là con_trỏ chứa địa_chỉ của phần_tử đầu 
 tiên trong mảng đó . Do đó , những phần_tử của mảng có_thể được 
 xác_định bằng chỉ_số trong mảng , bên cạnh đó chúng cũng có_thể 
 được xác_lập qua biến con_trỏ . 
 III. 1 Con_trỏ và mảng 1 chiều 
 III. 1.1 Truy_cập các phần_tử mảng theo dạng con_trỏ 
 Ta có các quy_tắc sau : 
 & < Tên mảng > [ 0 ] tương_đương với < Tên mảng > 
 & < Tên mảng > [ < Vị_trí > ] tương_đương với < Tên mảng > + < Vị_trí > 
 < Tên mảng > [ < Vị_trí > ] tương_đương với * ( < Tên mảng > + < Vị_trí > ) 
 Thí_dụ : Cho 1 mảng 1 chiều các số_nguyên a có 5 phần_tử , 
 truy_cập các phần_tử theo kiểu mảng và theo kiểu con_trỏ . 
 # include < stdio . h > 
 # include < conio . h > 
 / / Nhập mảng bình_thường 
 void NhapMang ( int a [ ] , int N ) { 
 int i ; 
 for ( i = 0 ; i < N ; i + + ) 
 { 
 printf ( " Phan_tu thu % d : " , i ) ; 
 scanf ( " % d " , & a [ i ] ) ; 
 } 
 } 
 / / Nhập mảng theo dạng con_trỏ 
 void NhapContro ( int a [ ] , int N ) { 
 int i ; 
 for ( i = 0 ; i < N ; i + + ) 
 { 
 printf ( " Phan_tu thu % d : " , i ) ; 
 scanf ( " % d " , a + i ) ; 
 } 
 } 
 main ( ) 
 { 
 int a [ 20 ] , N , i ; 
 printf ( " So phan tu N = " ) ; scanf ( " % d " , & N ) ; 
 NhapMang ( a , N ) ; / / NhapContro ( a , N )

---

## TRANG 111
Lập_trình căn_bản 
 printf ( " Truy_cap theo kieu mang : " ) ; 
 for ( i = 0 ; i < N ; i + + ) 
 printf ( " % d " , a [ i ] ) ; 
 printf ( " \ nTruy cap theo kieu con tro : " ) ; 
 for ( i = 0 ; i < N ; i + + ) 
 printf ( " % d " , * ( a + i ) ) ; 
 getch ( ) ; 
 } 
 Kết_quả_thực_thi của chương_trình : 
 III. 1.2 Truy_xuất từng phần_tử đang được quản_lý bởi con_trỏ 
 theo dạng_mảng 
 < Tên biến > [ < Vị_trí > ] tương_đương với * ( < Tên biến > + < Vị_trí > ) 
 & < Tên biến > [ < Vị_trí > ] tương_đương với ( < Tên biến > + < Vị_trí > ) 
 Trong đó < Tên biến > là biến con_trỏ , < Vị_trí > là 1 biểu 
 thức số_nguyên . 
 Thí_dụ : Giả_sử có khai_báo : 
 # include < stdio . h > 
 # include < malloc . h > 
 # include < conio . h > 
 main ( ) { 
 int * a ; 
 int i ; 
 a = ( int * ) malloc ( sizeof ( int ) * 10 ) ; 
 for ( i = 0 ; i < 10 ; i + + ) 
 a [ i ] = 2 * i ; 
 printf ( " Truy_cap theo kieu mang : " ) ; 
 for ( i = 0 ; i < 10 ; i + + ) 
 printf ( " % d " , a [ i ] ) ; 
 printf ( " \ nTruy cap theo kieu con tro : " ) ; 
 for ( i = 0 ; i < 10 ; i + + ) 
 printf ( " % d " , * ( a + i ) ) ; 
 getch ( ) ; 
 }

---

## TRANG 112
Lập_trình căn_bản 
 Kết_quả chương_trình : 
 Với khai_báo ở trên , hình_ảnh của con_trỏ a trong bộ_nhớ : 
 0 1 2 3 4 5 6 7 8 9

| 0 | 2 | 4 | 6 | 8 | 10 | 12 | 14 | 16 | 18 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |


a 2 byte 
 III. 1.3 Con_trỏ chỉ đến phần_tử mảng 
 Giả_sử con_trỏ ptr chỉ đến phần_tử a [ i ] nào đó của mảng a 
 thì : 
 ptr + j chỉ đến phần_tử thứ j sau a [ i ] , tức a [ i + j ] 
 ptr - j chỉ đến phần_tử đứng trước a [ i ] , tức a [ i - j ] 
 Thí_dụ : Giả_sử có 1 mảng mang_int , cho con_trỏ contro_int 
 chỉ đến phần_tử thứ 5 trong mảng . In ra các phần_tử của 
 contro_int & mang_int . 
 # include < stdio . h > 
 # include < conio . h > 
 # include < malloc . h > 
 main ( ) { 
 int i , mang_int [ 10 ] ; 
 int * contro_int ; 
 for ( i = 0 ; i < = 9 ; i + + ) 
 mang_int [ i ] = i * 2 ; 
 contro_int = & mang_int [ 5 ] ; 
 printf ( " \ nNoi dung cua mang_int ban dau = " ) ; 
 for ( i = 0 ; i < = 9 ; i + + ) 
 printf ( " % d " , mang_int [ i ] ) ; 
 printf ( " \ nNoi dung cua contro_int ban dau = " ) ; 
 for ( i = 0 ; i < 5 ; i + + ) 
 printf ( " % d " , contro_int [ i ] ) ; 
 for ( i = 0 ; i < 5 ; i + + ) 
 contro_int [ i ] + + ; 
 printf ( " \ n - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - " ) ;

---

## TRANG 113
Lập_trình căn_bản 
 printf ( " \ nNoi dung cua mang_int sau khi tang 1 = " ) ; 
 for ( i = 0 ; i < = 9 ; i + + ) 
 printf ( " % d " , mang_int [ i ] ) ; 
 printf ( " \ nNoi dung cua contro_int 
 sau khi tang 1 = " ) ; 
 for ( i = 0 ; i < 5 ; i + + ) 
 printf ( " % d " , contro_int [ i ] ) ; 
 if ( contro_int ! = NULL ) 
 free ( contro_int ) ; 
 getch ( ) ; 
 } 
 Kết_quả chương_trình 
 III. 2 Con_trỏ và mảng nhiều chiều 
 Giả_sử ta có mảng 2 chiều và biến con_trỏ như sau : 
 int a [ n ] [ m ] ; 
 int * contro_int ; 
 Thực_hiện phép gán contro_int = a ; 
 Khi đó phần_tử a [ 0 ] [ 0 ] được quản_lý bởi contro_int ; 
 a [ 0 ] [ 1 ] được quản_lý bởi contro_int + 1 ; 
 a [ 0 ] [ 2 ] được quản_lý bởi contro_int + 2 ; 
 ... 
 a [ 1 ] [ 0 ] được quản_lý bởicontro_int + m ; 
 a [ 1 ] [ 1 ] được quản_lý bởi contro_int + m + 1 ; 
 ... 
 a [ n ] [ m ] được quản_lý bởi contro_int + n * m ; 
 Tương_tự như thế đối_với mảng nhiều hơn 2 chiều .

---

## TRANG 114
Lập_trình căn_bản 
 Thí_dụ : Sự tương_đương giữa mảng 2 chiều và con_trỏ . 
 # include < stdio . h > 
 # include < conio . h > 
 # include < malloc . h > 
 main ( ) 
 { 
 int i , j ; 
 int mang_int [ 4 ] [ 5 ] = { 1,2,3,4,5,6,7,8,9,10,11 , 
 12,13,14,15,16,17,18,19,20 } ; 
 int * contro_int ; 
 contro_int = ( int * ) mang_int ; 
 printf ( " \ nNoi dung cua mang_int ban dau = " ) ; 
 for ( i = 0 ; i < 4 ; i + + ) 
 { 
 printf ( " \ n " ) ; 
 for ( j = 0 ; j < 5 ; j + + ) 
 printf ( " % d \ t " , mang_int [ i ] [ j ] ) ; 
 } 
 printf ( " \ n - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - " ) ; 
 printf ( " \ nNoi dung cua contro_int ban dau \ n " ) ; 
 for ( i = 0 ; i < 20 ; i + + ) 
 printf ( " % d " , contro_int [ i ] ) ; 
 for ( i = 0 ; i < 20 ; i + + ) 
 contro_int [ i ] + + ; 
 printf ( " \ n - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - " ) ; 
 printf ( " \ nNoi dung cua mang_int sau khi tang 1 = " ) ; 
 for ( i = 0 ; i < 4 ; i + + ) 
 { 
 printf ( " \ n " ) ; 
 for ( j = 0 ; j < 5 ; j + + ) 
 printf ( " % d \ t " , mang_int [ i ] [ j ] ) ; 
 } 
 printf ( " \ nNoi dung cua contro_int 
 sau khi tang 1 = \ n " ) ; 
 for ( i = 0 ; i < 20 ; i + + ) 
 printf ( " % d " , contro_int [ i ] ) ; 
 if ( contro_int ! = NULL ) 
 free ( contro_int ) ; 
 getch ( ) ;

---

## TRANG 115
Lập_trình căn_bản 
 } 
 Kết_quả_thực_hiện chương_trình như sau : 
 IV. CON_TRỎ LÀ THAM_SỐ HÌNH_THỨC CỦA HÀM 
 Khi tham_số hình_thức của hàm là một con_trỏ thì theo nguyên_tắc 
 gọi hàm ta dùng tham_số thực_tế là 1 con_trỏ có kiểu giống với 
 kiểu của tham_số hình_thức . Nếu lúc thực_thi hàm ta có sự thay 
 đổi trên nội_dung vùng nhớ được chỉ bởi con_trỏ tham_số hình 
 thức thì lúc đó nội_dung vùng nhớ được chỉ bởi tham_số thực_tế 
 cũng sẽ bị thay_đổi theo . 
 Thí_dụ : Xét hàm hoán_vị được viết như sau : 
 # include < stdio . h > 
 # include < conio . h > 
 void HoanVi ( int * a , int * b ) { 
 int c = * a ; 
 * a = * b ; 
 * b = c ; 
 } 
 main ( ) { 
 int m = 20 , n = 30 ; 
 printf ( " Truoc khi goi ham m = % d , 
 n = % d \ n " , m , n ) ; 
 HoanVi ( & m , & n ) ; 
 printf ( " Sau khi goi ham m = % d , 
 n = % d " , m , n ) ; 
 getch ( ) ; 
 }

---

## TRANG 116
Lập_trình căn_bản 
 Kết_quả_thực_thi chương_trình : 
 Giải_thích : 
 Với việc khi tham_số hình_thức là 1 con_trỏ có_thể làm thay 
 đổi giá_trị của vùng dữ_liệu của con_trỏ tham_số thực_tế nên_người 
 ta có_thể sử_dụng cách_thức truyền tham_số là con_trỏ để có_thể 
 nhận kết_quả trả về là vùng dữ_liệu của con_trỏ tham_số thực_tế . 
 Thí_dụ : Viết 1 hàm tính n ! nhưng sử_dụng tham_số hình 
 thức là 1 con_trỏ để có_thể nhận được kết_quả trả về sau khi thực 
 thi hàm :

---

## TRANG 117
Lập_trình căn_bản 
 void giaithua ( int n , long * K ) { 
 int i ; 
 ( * K ) = 1L ; 
 for ( i = 1 ; i < = n ; i + + ) 
 ( * K ) = ( * K ) * i ; 
 } 
 main ( ) { 
 int n ; 
 long KQ ; 
 printf ( " Nhap so n = " ) ; scanf ( " % d " , & n ) ; 
 giaithua ( n , & KQ ) ; 
 printf ( " \ n % d ! = % ld " , n , KQ ) ; 
 getch ( ) ; 
 }

---

## TRANG 118
Lập_trình căn_bản 
 Chương 8 
 CHUỖI KÝ_TỰ 
 Các vấn_đề được trình_bày trong chương này : 
  Khái_niệm về chuỗi ký_tự . 
  Một_số hàm xử_lý chuỗi và áp_dụng của chúng . 
 I. KHÁI_NIỆM 
 Chuỗi ký_tự là một dãy gồm các ký_tự hoặc một mảng các 
 ký_tự được kết_thúc bằng ký_tự ‘ \ 0 ’ ( còn được gọi là ký_tự NULL 
 trong bảng mã ASCII ) . 
 Các hằng chuỗi ký_tự được đặt trong cặp dấu nháy kép “ ” . 
 II. KHAI_BÁO 
 Ngôn_ngữ C không hỗ_trợ chuỗi ký_tự như là 1 kiểu riêng . Thực 
 chất chuỗi ký_tự trong C được coi như là 1 mảng gồm các phần_tử 
 là 1 ký_tự ( kiểu char ) với ký_tự cuối_cùng là ký_tự có mã ASCII là 
 0 ( ‘ \ 0 ’ ) . Vì_thế , việc khai_báo chuỗi ký_tự trong C chính là khai 
 báo 1 mảng ký_tự ( hoặc có_thể là 1 con_trỏ chỉ đến vùng nhớ 1 ký 
 tự ) . 
 II. 1 Khai_báo theo mảng 
 Cú_pháp : char < Biến > [ Chiều_dài tối_đa ] 
 Thí_dụ : Trong chương_trình , ta có khai_báo : 
 char Ten [ 12 ] ; 
 Đây là khai_báo của 1 biến chuỗi Ten có chiều_dài 
 tối_đa 12 ký_tự . 
 Ghi_chú : 
 - Chiều_dài tối_đa không nên khai_báo thừa để tránh lãng 
 phí bộ_nhớ , nhưng cũng không nên khai_báo thiếu . 
 - Với việc khai_báo 1 mảng ký_tự như trên , ký_tự ‘ \ 0 ’ 
 không được tự_động thêm vào cuối chuỗi .

---

## TRANG 119
Lập_trình căn_bản 
 II. 2 Khai_báo theo con_trỏ 
 Cú_pháp : char * < Biến > 
 Thí_dụ : Trong chương_trình , ta có khai_báo : 
 char * Ten ; 
 Trong khai_báo này , bộ_nhớ sẽ dành 2 byte để lưu 
 trữ địa_chỉ của biến con_trỏ Ten đang chỉ đến , chưa cung_cấp nơi 
 để lưu_trữ dữ_liệu . Muốn có chỗ để lưu_trữ dữ_liệu , ta phải gọi đến 
 hàm malloc ( ) hoặc calloc ( ) có trong “ malloc . h ” , sau đó mới gán 
 dữ_liệu cho biến . 
 II. 3 Vừa khai_báo vừa gán giá_trị 
 Cú_pháp : char < Biến > [ ] = < ” Hằng chuỗi ” > 
 Thí_dụ : 
 # include < stdio . h > 
 # include < conio . h > 
 main ( ) { 
 char Chuoi [ ] = " Mau nang hay la mau mat em ” ; 
 printf ( " Vua khai bao vua gan trị : % s ” , 
 Chuoi ) ; 
 getch ( ) ; 
 } 
 Ghi_chú : Chuỗi được khai_báo là một mảng các ký_tự nên 
 các thao_tác trên mảng có_thể áp_dụng đối_với chuỗi ký_tự . 
 III. CÁC THAO_TÁC TRÊN CHUỖI KÝ_TỰ 
 III. 1 . Nhập xuất_chuỗi 
 III. 1.1 Nhập chuỗi từ bàn_phím 
 Để nhập một chuỗi ký_tự từ bàn_phím , ta sử_dụng hàm 
 gets ( ) 
 Cú_pháp : gets ( < Biến chuỗi > ) 
 Thí_dụ : char Ten [ 20 ] ; 
 gets ( Ten ) ; 
 Ta cũng có_thể sử_dụng hàm scanf ( ) để nhập dữ_liệu cho 
 biến chuỗi , tuy_nhiên lúc này ta chỉ có_thể nhập được một chuỗi 
 không có dấu khoảng trắng .

---

## TRANG 120
Lập_trình căn_bản 
 Khi nhập chuỗi bằng hàm gets , ký_tự ‘ \ 0 ’ được tự_động 
 thêm vào cuối chuỗi . 
 III. 1.2 Xuất chuỗi lên màn_hình 
 Để xuất một chuỗi ( biểu_thức chuỗi ) lên màn_hình , ta sử 
_dụng hàm puts ( ) . 
 Cú_pháp : puts ( < Biểu_thức chuỗi > ) 
 Thí_dụ : Nhập vào một chuỗi và hiển_thị trên màn_hình chuỗi 
 vừa nhập . 
 # include < conio . h > 
 # include < stdio . h > 
 # include < string . h > 
 main ( ) { 
 char Ten [ 12 ] ; 
 printf ( " Nhap chuoi : " ) ; gets ( Ten ) ; 
 printf ( " Chuoi vua nhap : " ) ; puts ( Ten ) ; 
 getch ( ) ; 
 } 
 Ngoài_ra , ta có_thể sử_dụng hàm printf ( ) , cputs ( ) ( trong 
 conio . h ) để hiển_thị chuỗi lên màn_hình . 
 III. 2 Một_số hàm xử_lý chuỗi ( trong string . h ) 
 III. 2.1 Cộng_chuỗi - Hàm_strcat ( ) 
 Cú_pháp : char * strcat ( char * des , const char * source ) 
 Hàm này có tác_dụng ghép chuỗi nguồn vào chuỗi đích . 
 Thí_dụ : Nhập vào họ lót và tên của một người , sau đó in cả 
 họ và tên của họ lên màn_hình . 
 # include < stdio . h > 
 # include < string . h > 
 main ( ) { 
 char HoLot [ 30 ] , Ten [ 12 ] ; 
 printf ( " Nhap_Ho_Lot : " ) ; gets ( HoLot ) ; 
 printf ( " Nhap Ten : " ) ; gets ( Ten ) ; 
 strcat ( HoLot , Ten ) ; / / Ghep Ten vao HoLot 
 printf ( " Ho ten la : " ) ; puts ( HoLot ) ; 
 }

---

## TRANG 121
Lập_trình căn_bản 
 III. 2.2 Xác_định độ dài chuỗi - Hàm_strlen ( ) 
 Cú_pháp : int strlen ( const char * s ) 
 Thí_dụ : Sử_dụng hàm strlen xác_định độ dài một chuỗi 
 nhập từ bàn_phím . 
 # include < conio . h > 
 # include < stdio . h > 
 # include < string . h > 
 main ( ) 
 { 
 char Chuoi [ 255 ] ; 
 int Dodai ; 
 printf ( " Nhap chuoi : " ) ; gets ( Chuoi ) ; 
 Dodai = strlen ( Chuoi ) 
 printf ( " Chuoi vua nhap : " ) ; puts ( Chuoi ) ; 
 printf ( “ Co do dai % d ” , Dodai ) ; 
 getch ( ) ; 
 } 
 III. 2.3 Đổi một ký_tự thường thành ký_tự hoa và ngược_lại 
 Hàm_toupper ( ) ( trong ctype . h ) cho phép trả về ký_tự hoa 
 của 1 ký_tự đầu_vào là tham_số của hàm . Ngược_lại , hàm 
 tolower ( ) trả về ký_tự thường của ký_tự đầu_vào là tham_số của 
 hàm . 
 Cú_pháp : char toupper ( char c ) 
 char tolower ( chart c ) 
 III. 2.4 Đổi chuỗi chữ thường thành chuỗi chữ hoa , hàm strupr ( ) 
 Hàm_struppr ( ) được dùng để chuyển_đổi chuỗi chữ thường 
 thành chuỗi chữ hoa , kết_quả trả về của hàm là một con_trỏ chỉ 
 đến địa_chỉ chuỗi được chuyển_đổi . 
 Cú_pháp : char * strupr ( char * s ) 
 Thí_dụ : Viết chương_trình nhập vào một chuỗi ký_tự từ bàn 
 phím . Sau đó sử_dụng hàm strupr ( ) để chuyển_đổi chúng_thành 
 chuỗi chữ hoa . 
 # include < conio . h > 
 # include < stdio . h > 
 # include < string . h >

---

## TRANG 122
Lập_trình căn_bản 
 main ( ) { 
 char Chuoi [ 255 ] , * s ; 
 printf ( " Nhap chuoi : " ) ; gets ( Chuoi ) ; 
 s = strupr ( Chuoi ) ; 
 printf ( “ Chuoi chu hoa : ” ) ; puts ( s ) ; 
 getch ( ) ; 
 } 
 III. 2.5 Đổi chuỗi chữ hoa thành chuỗi chữ thường , hàm strlwr ( ) 
 Muốn chuyển_đổi chuỗi chữ hoa thành chuỗi toàn_chữ 
 thường , ta sử_dụng hàm strlwr ( ) , các tham_số của hàm tương_tự 
 như hàm strupr ( ) 
 Cú_pháp : char * strlwr ( char * s ) 
 III. 2.6 Sao_chép chuỗi , hàm strcpy ( ) 
 Hàm này được dùng để sao_chép toàn_bộ nội_dung của 
 chuỗi nguồn vào chuỗi đích . 
 Cú_pháp : char * strcpy ( char * Des , const char * Source ) 
 Thí_dụ : Viết chương_trình cho phép chép toàn_bộ chuỗi 
 nguồn vào chuỗi đích . 
 # include < conio . h > 
 # include < stdio . h > 
 # include < string . h > 
 main ( ) { 
 char Chuoi [ 255 ] , s [ 255 ] ; 
 printf ( " Nhap chuoi : " ) ; gets ( Chuoi ) ; 
 strcpy ( s , Chuoi ) ; 
 printf ( “ Chuoi dich : ” ) ; puts ( s ) ; 
 getch ( ) ; 
 } 
 III. 2.7 Sao_chép một phần chuỗi , hàm strncpy ( ) 
 Hàm này cho phép chép n ký_tự đầu_tiên của chuỗi nguồn 
 sang chuỗi đích . 
 Cú_pháp : 
 char * strncpy ( char * Des , const char * Source , size_t n )

---

## TRANG 123
Lập_trình căn_bản 
 Để_ý rằng khi sao_chép n ký_tự đầu_tiên của chuỗi nguồn 
 vào chuỗi đích , ký_tự ‘ \ 0 ’ không được tự_động thêm vào chuỗi 
 đích . 
 III. 2.8 Trích một phần chuỗi , hàm strchr ( ) 
 Để trích một chuỗi con của một chuỗi ký_tự bắt_đầu_từ một 
 ký_tự được chỉ_định trong chuỗi cho đến hết chuỗi , ta sử_dụng 
 hàm strchr ( ) . 
 Cú_pháp : char * strchr ( const char * str , int c ) 
 Ghi_chú : 
 - Nếu ký_tự đã chỉ_định không có trong chuỗi , kết_quả trả 
 về là NULL. 
 - Kết_quả trả về của hàm là một con_trỏ , con_trỏ này chỉ 
 đến ký_tự c được tìm thấy đầu_tiên trong chuỗi str . 
 III. 2.9 Tìm_kiếm nội_dung chuỗi , hàm strstr ( ) 
 Hàm_strstr ( ) được sử_dụng để tìm_kiếm sự xuất_hiện đầu 
 tiên của chuỗi s2 trong chuỗi s1 . 
 Cú_pháp : char * strstr ( const char * s1 , const char * s2 ) 
 Kết_quả trả về của hàm là một con_trỏ chỉ đến phần_tử đầu 
 tiên của chuỗi s1 có chứa chuỗi s2 hoặc giá_trị NULL nếu chuỗi 
 s2 không có trong chuỗi s1 . 
 Thí_dụ : Viết chương_trình sử_dụng hàm strstr ( ) để lấy ra 
 một phần của chuỗi gốc bắt_đầu_từ chuỗi “ hoc ” . 
 # include < conio . h > 
 # include < stdio . h > 
 # include < string . h > 
 main ( ) { 
 char Chuoi [ 255 ] , * s ; 
 printf ( " Nhap chuoi : " ) ; gets ( Chuoi ) ; 
 s = strstr ( Chuoi , ” hoc ” ) ; 
 printf ( “ Chuoi trich ra : ” ) ; puts ( s ) ; 
 getch ( ) ; 
 }

---

## TRANG 124
Lập_trình căn_bản 
 III. 2.10 So_sánh chuỗi , hàm strcmp ( ) 
 Để so_sánh hai chuỗi theo từng ký_tự trong bảng mã Ascii , 
 ta có_thể sử_dụng hàm strcmp ( ) . 
 Cú_pháp : int strcmp ( const char * s1 , const char * s2 ) 
 Hai chuỗi s1 và s2 được so_sánh với nhau , kết_quả trả về là 
 một_số_nguyên ( số này có được bằng cách lấy ký_tự của s1 trừ_ký 
 tự của s2 tại vị_trí đầu_tiên xảy ra sự khác nhau hoặc là 0 nếu 1 
 chuỗi giống nhau hoàn_toàn ) . 
 - Nếu kết_quả là số_âm , chuỗi s1 nhỏ hơn chuỗi s2 . 
 - Nếu kết_quả là 0 , hai chuỗi bằng nhau . 
 - Nếu kết_quả là số_dương , chuỗi s1 lớn hơn chuỗi s2 . 
 III. 2.11 So_sánh chuỗi , hàm stricmp ( ) 
 Hàm này thực_hiện việc so_sánh trong n ký_tự đầu_tiên của 
 2 chuỗi s1 và s2 , giữa chữ thường và chữ hoa không phân_biệt . 
 Cú_pháp : int stricmp ( const char * s1 , const char * s2 ) 
 Kết_quả trả về tương_tự như kết_quả trả về của hàm 
 strcmp ( ) . 
 III. 2.12 Khởi tạo chuỗi , hàm memset ( ) 
 Hàm này được sử_dụng để đặt n ký_tự đầu_tiên của chuỗi là 
 ký_tự c . 
 Cú_pháp : memset ( char * Des , int c , size_t n ) 
 III. 2.13 Đổi từ chuỗi ra số , hàm atoi ( ) , atof ( ) , atol ( ) ( trong 
 stdlib . h ) 
 Để chuyển_đổi chuỗi ra số , ta sử_dụng các hàm trên . 
 Cú_pháp : int atoi ( const char * s ) : chuyển chuỗi 
 thành số_nguyên 
 long atol ( const char * s ) : chuyển chuỗi 
 thành số_nguyên_dài 
 float atof ( const char * s ) : chuyển chuỗi 
 thành số_thực

---

## TRANG 125
Lập_trình căn_bản 
 Nếu chuyển_đổi không thành_công , kết_quả trả về của các 
 hàm là 0 . 
 Ngoài_ra , thư_viện string . h còn hỗ_trợ các hàm xử_lý_chuỗi 
 khác , ta có_thể đọc thêm trong phần trợ_giúp . 
 IV. BÀI_TẬP 
 1 . Viết chương_trình nhập một chuỗi ký_tự từ bàn_phím , xuất ra 
 màn_hình mã Ascii của từng ký_tự có trong chuỗi . 
 2 . Viết chương_trình nhập một chuỗi ký_tự từ bàn_phím , xuất ra 
 màn_hình chuỗi đảo_ngược của chuỗi đó . Thí_dụ đảo của “ abcd 
 egh ” là “ hge dcba ” . 
 3 . Viết chương_trình nhập một chuỗi ký_tự và kiểm_tra xem chuỗi 
 đó có đối_xứng không . 
 Thí_dụ : Chuỗi ABCDEDCBA là chuỗi đối_xứng . 
 4 . Nhập vào một chuỗi bất_kỳ , hãy đếm số lần xuất_hiện của mỗi 
 ký_tự có trong chuỗi . 
 5 . Viết chương_trình nhập vào một chuỗi . 
 - Hiển_thị lên màn_hình từ bên trái nhất và phần còn lại của 
 chuỗi . Thí_dụ : “ Nguyen_Van_Minh ” in ra thành : 
 Nguyen 
 Van_Minh 
 - Hiển_thị lên màn_hình từ bên phải nhất và phần còn lại 
 của chuỗi . Thí_dụ : “ Nguyen_Van_Minh ” in ra thành : 
 Minh 
 Nguyen_Van 
 6 . Viết chương_trình nhập vào một chuỗi rồi xuất chuỗi đó ra màn 
 hình dưới dạng mỗi từ một dòng . 
 Thí_dụ : “ Nguyễn Văn_Minh ” 
 In ra : 
 Nguyen 
 Van 
 Minh

---

## TRANG 126
Lập_trình căn_bản 
 7 . Viết chương_trình nhập vào một chuỗi , in ra chuỗi đảo_ngược 
 của nó theo từng từ . 
 Thí_dụ : chuỗi “ Nguyen_Van_Minh ” đảo thành “ Minh_Van 
 Nguyen ” . 
 8 . Viết chương_trình nhập vào họ và tên của một người , cắt bỏ 
 các khoảng trống_không cần_thiết ( nếu có ) , tách tên ra khỏi họ và 
 tên , in tên lên màn_hình . Chú_ý đến trường_hợp cả họ và tên chỉ 
 có một từ . 
 9 . Viết chương_trình nhập vào họ và tên của một người , cắt bỏ 
 các khoảng trắng bên phải , trái và các khoảng trắng không có 
 nghĩa trong chuỗi . In ra màn_hình toàn_bộ họ tên người đó dưới 
 dạng chữ hoa , chữ thường . 
 10 . Viết chương_trình nhập vào một danh_sách họ và tên của n 
 người theo kiểu chữ thường , đổi các chữ_cái đầu của họ , tên và 
 chữ lót của mỗi người thành chữ hoa . In kết_quả lên màn_hình . 
 11 . Viết chương_trình nhập vào một danh_sách họ và tên của n 
 người , tách tên từng người ra khỏi họ và tên rồi sắp_xếp_danh 
 sách tên theo thứ_tự từ_điển . In danh_sách họ và tên sau khi đã sắp 
 xếp .

---

## TRANG 127
Lập_trình căn_bản 
 Chương 9 
 KIỂU CẤU_TRÚC - STRUCT 
 Chương này trình_bày các vấn_đề sau : 
  Khái_niệm về kiểu cấu_trúc . 
  Cách sử_dụng kiểu cấu_trúc . 
  Con_trỏ cấu_trúc . 
 I. KIỂU CẤU_TRÚC 
 I. 1 Khái_niệm 
 Kiểu cấu_trúc ( Structure ) là kiểu dữ_liệu bao_gồm nhiều thành 
 phần có kiểu khác nhau , mỗi thành_phần được gọi là một trường 
 ( field ) . 
 Sự khác_biệt giữa kiểu cấu_trúc và kiểu mảng là : các phần_tử của 
 mảng là cùng kiểu còn các phần_tử của kiểu cấu_trúc có_thể có 
 kiểu khác nhau . 
 Hình_ảnh của kiểu cấu_trúc được minh_họa : 
 1 2 3 4 5 6 7

Đây là cấu_trúc có 7 trường 
 Còn kiểu mảng có dạng : 
 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14

Đây là mảng có 15 phần_tử

---

## TRANG 128
Lập_trình căn_bản 
 I. 2 Định_nghĩa kiểu cấu_trúc 
 Cách 1 : 
 struct < Tên cấu_trúc > 
 { 
 < Kiểu > < Trường 1 > ; 
 < Kiểu > < Trường 2 > ; 
 … … . . 
 < Kiểu > < Trường n > ; 
 } ; 
 Cách 2 : Sử_dụng từ khóa typedef để định_nghĩa kiểu : 
 typedef struct 
 { 
 < Kiểu > < Trường 1 > ; 
 < Kiểu > < Trường 2 > ; 
 … … . . 
 < Kiểu > < Trường n > ; 
 } < Tên cấu_trúc > ; 
 Trong đó : 
 - < Tên cấu_trúc > : là một tên được đặt theo quy_tắc đặt tên 
 của danh biểu ; tên này mang ý_nghĩa sẽ là tên kiểu cấu_trúc . 
 - < Kiểu > < Trường i > ( i = 1 . . n ) : mỗi trường trong cấu_trúc 
 có dữ_liệu thuộc kiểu gì ( tên của trường phải là một tên được đặt 
 theo quy_tắc đặt tên của danh biểu ) . 
 Thí_dụ 1 : Để quản_lý ngày , tháng , năm của một ngày 
 trong năm ta có_thể khai_báo kiểu cấu_trúc gồm 3 thông_tin : ngày , 
 tháng , năm . 
 struct NgayThang { typedef struct { 
 unsigned char Ngay ; unsigned char Ngay ; 
 unsigned char Thang ; unsigned char Thang ; 
 unsigned int Nam ; 
 unsigned int Nam ; 
 } NgayThang ; 
 } ;

---

## TRANG 129
Lập_trình căn_bản 
 Thí_dụ 2 : Mỗi sinh_viên cần được quản_lý bởi các thông 
 tin : mã_số sinh_viên , họ tên , ngày_tháng năm sinh , giới_tính , địa 
 chỉ thường_trú . Lúc này ta có_thể khai_báo một struct gồm các 
 thông_tin trên . 
 struct SinhVien { typedef struct { 
 char MSSV [ 10 ] ; char MSSV [ 10 ] ; 
 char HoTen [ 40 ] ; char HoTen [ 40 ] ; 
 struct NgayThang NgaySinh ; NgayThang NgaySinh ; 
 int Phai ; int Phai ; 
 char DiaChi [ 40 ] ; char DiaChi [ 40 ] ; 
 } SinhVien ; 
 } ; 
 I. 3 Khai_báo biến cấu_trúc 
 Việc khai_báo biến cấu_trúc cũng tương_tự như khai_báo biến 
 thuộc kiểu dữ_liệu chuẩn . 
 Cú_pháp : 
 - Đối_với cấu_trúc được định_nghĩa theo cách 1 : 
 struct < Tên cấu_trúc > < Biến 1 > [ , < Biến 2 > … ] ; 
 - Đối_với các cấu_trúc được định_nghĩa theo cách 2 : 
 < Tên cấu_trúc > < Biến 1 > [ , < Biến 2 > … ] ; 
 Thí_dụ : Khai_báo biến NgaySinh có kiểu cấu_trúc 
 NgayThang ; biến SV có kiểu cấu_trúc SinhVien . 
 struct NgayThang NgaySinh ; NgayThang NgaySinh ; 
 struct SinhVien SV ; SinhVien SV ;

---

## TRANG 130
Lập_trình căn_bản 
 II. CÁC THAO_TÁC TRÊN BIẾN KIỂU CẤU_TRÚC 
 II. 1 Truy_xuất đến từng trường của biến cấu_trúc 
 Cú_pháp : < Biến cấu_trúc > . < Tên trường > 
 Khi sử_dụng cách truy_xuất theo kiểu này , các thao_tác trên 
 < Biến cấu_trúc > . < Tên trường > giống như các thao_tác trên các 
 biến của kiểu dữ_liệu của < Tên trường > . 
 Thí_dụ 1 : Viết chương_trình cho phép đọc dữ_liệu từ bàn 
 phím cho biến cấu_trúc SinhVien và hiển_thị biến cấu_trúc đó lên 
 màn_hình : 
 # include < conio . h > 
 # include < stdio . h > 
 # include < string . h > 
 typedef struct { 
 unsigned char Ngay ; 
 unsigned char Thang ; 
 unsigned int Nam ; 
 } NgayThang ; 
 typedef struct { 
 char MSSV [ 10 ] ; 
 char HoTen [ 40 ] ; 
 NgayThang NgaySinh ; 
 int Phai ; 
 char DiaChi [ 40 ] ; 
 } SinhVien ; 
 / / Hàm in lên màn_hình 1 mẩu tin SinhVien 
 void InSV ( SinhVien s ) { 
 printf ( " MSSV : | Ho va ten | Ngay_Sinh | 
 Dia chi \ n " ) ; 
 printf ( " % s | % s | % d - % d - % d | % s \ n " , 
 s . MSSV , s . HoTen , s . NgaySinh . Ngay , 
 s . NgaySinh . Thang , s . NgaySinh . Nam , s . DiaChi ) ; 
 } 
 main ( ) { 
 SinhVien SV , s ; 
 printf ( " Nhap MSSV : " ) ; gets ( SV. MSSV ) ; 
 printf ( " Nhap_Ho va ten : " ) ; gets ( SV. HoTen ) ; 
 printf ( " Sinh ngay : " ) ; 
 scanf ( " % d " , & SV. NgaySinh . Ngay ) ;

---

## TRANG 131
Lập_trình căn_bản 
 printf ( " Thang : " ) ; 
 scanf ( " % d " , & SV. NgaySinh . Thang ) ; 
 printf ( " Nam : " ) ; scanf ( " % d " , & SV. NgaySinh . Nam ) ; 
 printf ( " Gioi_tinh ( 0 : Nu ) , ( 1 : Nam ) : " ) ; 
 scanf ( " % d " , & SV. Phai ) ; 
 fflush ( stdin ) ; 
 printf ( " Dia chi : " ) ; gets ( SV. DiaChi ) ; 
 InSV ( SV ) ; 
 s = SV ; / / Gán_trị cho cấu_trúc s 
 InSV ( s ) ; 
 getch ( ) ; 
 } 
 Lưu_ý : 
 - Các biến cấu_trúc có_thể gán cho nhau . Thực_chất đây là 
 thao_tác trên toàn_bộ cấu_trúc không phải trên một trường riêng_rẽ 
 nào . Chương_trình trên dòng s = SV là một ví_dụ . 
 - Với các biến kiểu cấu_trúc ta không_thể thực_hiện được 
 các thao_tác sau đây : 
 o Sử_dụng các hàm_xuất nhập trên biến cấu_trúc . 
 o Các phép_toán quan_hệ , các phép_toán số_học và logic . 
 Thí_dụ 2 : Nhập vào hai số_phức và tính tổng của chúng . Ta 
 biết rằng số_phức là một cặp ( a , b ) trong đó a , b là các số_thực , a 
 gọi_là phần thực , b là phần ảo . ( Đôi_khi người_ta cũng viết số 
 phức dưới dạng a + ib trong đó i là một đơn_vị ảo có tính_chất 
 i2 = - 1 ) . Gọi số_phức c1 = ( a1 , b1 ) và c2 = ( a2 , b2 ) khi đó tổng của hai 
 số_phức c1 và c2 là một_số_phức c3 mà c3 = ( a1 + a2 , b1 + b2 ) . Với 
 hiểu_biết như vậy ta có_thể xem mỗi số_phức là một cấu_trúc có 
 hai trường , một trường biểu_diễn cho phần thực , một trường biểu 
 diễn cho phần ảo . Việc tính tổng của hai số_phức được tính bằng 
 cách lấy phần thực cộng với phần thực và phần ảo cộng với phần 
 ảo .

---

## TRANG 132
Lập_trình căn_bản 
 # include < conio . h > 
 # include < stdio . h > 
 # include < string . h > 
 typedef struct { 
 float Thuc ; 
 float Ao ; 
 } SoPhuc ; 
 / / Hàm in số_phức lên màn_hình 
 void InSoPhuc ( SoPhuc p ) { 
 printf ( " % . 2f + i % . 2f \ n " , p . Thuc , p . Ao ) ; 
 } 
 main ( ) { 
 SoPhuc p1 , p2 , p ; 
 printf ( " Nhap so phuc thu nhat : \ n " ) ; 
 printf ( " Phan_thuc : " ) ; 
 scanf ( " % f " , & p1 . Thuc ) ; 
 printf ( " Phan_ao : " ) ; scanf ( " % f " , & p1 . Ao ) ; 
 printf ( " Nhap so phuc thu hai : \ n " ) ; 
 printf ( " Phan_thuc : " ) ; 
 scanf ( " % f " , & p2 . Thuc ) ; 
 printf ( " Phan_ao : " ) ; scanf ( " % f " , & p2 . Ao ) ; 
 printf ( " So phuc thu nhat : " ) ; 
 InSoPhuc ( p1 ) ; 
 printf ( " So phuc thu hai : " ) ; 
 InSoPhuc ( p2 ) ; 
 p . Thuc = p1 . Thuc + p2 . Thuc ; 
 p . Ao = p1 . Ao + p2 . Ao ; 
 printf ( " Tong 2 so phuc : " ) ; 
 InSoPhuc ( p ) ; 
 getch ( ) ; 
 } 
 Kết_quả_thực_hiện chương_trình :

---

## TRANG 133
Lập_trình căn_bản 
 II. 2 Khởi tạo cấu_trúc 
 Việc khởi tạo cấu_trúc có_thể được thực_hiện trong lúc khai_báo 
 biến cấu_trúc . Các trường của cấu_trúc được khởi tạo được đặt 
 giữa 2 dấu { và } , chúng được phân_cách nhau bởi dấu_phẩy ( , ) . 
 Thí_dụ : Khởi tạo biến cấu_trúc NgaySinh : 
 struct NgayThang NgaySinh = { 29 , 8 , 1986 } ; 
 III. CON_TRỎ CẤU_TRÚC 
 III. 1 Khai_báo 
 Việc khai_báo một biến con_trỏ kiểu cấu_trúc cũng tương_tự như 
 khi khai_báo một biến con_trỏ khác , nghĩa_là đặt thêm dấu * vào 
 phía trước tên biến . 
 Cú_pháp : struct < Tên cấu_trúc > * < Tên biến con_trỏ > ; 
 Thí_dụ : Ta có_thể khai_báo một con_trỏ cấu_trúc kiểu 
 NgayThang như sau : 
 struct NgayThang * p ; 
 hay NgayThang * p ; / / Nếu có định_nghĩa kiểu 
 III. 2 Sử_dụng các con_trỏ kiểu cấu_trúc 
 Khi khai_báo biến con_trỏ cấu_trúc , biến con_trỏ chưa chỉ đến 1 
 địa_chỉ cụ_thể . Lúc này nó chỉ mới được cấp_phát 2 byte để lưu 
 giữ địa_chỉ và được ghi_nhận là con_trỏ chỉ đến 1 cấu_trúc , nhưng 
 chưa chỉ đến 1 đối_tượng rõ_ràng . Muốn thao_tác trên con_trỏ_cấu 
 trúc hợp_lệ , cũng tương_tự như các con_trỏ khác , ta phải : 
 - Cấp_phát một vùng nhớ cho nó ( sử_dụng hàm malloc ( ) 
 hay calloc ( ) ) 
 - Hoặc , cho nó quản_lý địa_chỉ của một biến cấu_trúc nào 
 đó . 
 Thí_dụ : Sau khi khởi tạo giá_trị của cấu_trúc : 
 struct NgayThang Ngay = { 29,8,1986 } ; 
 p = & Ngay ; 
 lúc này biến con_trỏ p đã chứa địa_chỉ của Ngay .

---

## TRANG 134
Lập_trình căn_bản 
 III. 2 Truy_cập các thành_phần của cấu_trúc đang được quản 
 lý bởi con_trỏ 
 Để truy_cập đến từng trường của 1 cấu_trúc thông_qua con_trỏ của 
 nó , ta sử_dụng toán_tử dấu mũi_tên ( -> : dấu - và dấu > ) . 
 Ngoài_ra , ta vẫn có_thể sử_dụng đến phép_toán * để truy_cập vùng 
 dữ_liệu đang được quản_lý bởi con_trỏ cấu_trúc để lấy thông_tin 
 cần_thiết . 
 Thí_dụ : Sử_dụng con_trỏ cấu_trúc . 
 # include < conio . h > 
 # include < stdio . h > 
 typedef struct { 
 unsigned char Ngay ; 
 unsigned char Thang ; 
 unsigned int Nam ; 
 } NgayThang ; 
 main ( ) { 
 NgayThang Ng = { 29,8,1986 } ; 
 NgayThang * p ; 
 p = & Ng ; 
 printf ( " Truy_cap binh thuong % d - % d - % d \ n " , 
 Ng . Ngay , Ng . Thang , Ng . Nam ) ; 
 printf ( " Truy cap qua con tro % d - % d - % d \ n " , 
 p -> Ngay , p -> Thang , p -> Nam ) ; 
 printf ( " Truy cap qua vung nho con tro 
 % d - % d - % d \ n " , ( * p ) . Ngay , ( * p ) . Thang , ( * p ) . Nam ) ; 
 getch ( ) ; 
 } 
 Kết_quả :

---

## TRANG 135
Lập_trình căn_bản 
 IV. BÀI_TẬP 
 1 . Hãy định_nghĩa kiểu : 
 struct Hoso { 
 char HoTen [ 40 ] ; 
 float Diem ; 
 char Loai [ 10 ] ; 
 } ; 
 Viết chương_trình nhập vào họ tên , điểm của n học_sinh . 
 Xếp loại văn_hóa theo cách sau : 
 Điểm Xếp_loại 
 > = 9.0 Xuat_sac 
 8.0 - < 9.0 Gioi 
 7.0 - < 8.0 Khá 
 5.0 - < 7.0 Trung_bình 
 < 5.0 Không_đạt 
 Hiển_thị danh_sách lên màn_hình theo dạng sau ( thứ_tự 
 giảm dần theo điểm trung_bình ) : 
 XEP LOAI VAN HOA 
 HO VA TEN DIEM XEP LOAI 
 Nguyen_Van A 7.0 Kha 
 Ho_Thi B 5.0 Trung_binh 
 Dang Kim C 4.0 Khong dat . Xem một phân_số là một cấu_trúc có hai trường là tử_số và mẫu 
 số . Hãy viết chương_trình thực_hiện các phép_toán cộng , trừ , 
 nhân , chia hai phân_số . ( Các kết_quả phải tối_giản ) . 
 3 . Tạo một danh_sách cán_bộ công_nhân_viên , mỗi người_người 
 xem như một cấu_trúc bao_gồm các trường Ho , Ten , Luong , Tuoi , 
 Diachi . Nhập một_số người vào danh_sách , sắp_xếp tên theo thứ 
 tự từ_điển , in danh_sách đã sắp_xếp theo mẫu sau : 
 DANH SACH CAN BO CONG NHAN VIEN 
 STT HO VA TEN LUONG TUOI DIACHI 
 1 Nguyen_Van A 333.00 26 Can_Tho 
 2 Dang Kim B 290.00 23 Vinh_Long

---

## TRANG 136
Lập_trình căn_bản 
 Chương 10 
 TẬP_TIN 
 Các vấn_đề được trình_bày trong chương này : 
  Các khái_niệm liên_quan đến tập_tin . 
  Các bước thao_tác với tập_tin . 
  Một_số hàm truy_xuất tập_tin văn_bản . 
  Một_số hàm truy_xuất tập_tin nhị_phân . 
 I. MỘT_SỐ KHÁI_NIỆM VỀ TẬP_TIN 
 Đối_với các kiểu dữ_liệu ta đã biết như kiểu số , kiểu mảng , kiểu 
 cấu_trúc thì dữ_liệu được tổ_chức trong bộ_nhớ trong ( RAM ) của 
 máy_tính nên khi kết_thúc việc thực_hiện chương_trình thì dữ_liệu 
 cũng bị mất ; khi cần chúng_ta bắt_buộc phải nhập lại từ bàn_phím . 
 Điều đó vừa mất thời_gian vừa không giải_quyết được các bài 
 toán với số_liệu lớn . Để giải_quyết vấn_đề , người_ta đưa ra kiểu 
 tập_tin ( file ) cho phép lưu_trữ dữ_liệu ở bộ_nhớ_ngoài ( đĩa ) . Khi 
 kết_thúc chương_trình thì dữ_liệu vẫn còn do đó chúng_ta có_thể sử 
_dụng nhiều lần . Một đặc_điểm khác của kiểu tập_tin là kích_thước 
 lớn với số_lượng các phần_tử không hạn_chế ( chỉ bị hạn_chế bởi 
 dung_lượng của bộ_nhớ_ngoài ) . 
 Có 2 loại dữ_liệu kiểu tập_tin : 
  Tập_tin văn_bản ( Text_File ) : là loại tập_tin_dùng để ghi các 
 ký_tự lên đĩa . Điểm đặc_biệt là dữ_liệu của tập_tin được lưu_trữ 
 thành các dòng , mỗi dòng được kết_thúc bằng ký_tự xuống dòng 
 ( new line ) , ký_hiệu ‘ \ n ’ ; ký_tự này là sự kết_hợp của 2 ký_tự CR 
 ( Carriage_Return - Về đầu dòng , mã Ascii là 13 ) và LF ( Line 
 Feed - Xuống dòng , mã Ascii là 10 ) . Mỗi tập_tin được kết_thúc 
 bởi ký_tự EOF ( End Of_File ) có mã Ascii là 26 ( xác_định bởi tổ 
 hợp phím Ctrl + Z ) . 
 Tập_tin văn_bản chỉ có_thể truy_xuất theo kiểu tuần_tự .

---

## TRANG 137
Lập_trình căn_bản 
  Tập_tin nhị_phân : là loại tập_tin chứa 1 dãy liên_tục các 
 byte ( mã Ascii của các ký_tự ) . Tập_tin nhị_phân có 2 loại : 
 o Tập_tin định kiểu ( Typed_File ) : là loại tập_tin bao_gồm 
 nhiều phần_tử có cùng kiểu : char , int , long , cấu_trúc … và 
 được lưu_trữ trên đĩa dưới dạng một chuỗi các byte_liên 
 tục . 
 o Tập_tin không định kiểu ( Untyped_File ) : là loại tập_tin 
 mà dữ_liệu của chúng gồm các cấu_trúc dữ_liệu mà người 
 ta không quan_tâm đến nội_dung hoặc kiểu của nó , chỉ lưu 
 ý đến các yếu_tố vật_lý của tập_tin như độ lớn và các yếu 
 tố tác_động lên tập_tin mà thôi . 
 Biến tập_tin : là một biến thuộc kiểu dữ_liệu tập_tin_dùng để đại 
 diện cho một tập_tin . Dữ_liệu chứa trong một tập_tin được truy 
 xuất qua các thao_tác với thông_số là biến tập_tin đại_diện cho tập 
 tin đó . 
 Con_trỏ tập_tin : Khi một tập_tin được mở ra để làm_việc , tại mỗi 
 thời_điểm , sẽ có một vị_trí của tập_tin mà tại đó việc đọc / ghi 
 thông_tin sẽ xảy ra . Người_ta hình_dung có một con_trỏ đang chỉ 
 đến vị_trí đó và đặt tên nó là con_trỏ tập_tin . 
 Sau khi đọc / ghi xong dữ_liệu , con_trỏ sẽ chuyển_dịch thêm một 
 phần_tử về phía cuối tập_tin . Sau phần_tử dữ_liệu cuối_cùng của 
 tập_tin là dấu kết_thúc tập_tin EOF ( End Of_File ) . 
 II. CÁC THAO_TÁC TRÊN TẬP_TIN 
 Muốn thao_tác trên tập_tin , ta phải lần_lượt làm theo các bước : 
  Khai_báo biến tập_tin . 
  Mở tập_tin bằng hàm fopen ( ) . 
  Thực_hiện các thao_tác xử_lý dữ_liệu của tập_tin bằng các 
 hàm đọc / ghi dữ_liệu . 
  Đóng tập_tin bằng hàm fclose ( ) . 
 Lưu_ý : Các thao_tác liên_quan đến tập_tin sử_dụng các hàm 
 trong thư_viện stdio . h .

---

## TRANG 138
Lập_trình căn_bản 
 II. 1 . Khai_báo biến tập_tin 
 Cú_pháp : FILE < Danh_sách các biến con_trỏ > 
 Các biến trong danh_sách phải là các con_trỏ và được phân 
 cách bởi dấu_phẩy ( , ) . 
 Thí_dụ : FILE * f1 , * f2 ; 
 II. 2 . Mở tập_tin 
 Cú_pháp : FILE * fopen ( char * Path , const char * Mode ) 
 Trong đó : 
 - Path : chuỗi chỉ đường_dẫn đến tập_tin trên đĩa . 
 - Type : chuỗi xác_định cách_thức mà tập_tin sẽ mở . Các giá 
 trị có_thể của Mode :

| Chế độ | Ý nghĩa |
| --- | --- |
| r | Mở tập tin văn bản để đọc |
| w | Tạo ra tập tin văn bản mới để ghi |
| a | Nối vào tập tin văn bản |
| rb | Mở tập tin nhị phân để đọc |
| wb | Tạo ra tập tin nhị phân để ghi |
| ab | Nối vào tập tin nhị phân |
| r+ | Mở một tập tin văn bản để đọc/ghi |
| w+ | Tạo ra tập tin văn bản để đọc ghi |
| a+ | Nối vào hay tạo mới tập tin văn bản để đọc/ghi |
| r+b | Mở ra tập tin nhị phân để đọc/ghi |
| w+b | Tạo ra tập tin nhị phân để đọc/ghi |
| a+b | Nối vào hay tạo mới tập tin nhị phân |


- Hàm_fopen trả về một con_trỏ tập_tin . Chương_trình của 
 ta không_thể thay_đổi giá_trị của con_trỏ này . Nếu có một lỗi_xuất 
 hiện trong khi mở tập_tin thì hàm này trả về con_trỏ NULL. 
 Thí_dụ : Mở một tập_tin tên TEST. txt để ghi . 
 FILE * f ; 
 f = fopen ( “ TEST. txt ” , “ w ” ) ; 
 if ( f ! = NULL ) 
 { 
 / / Các câu_lệnh để thao_tác với tập_tin 
 / / Đóng tập_tin 
 }

---

## TRANG 139
Lập_trình căn_bản 
 Trong thí_dụ trên , ta có sử_dụng câu_lệnh kiểm_tra điều 
 kiện để xác_định mở tập_tin có thành_công hay không ? . 
 Nếu mở tập_tin để ghi , nếu tập_tin đã tồn_tại rồi thì tập_tin 
 sẽ bị xóa và một tập_tin mới được tạo ra . Nếu ta muốn ghi nối dữ 
 liệu , ta phải sử_dụng chế_độ “ a ” . Khi mở với chế_độ đọc , tập_tin 
 phải tồn_tại rồi , nếu không một lỗi sẽ xuất_hiện . 
 II. 3 . Đóng tập_tin 
 Hàm_fclose ( ) được dùng để đóng tập_tin được mở bởi hàm 
 fopen ( ) . Hàm này sẽ ghi dữ_liệu còn lại trong vùng_đệm vào tập 
 tin và đóng lại tập_tin . 
 Cú_pháp : int fclose ( FILE * f ) 
 Trong đó f là con_trỏ tập_tin được mở bởi hàm fopen ( ) . Giá 
 trị trả về của hàm là 0 báo rằng việc đóng tập_tin thành_công . 
 Hàm trả về EOF nếu có xuất_hiện lỗi . 
 II. 4 . Kiểm_tra đến cuối tập_tin hay chưa ? 
 Cú_pháp : int feof ( FILE * f ) 
 Ý_nghĩa : Kiểm_tra xem đã chạm tới cuối tập_tin hay chưa 
 và trả về EOF nếu cuối tập_tin được chạm tới , ngược_lại trả về 0 . 
 II. 5 Di_chuyển con_trỏ tập_tin về đầu tập_tin - Hàm_rewind ( ) 
 Khi ta đang thao_tác một tập_tin đang mở , con_trỏ tập_tin luôn_di 
 chuyển về phía cuối tập_tin . Muốn cho con_trỏ quay về đầu tập_tin 
 như khi mở nó , ta sử_dụng hàm rewind ( ) . 
 Cú_pháp : void rewind ( FILE * f ) 
 III. TRUY_CẬP TẬP_TIN VĂN_BẢN 
 III. 1 . Ghi dữ_liệu lên tập_tin văn_bản 
 III. 1.1 Hàm_putc ( ) : Hàm này được dùng để ghi một ký_tự lên một 
 tập_tin văn_bản đang được mở để làm_việc . 
 Cú_pháp : int putc ( int c , FILE * f ) 
 Trong đó , tham_số c chứa mã Ascii của một ký_tự nào đó . 
 Mã này được ghi lên tập_tin liên_kết với con_trỏ f . Hàm này trả về 
 EOF nếu gặp lỗi .

---

## TRANG 140
Lập_trình căn_bản 
 III. 1.2 Hàm_fputs ( ) : Hàm này dùng để ghi một chuỗi ký_tự chứa 
 trong vùng_đệm lên tập_tin văn_bản . 
 Cú_pháp : int puts ( const char * buffer , FILE * f ) 
 Trong đó , buffer là con_trỏ có kiểu char chỉ đến vị_trí đầu 
 tiên của chuỗi ký_tự được ghi vào . Hàm này trả về giá_trị 0 nếu 
 buffer chứa chuỗi rỗng và trả về EOF nếu gặp lỗi . 
 III. 1.3 Hàm_fprintf ( ) : Hàm này dùng để ghi dữ_liệu có định_dạng 
 lên tập_tin văn_bản . 
 Cú_pháp : void fprintf ( FILE * f , const char * format , varexpr ) 
 Trong đó : format : chuỗi định_dạng ( giống với các định 
 dạng của hàm printf ( ) ) , varexpr : danh_sách các biểu_thức , mỗi 
 biểu_thức cách nhau dấu_phẩy ( , ) . 
 Thí_dụ : Viết chương_trình ghi chuỗi ký_tự lên tập_tin văn 
 bản D : \ \ Baihat . txt 
 # include < stdio . h > 
 # include < conio . h > 
 main ( ) { 
 FILE * f ; 
 f = fopen ( " D : \ \ Baihat . txt " , " r + " ) ; 
 if ( f ! = NULL ) 
 { 
 fputs ( " Em oi Ha_Noi pho . \ n " , f ) ; 
 fputs ( " Ta con_em , mui hoang lan ; ta con_em , 
 mui hoa sua . " , f ) ; 
 fclose ( f ) ; 
 } 
 getch ( ) ; 
 } 
 Nội_dung tập_tin Baihat . txt khi được mở bằng trình soạn_thảo 
 văn_bản Notepad .

---

## TRANG 141
Lập_trình căn_bản 
 III. 2 . Đọc dữ_liệu từ tập_tin văn_bản 
 III. 2.1 Hàm_getc ( ) : Hàm này dùng để đọc dữ_liệu từ tập_tin văn 
 bản đang được mở để làm_việc . 
 Cú_pháp : int getc ( FILE * f ) 
 Hàm này trả về mã Ascii của một ký_tự nào đó ( kể_cả 
 EOF ) trong tập_tin liên_kết với con_trỏ f . 
 III. 2.2 Hàm_fgets ( ) 
 Cú_pháp : char * fgets ( char * buffer , int n , FILE * f ) 
 Hàm này được dùng để đọc một chuỗi ký_tự từ tập_tin văn 
 bản đang được mở ra và liên_kết với con_trỏ f cho đến khi đọc đủ 
 n ký_tự hoặc gặp ký_tự xuống dòng ‘ \ n ’ ( ký_tự này cũng được đưa 
 vào chuỗi kết_quả ) hay gặp ký_tự kết_thúc EOF ( ký_tự này không 
 được đưa vào chuỗi kết_quả ) . 
 Trong đó : 
 - buffer ( vùng_đệm ) : con_trỏ có kiểu char chỉ đến cùng nhớ 
 đủ lớn chứa các ký_tự nhận được . 
 - n : giá_trị nguyên chỉ độ dài lớn nhất của chuỗi ký_tự nhận 
 được . 
 - f : con_trỏ liên_kết với một tập_tin nào đó . 
 - Ký_tự NULL ( ‘ \ 0 ’ ) tự_động được thêm vào cuối chuỗi_kết 
 quả lưu trong vùng đêm . 
 - Hàm trả về địa_chỉ đầu_tiên của vùng_đệm khi không gặp 
 lỗi và chưa gặp ký_tự kết_thúc EOF. Ngược_lại , hàm trả về giá_trị 
 NULL. 
 III. 2.3 Hàm_fscanf ( ) : Hàm này dùng để đọc dữ_liệu từ tập_tin văn 
 bản vào danh_sách các biến theo định_dạng . 
 Cú_pháp : void fscanf ( FILE * f , const char * format , pointers ) 
 Trong đó : format : chuỗi định_dạng ( giống hàm scanf ( ) ) ; 
 pointers : danh_sách địa_chỉ các biến mỗi biến_cách nhau dấu_phẩy 
 ( , ) .

---

## TRANG 142
Lập_trình căn_bản 
 Thí_dụ : Viết chương_trình chép tập_tin D : \ Baihat . txt ở trên 
 sang tập_tin D : \ Baica . txt . 
 # include < stdio . h > 
 # include < conio . h > 
 main ( ) { 
 FILE * f1 , * f2 ; 
 f1 = fopen ( " D : \ \ Baihat . txt " , " rt " ) ; 
 f2 = fopen ( " D : \ \ Baica . txt " , " wt " ) ; 
 if ( f1 ! = NULL & & f2 ! = NULL ) 
 { 
 int ch = fgetc ( f1 ) ; 
 while ( ! feof ( f1 ) ) 
 { 
 fputc ( ch , f2 ) ; 
 ch = fgetc ( f1 ) ; 
 } 
 fclose ( f1 ) ; 
 fclose ( f2 ) ; 
 } 
 getch ( ) ; 
 } 
 IV. TRUY_CẬP TẬP_TIN NHỊ_PHÂN 
 IV. 1 Ghi dữ_liệu lên tập_tin nhị_phân - Hàm_fwrite ( ) 
 Cú_pháp : 
 size_t fwrite ( const void * ptr , size_t size , size_t n , FILE * f ) 
 Trong đó : 
 - ptr : con_trỏ chỉ đến vùng nhớ chứa thông_tin cần ghi lên 
 tập_tin . 
 - n : số phần_tử sẽ ghi lên tập_tin . 
 - size : kích_thước của mỗi phần_tử . 
 - f : con_trỏ tập_tin đã được mở . 
 - Giá_trị trả về của hàm này là số phần_tử được ghi lên tập 
 tin . Giá_trị này bằng n trừ khi xuất_hiện lỗi . 
 IV. 2 Đọc dữ_liệu từ tập_tin nhị_phân - Hàm_fread ( ) 
 Cú_pháp : 
 size_t fread ( const void * ptr , size_t size , size_t n , FILE * f )

---

## TRANG 143
Lập_trình căn_bản 
 Trong đó : 
 - ptr : con_trỏ chỉ đến vùng nhớ sẽ nhận dữ_liệu từ tập_tin . 
 - n : số phần_tử được đọc từ tập_tin . 
 - size : kích_thước của mỗi phần_tử . 
 - f : con_trỏ tập_tin đã được mở . 
 - Giá_trị trả về của hàm này là số phần_tử đã đọc được từ 
 tập_tin . Giá_trị này bằng n hay nhỏ hơn n nếu đã chạm đến cuối 
 tập_tin hoặc có lỗi xuất_hiện . . 
 IV. 3 Di_chuyển con_trỏ tập_tin - Hàm_fseek ( ) 
 Việc ghi hay đọc dữ_liệu từ tập_tin sẽ làm cho con_trỏ tập_tin dịch 
 chuyển một_số byte , đây chính là kích_thước của kiểu dữ_liệu của 
 mỗi phần_tử của tập_tin . 
 Khi đóng tập_tin rồi mở lại nó , con_trỏ luôn ở vị_trí ngay đầu tập 
 tin . Nhưng nếu ta sử_dụng kiểu mở tập_tin là “ a ” để ghi nối dữ 
 liệu , con_trỏ tập_tin sẽ di_chuyển đến vị_trí cuối_cùng của tập_tin 
 này . 
 Ta cũng có_thể điều_khiển việc di_chuyển con_trỏ tập_tin đến vị_trí 
 chỉ_định bằng hàm fseek ( ) . 
 Cú_pháp : int fseek ( FILE * f , long offset , int whence ) 
 Trong đó : 
 - f : con_trỏ tập_tin đang thao_tác . 
 - offset : số byte cần dịch_chuyển con_trỏ tập_tin kể từ_vị 
 trí trước đó . Phần_tử đầu_tiên là vị_trí 0 . 
 - whence : vị_trí bắt_đầu để tính offset , ta có_thể chọn 
 điểm xuất_phát là :

| 0 | SEEK_SET | Vị trí đầu tập tin |
| --- | --- | --- |
| 1 | SEEK_CUR | Vị trí hiện tại của con trỏ tập tin |
| 2 | SEEK_END | Vị trí cuối tập tin |


- Kết_quả trả về của hàm là 0 nếu việc di_chuyển thành 
 công . Nếu không thành_công , 1 giá_trị khác 0 ( đó là 1 
 mã lỗi ) được trả về .

---

## TRANG 144
Lập_trình căn_bản 
 IV. 3 Thí_dụ 
 Thí_dụ 1 : Viết chương_trình ghi lên tập_tin CacSo . Dat 3 giá 
 trị_số ( thực , nguyên , nguyên dài ) . Sau đó đọc các số từ tập_tin vừa 
 ghi và hiển_thị lên màn_hình . 
 # include < stdio . h > 
 # include < conio . h > 
 main ( ) { 
 FILE * f ; 
 f = fopen ( " D : \ \ CacSo . txt " , " wb " ) ; 
 if ( f ! = NULL ) 
 { 
 double d = 3.14 ; 
 int i = 101 ; 
 long l = 54321 ; 
 fwrite ( & d , sizeof ( double ) , 1 , f ) ; 
 fwrite ( & i , sizeof ( int ) , 1 , f ) ; 
 fwrite ( & l , sizeof ( long ) , 1 , f ) ; 
 / / Doc tu tap tin 
 rewind ( f ) ; 
 fread ( & d , sizeof ( double ) , 1 , f ) ; 
 fread ( & i , sizeof ( int ) , 1 , f ) ; 
 fread ( & l , sizeof ( long ) , 1 , f ) ; 
 printf ( " Cac ket qua la : % f % d % ld " , 
 d , i , l ) ; 
 fclose ( f ) ; 
 } 
 getch ( ) ; 
 } 
 Thí_dụ 2 : Mỗi sinh_viên cần quản_lý ít_nhất 2 thông_tin : mã 
 sinh_viên và họ tên . Viết chương_trình cho phép lựa_chọn các 
 chức_năng : nhập danh_sách sinh_viên từ bàn_phím rồi ghi lên tập 
 tin SinhVien . dat , đọc dữ_liệu từ tập_tin SinhVien . dat rồi hiển_thị 
 danh_sách lên màn_hình , tìm_kiếm họ tên của một sinh_viên nào 
 đó dựa vào mã sinh_viên nhập từ bàn_phím . 
 Ta nhận thấy rằng mỗi phần_tử của tập_tin SinhVien . Dat là 
 một cấu_trúc có 2 trường : mã và họ tên . Do đó , ta cần khai_báo 
 cấu_trúc này và sử_dụng các hàm đọc / ghi tập_tin nhị_phân với kích 
 thước mỗi phần_tử của tập_tin là chính kích_thước cấu_trúc đó .

---

## TRANG 145
Lập_trình căn_bản 
 # include < stdio . h > 
 # include < conio . h > 
 # include < string . h > 
 typedef struct { 
 char Ma [ 10 ] ; 
 char HoTen [ 40 ] ; 
 } SinhVien ; 
 void WriteFile ( char * FileName ) { 
 FILE * f ; 
 int n , i ; 
 SinhVien sv ; 
 f = fopen ( FileName , " ab " ) ; 
 if ( f = = NULL ) return ; 
 printf ( " Nhap bao nhieu sinh vien ? " ) ; 
 scanf ( " % d " , & n ) ; 
 fflush ( stdin ) ; 
 for ( i = 1 ; i < = n ; i + + ) { 
 printf ( " Sinh vien thu % i \ n " , i ) ; 
 printf ( " - MSSV : " ) ; gets ( sv . Ma ) ; 
 printf ( " - Ho_ten : " ) ; gets ( sv . HoTen ) ; 
 fwrite ( & sv , sizeof ( sv ) , 1 , f ) ; 
 fflush ( stdin ) ; 
 } 
 fclose ( f ) ; 
 printf ( " Bam phim bat ky de tiep tuc " ) ; 
 getch ( ) ; 
 } 
 void ReadFile ( char * FileName ) { 
 FILE * f ; 
 SinhVien sv ; 
 f = fopen ( FileName , " rb " ) ; 
 if ( f = = NULL ) return ; 
 printf ( " MSSV | Ho va ten \ n " ) ; 
 fread ( & sv , sizeof ( sv ) , 1 , f ) ; 
 while ( ! feof ( f ) ) { 
 printf ( " % s | % s \ n " , 
 sv . Ma , sv . HoTen ) ; 
 fread ( & sv , sizeof ( sv ) , 1 , f ) ; 
 } 
 fclose ( f ) ; 
 printf ( " Bam phim bat ky de tiep tuc ! ! ! " ) ; 
 getch ( ) ; 
 }

---

## TRANG 146
Lập_trình căn_bản 
 void Search ( char * FileName ) { 
 char MSSV [ 10 ] ; 
 FILE * f ; 
 int Found ; 
 SinhVien sv ; 
 fflush ( stdin ) ; 
 printf ( " Ma so sinh vien can tim : " ) ; 
 gets ( MSSV ) ; 
 Found = 0 ; 
 f = fopen ( FileName , " rb " ) ; 
 if ( f = = NULL ) return ; 
 while ( ! feof ( f ) & & Found = = 0 ) { 
 fread ( & sv , sizeof ( sv ) , 1 , f ) ; 
 if ( strcmp ( sv . Ma , MSSV ) = = 0 ) Found = 1 ; 
 } 
 fclose ( f ) ; 
 if ( Found = = 1 ) 
 printf ( " Tim thay SV co ma % s . Ho ten la : % s " , 
 sv . Ma , sv . HoTen ) ; 
 else 
 printf ( " Tim khong thay sinh vien co ma % s " , 
 MSSV ) ; 
 printf ( " \ nBam phim bat ky de tiep tuc ! ! ! " ) ; 
 getch ( ) ; 
 } 
 main ( ) { 
 int c ; 
 for ( ; ; ) { 
 printf ( " 1 . Nhap DSSV \ n " ) ; 
 printf ( " 2 . In DSSV \ n " ) ; 
 printf ( " 3 . Tim kiem \ n " ) ; 
 printf ( " 4 . Thoat \ n " ) ; 
 printf ( " Ban chon 1 , 2 , 3 , 4 : " ) ; 
 scanf ( " % d " , & c ) ; 
 if ( c = = 1 ) 
 WriteFile ( " d : \ \ SinhVien . Dat " ) ; 
 else if ( c = = 2 ) 
 ReadFile ( " d : \ \ SinhVien . Dat " ) ; 
 else if ( c = = 3 ) 
 Search ( " d : \ \ SinhVien . Dat " ) ; 
 else break ; 
 } 
 }

---

## TRANG 147
Lập_trình căn_bản 
 V. BÀI_TẬP 
 1 . Viết chương_trình quản_lý một tập_tin văn_bản theo các yêu 
 cầu : 
 - Nhập từ bàn_phím nội_dung một văn_bản sau đó ghi vào 
 đĩa . 
 - Đọc từ đĩa nội_dung văn_bản vừa nhập và in lên màn 
 hình . 
 - Đọc từ đĩa nội_dung văn_bản vừa nhập , in nội_dung đó 
 lên màn_hình và cho phép nối thêm thông_tin vào cuối tập_tin đó . 
 2 . Viết chương_trình cho phép thống_kê số lần xuất_hiện của các 
 ký_tự là chữ ( ‘ A ’ . . ’ Z ’ , ’ a ’ . . ’ z ’ ) trong một tập_tin văn_bản . 
 3 . Viết chương_trình đếm số từ và số dòng trong một tập_tin văn 
 bản . 
 4 . Viết chương_trình nhập từ bàn_phím và ghi vào 1 tập_tin tên là 
 DMHH. DAT với mỗi phần_tử của tập_tin là 1 cấu_trúc bao_gồm 
 các trường : Ma ( mã hàng : char [ 5 ] ) , Ten ( Tên hàng : char [ 20 ] ) . Kết 
 thúc việc nhập bằng cách gõ ENTER vào Ma . Ta sẽ dùng tập_tin 
 này để giải_mã hàng_hóa cho tập_tin DSHH. DAT sẽ đề_cập trong 
 bài 5 . 
 5 . Viết chương_trình cho phép nhập từ bàn_phím và ghi vào 1 tập 
 tin tên DSHH. Dat với mỗi phần_tử của tập_tin là một cấu_trúc bao 
 gồm các trường : mh ( mã hàng : char [ 5 ] ) , sl ( số_lượng : int ) , dg ( 
 đơn_giá : float ) , st ( Số tiền : float ) theo yêu_cầu : 
 - Mỗi lần nhập một cấu_trúc 
 - Trước_tiên nhập mã hàng ( mh ) , đưa mh so_sánh với Ma 
 trong tập_tin DMHH. DAT đã được tạo ra bởi bài_tập 4 , nếu 
 mh = ma thì in tên hàng ngay bên cạnh mã hàng . 
 - Nhập số_lượng ( sl ) . 
 - Nhập đơn_giá ( dg ) . 
 - Tính số tiền = số_lượng * đơn_giá . 
 Kết_thúc việc nhập bằng cách đánh ENTER vào mã hàng . 
 Sau khi nhập xong yêu_cầu in toàn_bộ danh_sách hàng_hóa có sự 
 giải_mã về tên hàng theo mẫu sau :

---

## TRANG 148
Lập_trình căn_bản

| STT | MA HANG | TEN HANG | SOLG | DON GIA | SO TIEN |
| --- | --- | --- | --- | --- | --- |
| 1 2 | a0101 b0101 | Duong cat trang Sua co gai Ha Lan | 25 10 | 10000.00 40000.00 | 250000.00 400000.00 |



---

## TRANG 149
Lập_trình căn_bản 
 TÀI_LIỆU THAM_KHẢO 
 [ 1 ] Nguyễn_Văn_Linh , Giáo_trình Tin_Học Đại_Cương A , Khoa 
 Công_Nghệ_Thông_Tin , Đại_học Cần_Thơ , 1991 . 
 [ 2 ] Nguyễn_Đình_Tê , Hoàng_Đức_Hải , Giáo_trình lý_thuyết và bài 
_tập ngôn_ngữ C ; Nhà xuất_bản Giáo_dục , 1999 . 
 [ 3 ] Nguyễn_Cẩn , C – Tham_khảo toàn_diện , Nhà xuất_bản Đồng 
 Nai , 1996 . 
 [ 4 ] Võ_Văn_Viện , Giúp tự học Lập_Trình_với ngôn_ngữ C , Nhà 
 xuất_bản Đồng_Nai , 2002 . 
 [ 5 ] Brain W. Kernighan & Dennis_Ritchie , The C_Programming 
 Language , Prentice Hall_Publisher , 1988 . 
 [ 6 ] Trần_Đức_Huyên , Phương_pháp giải các bài_toán trong Tin_học , 
 Nhà xuất_bản Giáo_dục , 2003 .

---

