# Báo cáo kết quả hệ thống giám sát tài xế — 08/10/2026

## Phạm vi và thiết kế

Hệ thống gồm ba mô hình chuyên biệt (Gaze, mắt/ngáp, hành vi) và chính sách thời gian v3. Các checkpoint và chính sách được giữ nguyên trong đánh giá cuối. Camera mặt phục vụ Gaze/mắt-ngáp; camera thân phục vụ hành vi. Đây là đánh giá từng nhánh, chưa phải kiểm chứng đồng bộ ba nhánh trên cùng góc camera triển khai.

Validation dùng người 5,13,29 để phát triển/chọn chính sách. Đánh giá thời gian cuối dùng người 7,23,36 với 21 video (4 Gaze, 4 mắt-ngáp, 13 hành vi). Người 23 có nhiều video hơn, nên số liệu gộp chịu ảnh hưởng lớn hơn từ người này. SHA256 của 21 video khác nhau; điều đó không tự chứng minh mọi nội dung hình ảnh đều độc lập. Những người này đã được đánh giá phân loại ảnh trước đó, vì vậy đây là đánh giá thời gian bổ sung, không phải một tập hoàn toàn chưa từng xem kết quả.

Sự kiện tham chiếu suy ra từ annotation: mắt nhắm đủ 1.5 giây, nhìn ngoài front/hành vi ngoài safe_drive đủ 2 giây. Ngáp chỉ là tín hiệu hỗ trợ. Sự kiện này không tương đương nhãn nguy hiểm hay buồn ngủ sinh lý. Các khoảng nhìn gương cũng thuộc nhóm ngoài front, cần ngữ cảnh giao thông để xác định có nên cảnh báo.

## Kết quả theo sự kiện

| Nhánh | Video | Phát hiện / tham chiếu | Recall | Bỏ sót | Bắt đầu sai trên đoạn âm | Thời gian âm (giây) | Bắt đầu ở vùng chưa rõ nhãn |
|---|---:|---:|---:|---:|---:|---:|---:|
| Nhìn lệch | 4 | 10/10 | 100.00% | 0 | 1 | 56.89 | 25 |
| Mắt nhắm kéo dài | 4 | 21/22 | 95.45% | 1 | 7 | 422.98 | 36 |
| Hành vi mất tập trung | 13 | 91/98 | 92.86% | 7 | 2 | 1354.37 | 5 |

Phát hiện được định nghĩa là có ít nhất một mẫu cảnh báo chồng lấp sự kiện tham chiếu. Một cảnh báo liên tục có thể chồng nhiều sự kiện; không phải phép ghép một-một giữa cảnh báo và sự kiện. Số lần bắt đầu sai không tính đầy đủ cảnh báo kéo dài sang đoạn âm; cần đọc thêm thời gian chồng đoạn âm (Gaze 2.39 giây, mắt 3.49 giây, hành vi 4.54 giây). Các lần bắt đầu ở vùng chưa rõ nhãn được báo riêng, không coi là đúng hoặc sai. Không cộng recall giữa các nhánh thành một độ chính xác chung.

## Kịp thời và bỏ sót

| Nhánh | Trễ P95 sau mốc tham chiếu (giây) | Trễ lớn nhất sau mốc (giây) | Bắt được trong 2 giây sau mốc / tổng sự kiện |
|---|---:|---:|---:|
| Nhìn lệch | 5.80 | 5.98 | 7/10 |
| Mắt nhắm kéo dài | 0.00 | 0.00 | 21/22 |
| Hành vi mất tập trung | 2.40 | 38.98 | 84/98 |

Các độ trễ được tính trên sự kiện bắt được; bỏ sót được giữ trong mẫu số ở cột cuối. Mốc 2 giây là mô tả bổ sung sau đánh giá, không phải tiêu chí nghiệm thu đặt trước và không dùng chỉnh ngưỡng. Trễ 0 sau mốc không có nghĩa cảnh báo ngay khi hành vi bắt đầu: mốc tham chiếu đã chứa thời gian chờ 1.5 hoặc 2 giây. CSV riêng lưu thời điểm bắt đầu hành vi và mẫu cảnh báo đầu tiên, kể cả khi cảnh báo đã hoạt động từ trước.

Ca chậm nhất là gọi điện trái ở video 009_distraction_7: trễ 38.98 giây sau mốc tham chiếu (khoảng 40.99 giây sau lúc hành vi bắt đầu). Trong đoạn tham chiếu có 494 mẫu phonecall_left; model dự đoán 241 phonecall_left, 240 safe_drive và 13 texting_left. Đây là bằng chứng nhầm phân loại và điều kiện tích lũy ảnh hưởng thời gian cảnh báo, chưa phải xác định nguyên nhân hình ảnh vì chưa xem video gốc. Một ca khác trong cùng video trễ 17.91 giây.

Mắt bỏ sót một sự kiện người 7: trong 17 mẫu còn lại sau mốc tham chiếu, 14 mẫu bị dự đoán open và 3 close. Hành vi bỏ sót 7 sự kiện; một số chỉ còn 1–3 mẫu sau mốc đủ thời lượng, cần xem đầy đủ khoảng hành vi trước mốc khi phân tích, không quy hết thành lỗi model hoặc nhãn. Ba sự kiện Gaze trễ trên 2 giây nằm trong các đoạn left_mirror/left.

## Phân loại từng ảnh trong luồng video

| Nhánh | Mẫu có nhãn phù hợp | Accuracy tính thiếu dự đoán là lỗi | Macro-F1 | Độ phủ dự đoán |
|---|---:|---:|---:|---:|
| gaze | 3027 | 80.87% | 80.74% | 97.49% |
| eyes | 5355 | 98.64% | 96.94% | 99.96% |
| yawn | 7629 | 92.76% | 84.28% | 99.96% |
| action | 31585 | 83.59% | 78.10% | 100.00% |

Đây là metric gộp ma trận nhầm lẫn toàn bộ video, không lấy trung bình F1 các video thiếu lớp. Nhánh mắt chỉ tính close/open; opening/closing bị mask. Nhãn không thuộc 11 lớp hành vi được loại khỏi phần đánh giá tương ứng. Sampling và xử lý mất mặt khác luồng ảnh đóng gói ban đầu nên không đồng nhất tuyệt đối các mẫu số.

## Kết luận có căn cứ

Bản v3 đạt recall sự kiện tham chiếu cao trong điều kiện DMD, nhưng còn cảnh báo sai, đoạn chưa rõ nhãn và độ trễ dài. Chưa đủ căn cứ khẳng định cảnh báo nguy hiểm luôn kịp thời, hiệu quả ngoài thực tế, hoặc đạt 90% recall buồn ngủ sinh lý. Gaze chỉ có 10 sự kiện và khoảng 57 giây âm, nên cần đặc biệt thận trọng với con số 100%.

Giữ nguyên bản đã đánh giá làm mốc báo cáo; không chỉnh ngưỡng trên tập cuối. Việc kiểm thử mới phải dùng video khác và ghi riêng kết quả, ưu tiên góc camera triển khai, phản chiếu kính, tay/điện thoại che khuất và thời lượng lái xe an toàn đủ dài. Chưa có đo FPS webcam/toàn hệ thống trong thử nghiệm này.

## Nguồn truy vết

- reports/temporal_final_lock.json: cấu hình khóa trước đánh giá.
- reports/temporal_final_verified.json: kiểm chứng hash, frame metric và replay chính sách.
- reports/final_analysis_20261008/all_events.csv: toàn bộ sự kiện.
- reports/final_analysis_20261008/review_missed_or_late.csv: sự kiện bỏ sót hoặc trễ trên 2 giây.
- reports/final_analysis_20261008/negative_and_unknown_alerts.csv: cảnh báo trên đoạn âm/chưa rõ nhãn.
- reports/final_analysis_20261008/summary.csv: bảng số liệu tái sử dụng.

Thuyết minh: kiến trúc module phù hợp định hướng nhiều dấu hiệu. Phần NTHU, dữ liệu người Việt, tối ưu quantization/pruning và kiểm thử thực tế cần báo cáo đúng mức hoàn thành; kết quả DMD hiện tại không tự thay thế các nội dung chưa thực hiện đó.
