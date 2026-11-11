---
name: quet-deal-phan-lo-tphcm
description: Quét và sàng lọc quỹ đất/nhà cũ/kho xưởng cho chiến lược nghiên cứu phân lô TP.HCM theo bộ tiêu chí người dùng. Dùng khi quét deal phân lô, tìm đất lớn, kiếm thêm hoặc chạy lại sourcing. Bắt buộc đất ≥150 m²; ngoài Gò Vấp và Quận 12 cần hệ số rộng/dài ≥ 2/3 hoặc ≥2 mặt đường/hẻm tiếp cận được. Có ngoại lệ Gò Vấp và Quận 12; ưu tiên Tân Bình, Gò Vấp, Bình Thạnh, Tân Phú, Phú Nhuận trước các tài sản vùng ven; hạn chế mặt tiền đường lớn trừ khi giá ngộp hoặc có hẻm phụ; chống trùng, kiểm tra chéo và xử lý CAPTCHA bằng web search/open.
---

# Quét deal phân lô TP.HCM

Trả tiếng Việt ngắn, dễ quét. Chạy sourcing độc lập, không tạo/sửa/kích hoạt lịch daily trừ yêu cầu rõ về lịch. Đây là bản phục dựng; không giả định có sổ deal/lịch tài khoản cũ.

## Điều kiện cứng

Diện tích **đất** ≥150 m² ở mọi nơi; không dùng diện tích sàn.
Gò Vấp và Quận 12 được xác định: chỉ diện tích là ngưỡng tối thiểu (ngoại lệ không yêu cầu tỷ lệ rộng/dài hay số mặt tiếp giáp).
Ngoài Gò Vấp và Quận 12, kể cả vùng mở rộng: diện tích ≥150 m² AND (hệ số rộng/dài ≥ 2/3 OR ≥2 mặt đường/hẻm tiếp cận được).
Hai mặt thoáng giáp nhà/kênh/đất hàng xóm không tự coi là hai mặt tiếp giáp. Không suy ngoại lệ Gò Vấp / Quận 12 từ phường mới chưa ánh xạ địa bàn cũ.

Thiếu dữ liệu điều kiện cứng (chưa rõ kích thước rộng/dài hoặc chưa rõ mặt tiếp giáp ở ngoài Gò Vấp & Q12) → nhóm C cần xác minh. Rõ không đạt → loại, không chứa trong nhóm C. Chạy `python3 scripts/eligibility.py < candidate.json` nếu cần kiểm tra logic: `area_m2`, `width_m`, `length_m`, `width_to_length_ratio`, `access_sides`, `go_vap`, `quan_12`, `adverse_planning`, `excessive_setback`; chưa biết là null. Script không xác minh nguồn.

Loại nhóm chính khi bài công khai có quy hoạch bất lợi: cây xanh/giao thông/hỗn hợp/hành lang bảo vệ/khó xây dựng, dính lộ giới đường lớn >25% diện tích, hoặc loại đất rõ không phù hợp. Gần sông/kênh chỉ là risk flag, không tự kết luận dính hành lang. Thiếu số m² đất ở không tự loại, nhưng ghi thiếu và hạ ưu tiên. “Công nhận đủ” không đồng nghĩa full thổ cư.

## Phạm vi và ưu tiên

Mặc định ưu tiên tìm tin các khu vực: **Tân Bình → Gò Vấp → Bình Thạnh → Tân Phú → Phú Nhuận** trước, sau đó mới đến các tài sản vùng ven (Bình Tân, Quận 12, Hóc Môn, Bình Chánh...). Dùng phạm vi/budget người dùng nếu có. Khi mở rộng tại TP.HCM, ghi riêng; không thay vùng chỉ định âm thầm. Không tự đặt trần vốn.

Ưu tiên đất ở tỷ lệ cao, lô góc, thửa đẹp (rộng/dài cân đối), ô tô/hẻm thông (5–8 m), đất trống/nhà cũ/cấp 4/dãy trọ/kho xưởng dễ xử lý. Hạ premium công trình mới/biệt thự/building.

**Hạn chế mặt tiền đường lớn:** Mặc định hạ ưu tiên các tài sản nằm ngay mặt tiền đường lớn, trục xương sống hoặc đại lộ (lộ giới ≥20 m) do đơn giá bị đội chi phí thương mại và rủi ro lộ giới lớn. Chỉ giữ và xem xét khi đạt ít nhất một trong các điều kiện: (1) Giá ngộp/đơn giá thô rẻ: giá/m² trên đất công nhận xấp xỉ hoặc chỉ nhỉnh nhẹ (≤1.2 lần) so với giá hẻm xe hơi khu vực; (2) Lô góc có hẻm phụ: mặt tiền đường lớn nhưng có hẻm hông/hẻm sau ≥4 m để tổ chức giao thông tách thửa; (3) Thửa đất "lõi sâu/nở hậu lớn": mặt tiền kết nối còn phần lớn diện tích (≥70%) nằm phía sau phù hợp mở hạ tầng nội bộ. Loại thẳng nếu diện tích dính quy hoạch lộ giới đường lớn chiếm >25% tổng diện tích khuôn viên hoặc phần đất còn lại sau lộ giới không đủ chuẩn diện tích tách thửa.

Xếp hình thể: (rộng/dài ≥ 2/3 + hai mặt) → hai mặt → rộng/dài ≥ 2/3 → ngoại lệ Gò Vấp & Quận 12; kết hợp độ mới, đầy đủ, đất ở, công trình và giá/m². Không chấm số trừ khi được yêu cầu; không gọi giá thấp là deal có lời trước khi định giá đầu ra. Chỉ đọc quy hoạch bài công bố ở sourcing, không tra địa chính chuyên sâu từng candidate.

## Tìm và xác minh

Đọc [references/source-policy.md](references/source-policy.md). Ưu tiên web search → web open, đa nguồn. Không tự browser/dò đăng nhập để lookup công khai. Không vượt CAPTCHA; một bài bị chặn không dừng cả lượt.

Tìm cùng mã tin/tiêu đề/địa chỉ/hình thể trên nguồn khác. Index/cache dùng sàng lọc; nhóm chính cần URL bài riêng và bằng chứng đủ điều kiện cứng. Bài gốc bị chặn cần đối soát trên nguồn khác và ghi rõ chưa đọc bài gốc; snippet thiếu trường không đủ xác minh.

Chống trùng theo địa chỉ, ảnh, diện tích/hình thể, mô tả và giá dù khác URL/môi giới. “Tìm thêm” loại tài sản đã gửi trong ngữ cảnh/sổ deal truy cập được. Không có lịch sử đầy đủ thì nói giới hạn chống trùng; không hứa xuyên tài khoản. Không tự ghi sổ bền vững chưa xác định.

Phân biệt ngày đăng, cập nhật/đẩy tin, thu thập và index. Tin cũ đẩy lại không gọi tin mới. “Hôm nay” dùng giờ Việt Nam. Không bù đủ 5 bằng tin trượt lọc hoặc che tuổi tin.

## Kết quả

Mặc định tối đa 5 deal; trả ít hơn nếu thiếu. Ba nhóm: A Rất đáng xem; B Đạt tiêu chí; C Cần xác minh. C không tính deal đạt; ghi rõ vùng mở rộng.

Mỗi dòng: địa chỉ/khu vực; diện tích đất/công nhận; ngang×sâu; mặt tiếp giáp; đường/lối vào; hiện trạng; đất ở X/Y hoặc chưa công bố; quy hoạch theo lời đăng/chưa có; giá chào; giá/m² và mẫu số; ngày đăng/cập nhật; một câu lý do; mâu thuẫn; **link bài gốc** và mức kiểm chứng.

Kết thúc thứ tự gọi và 2–3 câu hỏi quan trọng: sổ/sơ đồ, đất ở, quy hoạch/lộ giới, thuê/bàn giao. Không tự liên hệ môi giới. Không khẳng định pháp lý sạch/tách thửa/xây dựng chỉ từ quảng cáo. Khi yêu cầu pháp lý sâu, tra văn bản chính thức hiện hành riêng.
