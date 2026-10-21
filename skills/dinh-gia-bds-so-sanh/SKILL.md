---
name: dinh-gia-bds-so-sanh
description: Định giá sơ bộ BĐS bằng phương pháp so sánh; tìm 5–10 tin mỗi loại lô, điều chỉnh từ 3 tài sản tương đồng nhất và dự phóng doanh thu gộp. Dùng khi yêu cầu định giá nhà đất, tìm comparables, so sánh phương án chia lô từ Google Sheet/CSV/XLSX, văn bản hoặc ảnh Maps chỉ định khu vực. Không áp dụng bộ lọc sourcing 150 m².
---

# Định giá BĐS so sánh

Trả tiếng Việt, bảng ngắn, số liệu truy nguyên được. Đây là bản phục dựng từ lịch sử, chưa có file gốc; mẫu 18 cột và helper được thiết kế lại.

## Chuẩn hóa đầu vào

Đọc [references/input-schema.md](references/input-schema.md) khi nhận bảng; dùng [assets/mau-dau-vao.csv](assets/mau-dau-vao.csv) làm mẫu. Một dòng là một loại sản phẩm có số lượng lô. Tách dòng khi vị trí, diện tích, hình thể hoặc pháp lý khác nhau. Nhóm theo dự án/phương án; không cộng các phương án thay thế vào một tổng doanh thu.

Nhận cả văn bản/ảnh. Hỏi chỉ thiếu thông tin ảnh hưởng trọng yếu: vị trí, loại sản phẩm đầu ra, diện tích/cơ sở trước-sau lộ giới, bề ngang, đường/hẻm và phạm vi tìm. Không mặc định số lượng hay thời hạn bán; thiếu số lượng thì chỉ định giá đơn lô. Nếu Sheet không đọc được, yêu cầu CSV/XLSX, không giả vờ đã đọc.

Đọc nhãn/ranh ảnh Maps; không tự suy tọa độ/bán kính/kích thước khi thiếu tỷ lệ. Không trừ lộ giới lần hai nếu diện tích đã sau lộ giới. Giữ mâu thuẫn diện tích và hỏi trước khi tính. Dùng địa danh cũ/mới làm từ khóa, không tự khẳng định tương đương.

## Tìm và đối soát

Ưu tiên web search → web open, không tự khởi tạo browser/dò đăng nhập cho lookup công khai. Tìm đa nguồn theo địa chỉ, cách viết, đường/hẻm, diện tích, ngang, đất trống/nhà cũ. Giữ phạm vi chỉ định; thiếu tin thì báo và đề xuất vùng mở rộng riêng.

Chỉ trả URL trực tiếp có thật; không tạo slug, dùng trang danh mục/search thay bài. Gặp CAPTCHA thì tìm mã tin/tiêu đề/địa chỉ/hình thể trên nguồn khác; không vượt xác thực. Snippet đơn lẻ chỉ là đầu mối. Tin index/cache phải ghi nguồn, trường đã đối soát và trạng thái bài gốc chưa mở được.

Loại trùng theo địa chỉ, ảnh, diện tích/hình thể và mô tả dù khác giá/môi giới/URL. Giữ giá tiêu đề/bảng/mô tả nếu mâu thuẫn, không chọn thấp nhất âm thầm. “Đã bán” không chứng minh giá giao dịch. Phân biệt ngày đăng, đẩy tin và ngày thu thập.

Thu thập 5–10 tài sản riêng biệt cho mỗi loại lô nếu đủ chất lượng. Bảng gồm link, vị trí/đường-hẻm, giá chào, diện tích đất và cơ sở diện tích, ngang/sâu, hiện trạng, đất ở/pháp lý, ngày, độ tương đồng, thiếu/mâu thuẫn và trạng thái kiểm chứng. Dừng khi đủ tập tin tốt và 3 mốc chính đã kiểm tra, không kéo dài để đủ số.

## Điều chỉnh 3 mốc tốt nhất

Đọc [references/adjustment-policy.md](references/adjustment-policy.md). Chọn vị trí/công năng trước, rồi diện tích, hình thể, đường/hẻm, hiện trạng, pháp lý và độ mới; không chọn chỉ vì giá thấp. Giải thích chọn/loại từng mốc.

So nhà với đất trống phải tách giá trị còn lại công trình, có căn cứ hoặc khoảng Assumption. Không trừ nguyên chi phí xây mới của nhà cũ. Phân biệt giá trị công trình mốc và chi phí phá dỡ dự án. Không lấy giá nhà/m² gọi là giá đất.

Lập bảng từng chênh lệch: hướng, mức/range, căn cứ, Fact/Assumption. Mục tiêu tốt hơn mốc → điều chỉnh mốc lên. Không cộng premium ngang mà bỏ qua thửa nông/công năng/xây dựng. Tránh đếm hai lần diện tích-quy mô, vị trí-đường, thời điểm-thương lượng.

Dùng `python3 scripts/compare_value.py < input.json` để kiểm tra số học; helper không lựa chọn điều chỉnh hay xác minh dữ liệu. Công bố input trong bảng. Nếu có 1–2 mốc tốt, dùng đúng số và hạ độ tin cậy; nếu không có mốc đủ căn cứ, trả dữ liệu và thiếu hụt, không nặn khoảng giá.

## Kết quả

Trả các tin → 3 mốc/điều chỉnh → thấp/cơ sở/cao mỗi lô → số lô và doanh thu gộp riêng từng phương án. Ghi đơn vị, độ tin cậy và 2–3 biến nhạy. Không tự mặc định bán trong 6 tháng.

Phân biệt giá chào, giá bán khả thi giả định, giá giao dịch xác nhận. Doanh thu không phải lợi nhuận/NPV/vốn thu ròng. Muốn lợi nhuận/DCF phải bổ sung chi phí và lịch dòng tiền. Không khẳng định tách thửa/xây dựng dựa quảng cáo; khi phụ thuộc điều kiện đó, nêu cần xác minh và tra văn bản chính thức hiện hành nếu được yêu cầu thẩm định pháp lý.
