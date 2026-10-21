# Mẫu 18 cột phục dựng

Nhận cả bảng tên cột khác nếu ánh xạ rõ. Mỗi dòng là một loại lô; không đoán ô trống là 0. Không ép người dùng cung cấp lại dữ liệu đọc được.

| Cột | Ý nghĩa |
|---|---|
| ma_du_an | Nhóm dự án |
| phuong_an | Phương án, không cộng phương án thay thế |
| ma_tai_san | Mã loại sản phẩm |
| vi_tri | Địa chỉ/cụm đường |
| loai_san_pham | Đất trống, nhà đất... |
| dien_tich_m2 | Diện tích đất định giá, số dương |
| co_so_dien_tich | sau_lo_gioi / truoc_lo_gioi / chua_ro |
| ngang_m | Bề ngang |
| sau_m | Chiều sâu, để trống nếu chưa rõ |
| hinh_the | Vuông, nở hậu, thửa nông... |
| loai_duong_hem | Mặt tiền, hẻm thông/cụt, lối vào... |
| rong_duong_hem_m | Độ rộng hiện hữu; lộ giới ghi riêng |
| so_mat_tiep_giap | Mặt đường/hẻm tiếp cận được |
| hien_trang | Đất trống, cấp 4, nhà tầng, thuê... |
| phap_ly_quy_hoach | Loại đất, sổ, quy hoạch/lộ giới |
| so_luong_lo | Số nguyên dương; không mặc định |
| pham_vi_tim_kiem | Ranh đường/khu vực/ảnh Maps |
| thoi_han_ban_thang | Thời hạn bán, để trống nếu chưa rõ |

Không lấy diện tích/ngang làm chiều sâu thực tế; chỉ được ghi tỷ số này là ước tính kiểm tra hình thể. Không cào Sheet bằng phiên đăng nhập khi không có quyền; dùng file người dùng gửi khi không đọc được.
