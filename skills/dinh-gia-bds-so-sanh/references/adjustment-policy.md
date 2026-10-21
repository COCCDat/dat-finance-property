# Quy ước tính

Giá nền đất = giá chào × (1 − thương lượng) − giá trị còn lại công trình.
Đơn giá nền = giá nền đất / diện tích đất mốc theo cùng cơ sở diện tích.
Đơn giá điều chỉnh = đơn giá nền × tích (1 + tỷ lệ từng yếu tố).
Giá lô mục tiêu = đơn giá điều chỉnh × diện tích mục tiêu.
Giá tổng hợp = tổng (giá lô từ mốc × trọng số) / tổng trọng số.
Doanh thu = giá đơn lô × số lượng, cộng trong cùng dự án/phương án.

Tỷ lệ dạng thập phân (0.05=+5%). Quy ước nhân phải được công bố, không trộn với cộng tỷ lệ. Không có tỷ lệ điều chỉnh mặc định. Dùng chứng cứ cặp mốc, chào thử hoặc căn cứ khác; thiếu thì Assumption và khoảng nhạy cảm. Không mặc định mọi giá chào giảm 5–10%.

Helper nhận JSON `target_area_m2`, `quantity`, `comparables`. Mỗi mốc có `id`, `ask_vnd`, `area_m2`, `weight`, `scenarios`; mỗi scenario `low/base/high` gồm `discount`, `building_vnd`, `adjustments` (danh sách tỷ lệ). Mọi trường phải được khai báo. Helper tính một loại lô; nhóm/cộng doanh thu dự án riêng, không nhập phương án thay thế cùng nhau.
