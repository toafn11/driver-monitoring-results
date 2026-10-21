# Kiểm chứng bằng video mới — giữ nguyên v3

## Mục đích

Đánh giá góc camera triển khai và các lỗi đã ghi nhận, không dùng lại tập đánh giá cuối để dò ngưỡng. Webcam chưa bắt buộc: có thể dùng video quay bằng điện thoại/camera sẵn có, khi xe đứng yên hoặc trong mô phỏng. Không thực hiện hành vi gây mất tập trung khi đang lái xe thật.

## Video cần chuẩn bị

- Ưu tiên 3–5 người mới, không trùng người đã dùng phát triển. Đây là quy mô thử nghiệm ban đầu, không phải đủ để chứng minh an toàn thống kê.
- Mỗi người có đoạn bình thường liên tục khoảng 10–15 phút, nhìn gương ngắn tự nhiên, nói chuyện bình thường; mục tiêu đo cảnh báo sai, không mặc định mọi đoạn chưa gán nhãn đều an toàn.
- Các đoạn có sự kiện được người đánh giá xác định trước: nhìn lệch kéo dài, nhắm mắt có chủ ý khi đứng yên, cầm/gọi điện trái-phải, thao tác thân/tay. Ghi 5–10 lần mỗi tình huống phù hợp, xen đoạn âm; không gọi nhắm mắt diễn là buồn ngủ sinh lý.
- Có người đeo kính, thay đổi ánh sáng và vị trí tay. Camera thấy mặt và thân/tay nếu muốn chạy cả ba nhánh; video chỉ mặt thì tắt nhánh hành vi.
- Không lật gương, giữ video gốc và FPS/timestamp. Xin phép người tham gia; lưu dữ liệu riêng tư.

## Nhãn và quy trình

1. Chốt danh sách video, tiêu chí cảnh báo cần đánh giá và danh sách người trước khi xem output.
2. Gán nhãn khoảng thời gian trong mẫu CSV đi kèm; phân biệt hành vi quan sát được, sự kiện cần cảnh báo và vùng không chắc chắn. Trường danger_label để unknown nếu không đủ căn cứ.
3. Chạy đúng v3 đã khóa theo HUONG_DAN_POLICY_V3.md. Lưu log, summary, hash video và hash cấu hình. Không sửa ngưỡng giữa các video.
4. Đối chiếu một-một sự kiện/cảnh báo nếu có nhãn sự kiện mới; báo đồng thời bỏ sót, báo sai/giờ có nhãn âm, tổng thời gian báo sai, độ trễ và số không xác định. Không so trực tiếp với metric chồng lấp DMD nếu quy tắc ghép khác.
5. Báo cáo kết quả mới riêng. Nếu quyết định cải thiện model/policy sau đó, chuyển phần dữ liệu phát triển thành validation và cần bộ đánh giá mới; không gọi dữ liệu đã dùng chỉnh là test độc lập.

## Mẫu CSV

reports/final_analysis_20261008/new_video_annotation_template.csv là mẫu định dạng, không phải annotation thực. Thời gian tính giây từ đầu video; subject_id dùng mã giả danh. Có thể dùng nhiều dòng cùng khoảng cho các nhánh khác nhau. Không có dòng không có nghĩa là âm.

## Đề xuất bước tiếp theo

Hoàn thiện báo cáo từ kết quả DMD đã khóa trước. Nếu cần kiểm chứng triển khai ngay, chuẩn bị một video bình thường và vài sự kiện mô phỏng có nhãn để kiểm tra góc quay/định dạng, rồi mới mở rộng người và thời lượng. Không cần train Kaggle lại ở bước này.
