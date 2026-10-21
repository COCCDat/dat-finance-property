# Đầu vào

Mẫu đã tạo cho người dùng: https://docs.google.com/spreadsheets/d/1P8aKldn4453yoUJxkC8UmIzTJ8-YVCQR4qGBfNoIQ7s/edit . Khi người dùng nói dùng mẫu dự án mà không gửi link mới, có thể đọc mẫu này. Nếu họ cung cấp link/file khác thì dùng nguồn họ chỉ định. Không tự sửa mẫu hoặc ghi khách tìm được vào đó khi đầu ra chỉ yêu cầu bảng chat.

Nhận Google Sheet, CSV/XLSX hoặc văn bản. Với mẫu Sheet, đọc `Huong_dan`, `Du_an`, `Tai_san`. `Huong_dan!B14` là số đầu mối mục tiêu mặc định 20. Không coi mã mẫu/dòng Chưa nhập là dữ liệu đang bán.

## Du_an — mỗi dòng một dự án

Các trường theo thứ tự:

1. Mã dự án * — khóa duy nhất.
2. Tên dự án * — tên nội bộ cũng được.
3. Tỉnh / Thành phố *.
4. Quận / Huyện theo tên quen dùng * — tên cũ để tìm cũng được.
5. Phường / Xã hiện tại — bổ sung tên cũ nếu khác.
6. Đường / Khu vực cụ thể *.
7. Link Google Maps * — chấp nhận tọa độ/mô tả thay thế đủ chính xác.
8. Khu vực lân cận có thể chào — để trống thì đề xuất theo vị trí.
9. Mô tả dự án.
10. Pháp lý chung.
11. Quy hoạch / Xây dựng — nguồn, ngày kiểm tra nếu có.
12. Tiến độ / Thời gian bàn giao.
13. Điểm phù hợp khách xây bán / xây ở.
14. Điều kiện hợp tác môi giới.
15. Link ảnh / Hồ sơ được phép dùng.
16. Giới hạn thông tin được chào.
17. Ghi chú.

## Tai_san — mỗi dòng một tài sản

Các trường theo thứ tự:

1. Mã tài sản * — khóa duy nhất.
2. Mã dự án * — liên kết Du_an.
3. Tên / Ký hiệu lô *.
4. Trạng thái * — Chưa nhập; Đang bán; Tạm ngưng; Đã bán. Chỉ dùng Đang bán.
5. Loại tài sản * — Chưa xác định; Đất trống; Nhà cũ; Nhà nát; Dãy trọ; Kho xưởng; Khác.
6. Vị trí riêng / Maps — ghi đè vị trí chung khi có.
7. Diện tích đất (m²) * — phân biệt với diện tích sàn.
8. Ngang (m) *.
9. Dài (m).
10. Đường / Hẻm trước đất (m) * — rộng tiếp giáp.
11. Lối vào / Điểm thắt hẻm — khả năng tiếp cận thực tế.
12. Số mặt tiếp cận.
13. Giá chào (tỷ VNĐ) * — số: 3.5 = 3.5 tỷ VNĐ.
14. Giá thấp nhất có thể trao đổi (tỷ VNĐ) — nội bộ, không công bố/truy vấn.
15. Pháp lý riêng *.
16. Hiện trạng công trình *.
17. Điều kiện xây dựng / Quy hoạch.
18. Thời điểm bàn giao.
19. Khách phù hợp ưu tiên — Tất cả; Đầu tư xây bán; Đầu tư sửa bán; Mua xây ở; Mua sửa ở; Khác.
20. Điểm mạnh để ghép khách.
21. Hạn chế / Điều kiện bắt buộc.
22. Phí / Điều kiện môi giới riêng.
23. Link ảnh / Hồ sơ riêng.
24. Thông tin được phép chào.
25. Ghi chú.

Dấu * là cốt lõi đề nghị điền, không phải lý do hỏi lại tất cả ô trống khi đã đủ tìm. Pháp lý chưa rõ phải thể hiện, không ghép chắc chắn với khách yêu cầu pháp lý cụ thể. Không coi giá sàn là cam kết chốt; chỉ nêu khả năng trao đổi khi người dùng cho phép. Dữ liệu tài sản riêng ưu tiên thông tin chung.
