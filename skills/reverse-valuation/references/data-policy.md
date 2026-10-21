# Dữ liệu và trạng thái kết nối

Lịch sử ghi adapter Community 4.0.8: OHLCV/quote/finance/ratio/profile, web/local độc lập, retry/cache metadata, cô lập thư mục để ngăn AGENTS.md bootstrap, không dùng gói tài trợ. Chưa tìm được mã gốc.

Kiểm tra 2026-10-14: https://pypi.org/project/vnstock/4.0.8/ ghi project quarantined. https://www.vnstocks.com/docs/vnstock/cai-dat mô tả v5 từ kho riêng, API thay đổi. Không cài vòng qua quarantine hoặc suy kho mới/bản cũ cài sẵn đã được kiểm toán. Bản phục dựng không import/query/install Vnstock, không tự nâng global Python.

`scripts/vnstock_preflight.py` chỉ đọc metadata, trả UNAVAILABLE/adapter chưa khôi phục, ghi Python và version nếu có. READY chỉ sau khi adapter/nguồn phân phối được kiểm tra, pin, test. Không nói thiếu Python khi chỉ thiếu adapter.

Nguồn fallback: BCTC kiểm toán/soát xét/công bố doanh nghiệp/sở → file người dùng với nguồn/ngày/kỳ → provider công khai khác → web search tìm/đọc tài liệu. Chính thức quyết định khi xung đột, log chênh và ảnh hưởng. Snippet đơn lẻ không đủ driver trọng yếu.

Cache chỉ dùng khi biết nguồn/version/time/as-of/unit, ghi stale; quote cache không là giá mới. Không trộn cache/credentials giữa web-local.

Khi cập nhật adapter tương lai: Guest/free, pin version đã test, timeout process, retry 2–3 lỗi tạm thời (không retry schema/auth), JSON sạch, không key trong logs, kiểm tra schema/đơn vị/kỳ, scratch riêng, không thực thi AGENTS.md dependency sinh, cache theo query/source/version/env. Mạng bị chặn → fallback, không loop.
