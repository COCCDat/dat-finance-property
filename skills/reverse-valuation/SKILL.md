---
name: reverse-valuation
description: Định giá ngược cổ phiếu/doanh nghiệp theo giá → tập kỳ vọng hàm ý → evidence → expectation gap → edge → catalyst → payoff/falsifier. Dùng cho PRICE-IN, FIND EDGE, RED TEAM, FULL, ưu tiên Việt Nam và thị trường mới nổi; nhận giá/ngày, BCTC/dữ liệu người dùng. Không dùng định giá trữ lượng hoặc coi target price là dự báo chắc chắn.
---

# Reverse Valuation

Trả tiếng Việt, phân biệt thông tin và phân tích. Đây là bản phục dựng lịch sử, chưa khôi phục script Vnstock gốc. Không dùng giá/con số cũ trong lịch sử như dữ liệu mới.

## Mode và phạm vi

- PRICE-IN: giải các tổ hợp giả định phù hợp giá, chưa tự khẳng định edge.
- FIND EDGE: đối chiếu expectation gap với evidence/materiality.
- RED TEAM: phản đề mạnh, giả thuyết thay thế và falsifier.
- FULL / FULL REVERSE VALUATION: toàn bộ luồng và investment map.

Không chỉ mode → FULL phù hợp độ đủ dữ liệu. Khóa mã/sàn, giá/ngày, chân trời, tiền tệ/đơn vị, cổ phiếu/corporate actions, công bố có sẵn tại ngày định giá. Thiếu đối tượng → hỏi; thiếu drivers → làm phần có evidence và báo thiếu. Bài toán quá khứ không dùng dữ liệu công bố sau ngày định giá làm bằng chứng biết trước.

## Data gate

Đọc [references/data-policy.md](references/data-policy.md). Chạy `python3 scripts/vnstock_preflight.py` khi kiểm tra môi trường. Preflight hiện trả UNAVAILABLE có chủ đích: Vnstock 4.0.8 PyPI quarantined, adapter gốc chưa khôi phục. Không cài/import bản cũ, không nói đã truy vấn Vnstock, không tự đổi gói tài trợ. Dùng BCTC/công bố, dữ liệu người dùng hoặc nguồn công khai dự phòng.

Mỗi driver: giá trị, đơn vị, kỳ, ngày công bố/lấy, URL/file/trang, hợp nhất/riêng lẻ và Fact / Market input / Assumption / Inference / Forecast. Không bịa consensus; thiếu thì gọi proxy/reference scenario. Dữ liệu người dùng chưa đối soát phải ghi rõ.

Kiểm tra giá/shares cùng ngày, corporate actions, VND/nghìn/triệu/tỷ, LNST hợp nhất/thuộc mẹ, quý/lũy kế, restatement, cash/debt/NCI, dữ liệu trùng/rỗng/sai kỳ. Thiếu trọng yếu → Insufficient evidence, không tự điền.

## Luồng bắt buộc

1. Business economics: chọn 2–4 drivers quyết định cash flow/risk, giải cơ chế và độ nhạy; đọc [references/model-and-output.md](references/model-and-output.md) để chọn model.
2. Capital bridge: market cap=giá×shares phù hợp; EV=equity+debt+NCI+claims phù hợp−cash/excess assets phù hợp. Không trừ toàn bộ cash hoạt động; ngân hàng không dùng EV/EBITDA máy móc.
3. Reverse model: khóa giả định có lý do; giải một driver mỗi lần hoặc grid nhiều biến. Một giá không nhận diện duy nhất nhiều biến; trả **tập tổ hợp**, nhạy discount rate/terminal value. Nghiệm không là kỳ vọng duy nhất của thị trường.
4. Evidence map: kiểm tra assumption với lịch sử/công suất/chất lượng tài sản/orderbook/presales/cash collection. Các bài kể cùng nguồn không là evidence độc lập. Không suy thiếu disclosure là tin tốt.
5. Edge: market-compatible assumption → thesis khác → evidence → materiality trên cash flow/value → vì sao chưa phản ánh → điều kiện sai. Khác consensus không tự là edge. Bằng chứng/cơ chế chưa đủ thì gọi hypothesis.
6. Catalyst: sự kiện → driver kinh tế → assumption được kiểm định → value. Timeline, threshold, uncertainty. Tin tốt có thể đã price-in; không gán xác suất tùy ý/hứa rerating. Với VN, hypothesis phản ứng giá khác kết quả event study thực tế.
7. Bear/base/bull: cùng model, tính dilution/dividends/thời gian/chi phí khi phù hợp; kiểm tra opportunity cost và không có catalyst. Chỉ tính expected value khi lý giải xác suất.
8. Red team/falsifier: ≥2 phản đề mạnh, permanent loss, chỉ báo thesis sai, deadline review và biến theo dõi. Không chọn phản biện yếu để dễ bác.

PRICE-IN làm 1–3 kèm data/sensitivity; FIND EDGE 1–5 kèm catalyst/falsifier; RED TEAM bám thesis/dữ liệu; FULL cả 8. Dữ liệu thiếu thì trả phần có thể và giới hạn.

## Output

Mode/ngày → kết luận mức evidence → snapshot nguồn → model/bridge → bảng tập kỳ vọng → evidence/gap → catalyst → bear/base/bull → red team/falsifier → investment map/dữ liệu thiếu. Đưa công thức/giả định kiểm tra được, không yêu cầu chuỗi suy nghĩ nội bộ.

FULL xếp Actionable for further diligence / Watchlist / Pass / Insufficient evidence, giải thích bằng điều kiện kiểm chứng. Đây là xếp loại nghiên cứu, không tự đặt lệnh/gán tỷ trọng cá nhân. Upside model không là lợi nhuận chắc chắn; intrinsic value không là dự báo giá 6–12 tháng. Cite ngay cạnh dữ kiện, không chỉ danh sách nguồn chung.
