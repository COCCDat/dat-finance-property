# Loại đầu mối đã trả ở những lượt trước

## Chuẩn bị lịch sử trước khi tìm

1. Đọc toàn bộ [state/seen-leads.json](../state/seen-leads.json) của skill, lịch sử kết quả đang thấy trong hội thoại và danh sách loại trừ người dùng đã cung cấp. Đây là lịch sử **đã trình bày**, không phải danh sách đã liên hệ hay danh sách số đã xác minh.
2. Nếu người dùng nhắc lượt cũ chưa có trong sổ hoặc bắt đầu phiên khác, dùng Personal Context theo skill/công cụ sẵn có để tìm đúng các kết quả tìm **khách mua BĐS và môi giới kết nối chủ xây** đã gửi. Chỉ tìm file lịch sử cụ thể khi đã biết có file phù hợp. Không đưa danh sách người bán trong sourcing/định giá so sánh, danh bạ không liên quan hoặc cơ sở dữ liệu rò rỉ vào sổ này.
3. Bổ sung khóa lịch sử khôi phục được trước khi lọc. Giữ nguồn gốc thông tin và phần chưa rõ; không bịa URL rút gọn, số thiếu, ngày trả hoặc danh tính. Lịch sử có nguồn từ kết quả cũ không làm số/nhu cầu trở thành đã xác minh.
4. Không có quyền đọc hoặc không khôi phục hết lịch sử: vẫn loại theo phần đã có, nêu ngắn “Đã đối chiếu sổ đã trả và lịch sử đọc được; chưa xác nhận bao phủ toàn bộ các phiên cũ”. Không giả định sổ trống đồng nghĩa chưa từng trả khách; không tuyên bố chống trùng tuyệt đối. Nếu sổ mất/hỏng, không ghi đè trắng; khôi phục từ phiên bản đã lưu hoặc kết quả cũ.

## Khóa đối chiếu

- **Số đầy đủ:** bỏ khoảng trắng/chấm/gạch/ký tự phân cách; quy `+84`, `0084`, `84` về `0` khi cấu trúc số Việt Nam rõ. So tập tất cả số liên hệ công khai thuộc cùng chủ thể đã biết. Không hoàn thiện số bị che. Số chỉ thấy trong snippet giữ trạng thái chưa xác minh.
- **Bài gốc:** đối chiếu mã bài/URL nội dung. Bỏ `utm_*`, `fbclid`, mảnh `#` không định danh nội dung; giữ tham số định danh như Facebook `story_fbid`, `id` và mã bình luận khi cần. Nhận diện URL Facebook bài dài/rút gọn theo cùng mã bài, TikTok theo mã video, tin BĐS theo mã tin cùng nền tảng. Link danh mục/tìm kiếm chung không phải khóa bài duy nhất.
- **Tài khoản/hồ sơ:** dùng URL/ID hồ sơ, trang doanh nghiệp hoặc quan hệ chủ thể đã xác minh. Tên hiển thị giống nhau không đủ. Cùng tài khoản công khai xác định rõ vẫn là một đầu mối dù đổi số.
- **Đơn vị/hotline:** cùng đơn vị và hotline chung là một đầu mối, không tách mỗi nhân viên/bài thành khách mới. Chỉ thêm bí danh/số khác khi có nguồn chứng minh cùng chủ thể.
- **Nội dung:** tin đăng lại có cùng người liên hệ, cùng nhu cầu/nguồn gốc là trùng dù đổi URL/nền tảng. Cùng khu vực/ngân sách/từ khóa hoặc nhiều môi giới bán cùng căn nhà chưa đủ kết luận cùng đầu mối. Chỉ có tên/nội dung tương tự thì đánh dấu nghi trùng để kiểm tra, không tự loại người khác.

## Quyết định bắt buộc

| Kết quả đối chiếu | Xử lý mặc định |
|---|---|
| Trùng chắc số/chủ thể/bài gốc với kết quả đã trả | Tự bỏ khỏi **mọi bảng** của lượt mới, kể cả bảng mức 3. Không đưa lại dưới nhãn “rà lại nguồn cũ”. |
| Cùng đầu mối cũ có bài, số, vai trò, nhu cầu mới hoặc nâng mức xác minh | Cập nhật khóa/bằng chứng trong sổ; vẫn bỏ khỏi kết quả mới. Chỉ hiển thị lại nếu người dùng yêu cầu xem/cập nhật khách cũ. |
| Trùng giữa nhiều ứng viên mới của chính lượt này | Gộp một dòng/một đầu mối, giữ các nguồn và nhu cầu cần thiết; chọn một nhóm chính, tham chiếu vai trò khác. |
| Nghi trùng, chưa có khóa đủ chắc | Kiểm tra chủ thể trước; nếu vẫn chưa rõ có thể để phần cần xác minh với nhãn nghi trùng, không đếm là đầu mối mới xác nhận. |
| Không trùng trong lịch sử đã đọc | Tiếp tục kiểm tra bằng chứng, thời gian và độ khớp như bình thường; không tự nâng chất lượng vì “mới”. |

Áp cho **cả 5 nhóm, mọi dự án, mọi mức 1–3 đã từng trình bày**, không hết hạn tự động. Đổi ngân sách, đăng lại bài, đổi dự án phù hợp hoặc đổi nhóm không biến đầu mối cũ thành mới. Không xóa/sửa bài, liên hệ hay dữ liệu dự án gốc khi loại khỏi đầu ra. Ngoại lệ chỉ khi người dùng yêu cầu rõ xem lại người cũ hoặc cho phép đưa lại một đầu mối cụ thể.

## Ghi lịch sử sau mỗi lượt

- Thêm mọi dòng thực sự chuẩn bị trả cho người dùng vào `state/seen-leads.json`, gồm mức 3. Không ghi mọi số tình cờ thấy trên web hoặc ứng viên đã bị loại trước khi trình bày. Đầu mối cũ chỉ cập nhật bí danh/nguồn, không thêm dòng mới.
- Mỗi mục giữ tối thiểu: mã nội bộ, tên hiển thị nếu biết, tập số chuẩn hóa, URL bài/hồ sơ đủ định danh, nhóm, ngày đã trả nếu biết, nguồn chứng minh từng được trả và trạng thái xác minh cần thiết. Không lưu giá sàn dự án, nội dung đời tư hay dữ liệu không phục vụ đối chiếu.
- Lưu bền vững ngay trong thư mục skill cá nhân đang dùng: đọc skill-creator hiện hành, chỉ lưu thay đổi của skill này bằng quy trình lưu skill được hỗ trợ; kiểm tra nội dung sau lưu. Không coi tệp scratch hoặc lời hứa nhớ là đã lưu. Không tự ghi vào Sheet dự án. Không yêu cầu người dùng tự cập nhật sổ sau mỗi lượt.
- Nếu lưu thất bại, bảo toàn sổ cũ, vẫn lọc lượt hiện tại theo lịch sử đã đọc và báo hạn chế lưu cho lượt sau; không nhận đã cập nhật sổ thành công.
- Chốt đầu ra bằng số ngắn: `Đã loại X đầu mối trùng lịch sử; Y đầu mối mới đạt chuẩn; Z ứng viên mới cần xác minh`. X đếm đầu mối nhận diện được, không đếm mỗi bản đăng lại thành một người. Không lặp lại tên/số bị loại nếu người dùng chưa yêu cầu danh sách trùng. Thiếu đầu mối mới thì tìm tiếp đủ các nhóm, trả ít hơn khi nguồn không đủ; không lấy khách cũ bù mục tiêu 20.
