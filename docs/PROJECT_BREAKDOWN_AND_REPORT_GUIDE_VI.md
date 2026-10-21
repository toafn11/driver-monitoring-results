# Phân rã dự án, quá trình nghiên cứu và hướng dẫn viết báo cáo

Tài liệu bàn giao cho nhóm, cập nhật gói demo ngày 21/10/2026. Số liệu nghiên cứu giữ theo bản đã kiểm chứng đến 08/10/2026. Việc bổ sung giao diện demo không thay đổi trọng số, chính sách hoặc kết quả đã báo cáo.

## 1. Mục đích và cách sử dụng repo

Repo kết quả dành cho hai công việc: chạy demo để các thành viên hiểu hệ thống và sử dụng bằng chứng đã kiểm chứng để viết báo cáo. Repo phát triển vẫn private; repo này không chứa toàn bộ lịch sử thử nghiệm, dữ liệu huấn luyện hay các đường dẫn tải dữ liệu riêng.

Tài liệu viết chung: [Google Docs báo cáo tổng kết](https://docs.google.com/document/d/1tW-ffErO15po9oFcCIh8oE8n61blfpx9Y3yu3EEIfos/edit?usp=sharing). Quyền đọc, sửa do chủ tài liệu quản lý riêng. Mã nguồn hoặc trọng số không được sửa chỉ để khớp với một kết luận mong muốn trong báo cáo.

## 2. Có thể tổng kết đến mức nào?

Có thể tổng kết phần xây dựng dữ liệu, huấn luyện mô hình, lựa chọn cấu hình, tích hợp suy luận và đánh giá DMD. Chưa thể kết luận đã hoàn thiện hệ thống cảnh báo an toàn trong thực tế. Các thành viên có thể dùng demo mới để thu thập minh chứng, nhưng cần phân biệt chạy được phần mềm với đánh giá định lượng có nhãn.

| Nội dung | Mức hoàn thành | Cách trình bày |
|---|---|---|
| Ba mô hình DMD | Đã chọn và kiểm chứng trọng số | Nêu kiến trúc, nhiệm vụ, nhãn và tập đánh giá |
| Quy tắc thời gian v3 | Đã khóa trước đánh giá cuối | Nêu tham số, quy trình chọn và giới hạn |
| Đánh giá video DMD | Đã có 21 video, ba người | Báo cáo recall cùng độ trễ và báo nhầm |
| Ứng dụng demo webcam/video | Đã bổ sung mã demo | Ghi rõ mới kiểm tra phần mềm, chưa có đánh giá webcam thực tế |
| Demo trên máy thành viên | Chờ từng thành viên thực hiện | Lưu môi trường, điều kiện và kết quả chạy |
| Bộ dữ liệu người Việt, NTHU | Chưa có kết quả hoàn thành được kiểm chứng | Không viết như thực nghiệm đã làm |
| Quantization/pruning, FPS toàn hệ thống | Chưa hoàn thành | Đưa vào hạn chế và hướng phát triển |

## 3. Quá trình phát triển và các quyết định chính

### Giai đoạn 1: xuất phát từ nhận diện buồn ngủ

Hướng ban đầu sử dụng đặc trưng khuôn mặt và mô hình chuỗi trên RLDD. Quá trình bao gồm kiểm tra video, trích xuất đặc trưng, chia phần xử lý trên Kaggle, ghép dữ liệu và huấn luyện các cấu hình GRU. Những lỗi metadata, seek và timestamp được xử lý bằng kiểm tra giải mã thực tế thay vì bỏ qua kiểm tra dữ liệu.

GRU12 và GRU20 khác số đặc trưng đầu vào trong hướng mô hình chuỗi, không phải hai tên gọi của các mô hình DMD hiện tại. Nhánh này giúp khảo sát buồn ngủ nhưng chưa bao phủ các hành vi như dùng điện thoại hoặc với tay. Các trọng số RLDD cũ không nằm trong gói demo cuối. Nếu báo cáo cần nêu số liệu của giai đoạn này, phải đối chiếu hồ sơ riêng trong repo phát triển, không lấy kết quả DMD thay thế.

### Giai đoạn 2: mở rộng theo mục tiêu mất tập trung

Sau khi đối chiếu mục tiêu đề tài, phạm vi được mở rộng sang hướng nhìn và hành vi. Có nghiên cứu mô-đun nhìn lệch và hướng dữ liệu State Farm; đây là các bước hình thành hướng tiếp cận, không phải các thành phần được cộng vào bộ trọng số cuối. Báo cáo nên dùng chúng để giải thích quá trình lựa chọn, không tạo bảng so sánh giữa các thí nghiệm khác dữ liệu nếu chưa chuẩn hóa nhiệm vụ và cách đánh giá.

### Giai đoạn 3: chuyển sang ba phần DMD

DMD được tổ chức theo Gaze, Drowsiness và Distraction để phát triển ba mô hình phù hợp với từng nhóm dấu hiệu. Nhóm xử lý video RGB, nhãn OpenLABEL, đồng bộ thời gian, chuẩn hóa ảnh và tên tệp. Gaze, hành vi lấy mẫu ảnh ở 2 FPS; mắt/ngáp ở 10 FPS. Đây là tần suất chuẩn bị dữ liệu, không phải tốc độ hệ thống đã đạt trên webcam.

Phân hoạch được tách theo người: train 1, 6, 9, 10, 14, 28, 33, 37; validation 5, 13, 29; test 7, 23, 36. Người 28 không có trong phần Drowsiness đang sử dụng. Số mẫu ảnh lần lượt 2.435, 29.583 và 23.558 cho ba phần. Các khung hình tương quan, nên không xem tổng số ảnh là số quan sát độc lập.

### Giai đoạn 4: hoàn thiện Gaze

Gaze nhận diện chín vùng nhìn. Sau các thử nghiệm biểu diễn ảnh, phương án cuối dùng ảnh mặt và dải mắt với ResNet18 chia sẻ bộ mã hóa. Mỗi vùng tạo vector 512 chiều; vector ghép 1.024 chiều được đưa vào đầu phân loại. Vùng mắt thiếu được biểu diễn theo quy tắc cố định, không tạo thêm chi tiết giả.

So sánh validation ba seed cho thấy macro-F1 trung bình tăng từ 62,96% với chỉ mặt lên 77,36% khi kết hợp mặt và mắt. Mô hình chọn seed 43, epoch 7; macro-F1 ảnh test 84,22%. Đây là so sánh trong cùng quy trình, không phải tuyên bố hơn mọi phương pháp trong tài liệu. Gaze vẫn còn các lớp khó như front_right và left_mirror.

### Giai đoạn 5: điều chỉnh mục tiêu mắt và ngáp

Phương án bốn trạng thái mắt được thu hẹp thành hai trạng thái ổn định close/open. Nhãn closing/opening được bỏ qua ở mất mát và đánh giá đầu mắt, nhưng ảnh vẫn có thể đóng góp vào đầu ngáp nếu nhãn ngáp hợp lệ. Mô hình dùng một ResNet18 và hai đầu phân loại.

Quyết định này phù hợp mục tiêu nhận diện nhắm mắt kéo dài, đồng thời làm thay đổi bài toán. Không được lấy chênh lệch F1 bốn lớp và hai lớp làm bằng chứng thuần túy rằng mạng đã tốt hơn trên cùng nhiệm vụ. Mô hình cuối seed 43, epoch 6 đạt F1 ảnh test 96,95% cho mắt và 84,28% cho ngáp. Ngáp là tín hiệu hỗ trợ, không đủ để xác định buồn ngủ sinh lý.

### Giai đoạn 6: nhận diện 11 hành vi

Nhánh hành vi dùng ảnh toàn khung hình thấy thân, tay và đối tượng tương tác. Các lớp gồm lái xe bình thường, gọi điện/nhắn tin trái phải, uống nước, chỉnh tóc/trang điểm, radio, với ra sau, với sang bên, nói chuyện với hành khách. change_gear và standstill_or_waiting không thuộc cấu hình 11 lớp, không được gán lại thành safe_drive.

Mô hình chọn seed 43, epoch 8, macro-F1 test 77,96%. Các lớp nói chuyện và với ra sau còn yếu. Khi demo bằng laptop chỉ thấy mặt, không thể lấy kết quả nhánh hành vi để đánh giá công bằng mô hình. Vì vậy, chương trình yêu cầu người dùng bật rõ tùy chọn thấy thân và tay.

### Giai đoạn 7: từ phân loại ảnh sang cảnh báo

Chính sách v1 dựa trên điều kiện liên tục có recall thấp trên validation. V2 dùng tích lũy theo cửa sổ; nhánh hành vi còn báo nhầm. V3 chia hành vi thành nhóm điện thoại, nhóm khác và nói chuyện, dùng ngưỡng và thời gian khác nhau, cùng cơ chế bật/tắt và chống lặp.

Trong kiểm tra chọn chính sách luân phiên để riêng một người, nhánh hành vi v2 phát hiện 70/83 sự kiện với 32 lần bắt đầu sai; v3 là 72/83 với 3 lần bắt đầu sai. Đây là kết quả phát triển chính sách trên validation đã được dùng lặp lại, không phải test độc lập của cả quy trình. Những cải thiện này không đến từ huấn luyện lại trọng số mạng ở bước đó.

### Giai đoạn 8: khóa và đánh giá cuối

Ba checkpoint và chính sách được khóa trước đánh giá thời gian. Trên 21 video, hệ thống phát hiện 10/10 nhìn lệch, 21/22 nhắm mắt kéo dài, 91/98 hành vi. Số lần bắt đầu sai trên đoạn âm là 1, 7, 2; số lần bắt đầu trong vùng chưa rõ nhãn là 25, 36, 5.

Cần giữ ca trễ hành vi 38,98 giây trong phần bàn luận. Một cảnh báo xuất hiện muộn vẫn có thể được tính là phát hiện theo phép chồng lấp; vì vậy recall cao không đồng nghĩa cảnh báo luôn kịp thời. Nhóm test đã được đánh giá ảnh trước đó, nên đánh giá video là đánh giá bổ sung theo thời gian trên nhóm hiện có.

### Giai đoạn 9: tách repo kết quả và chuẩn bị demo

Repo hiện tại đóng gói đúng các trọng số đã kiểm chứng, không huấn luyện thêm hoặc thay ngưỡng. Mã demo mới sử dụng cùng bộ suy luận và chính sách khóa; bổ sung camera/video, cửa sổ hiển thị, kiểm tra tài sản và nhật ký tùy chọn. Đây là thay đổi phục vụ trình diễn, không tự tạo thêm bằng chứng về chất lượng.

## 4. Phân rã hệ thống cho người viết báo cáo

| Phần | Vai trò | Tệp chính | Điều cần mô tả |
|---|---|---|---|
| Đầu vào và giao diện demo | Đọc camera/video, hiển thị | `demo.py` | Góc camera, thời gian, không lật ảnh khi suy luận |
| Tiền xử lý | Cắt mặt/mắt, letterbox, JPEG convention | `driver_system/preprocess.py` | Nhất quán với huấn luyện; thiếu mặt không phải an toàn |
| Mã hóa Gaze | Trích xuất đặc trưng mặt/mắt | `driver_system/gaze_runtime.py` | Chia sẻ encoder, ghép đặc trưng, chín lớp |
| Mắt/ngáp và hành vi | Nạp checkpoint, suy luận đầu ra | `driver_system/runtime.py` | Hai đầu mắt/ngáp, 11 lớp hành vi, thứ tự lớp |
| Chính sách cửa sổ | Gaze và mắt theo thời gian | `driver_system/window_policy.py` | Tỷ lệ thời gian dương, yêu cầu đủ quan sát |
| Chính sách hành vi | Gom nhóm, ngưỡng bật/tắt | `driver_system/action_policy.py` | Điện thoại/khác/nói chuyện và độ trễ |
| Khóa và kiểm tra | Bảo đảm đúng bộ đã đánh giá | `config/final_lock.json`, `verify_setup.py` | Mã băm, danh sách lớp, policy không thay đổi |
| Kết quả | Các chỉ số đã kiểm chứng | `reports/` | Phạm vi mẫu và định nghĩa sự kiện |
| Tài liệu | Bản thảo và minh chứng | `docs/` | Phân biệt hoàn thành với dự kiến |

## 5. Phân công nội dung báo cáo theo cấu trúc hiện có

### Phần mở đầu

Viết vấn đề nghiên cứu và phạm vi “dấu hiệu quan sát được”. Tránh đồng nhất nhìn ngoài front với nguy hiểm hoặc mắt nhắm với chẩn đoán buồn ngủ. Lấy mục tiêu từ thuyết minh và đối chiếu mức hoàn thành thực tế, không viết lại mục tiêu theo hướng che các phần chưa làm.

### Chương 1: cơ sở lý thuyết

Giải thích ResNet18, học chuyển giao, phân loại nhiều đầu, vai trò điểm mốc mặt và xử lý thời gian. Phân biệt mô hình học từ dữ liệu với quy tắc cảnh báo. Không trình bày GRU/LSTM như thành phần đang chạy trong gói DMD cuối. Trích dẫn tài liệu gốc cho kiến trúc và dataset; số liệu dự án dẫn hồ sơ thực nghiệm.

### Chương 2: dữ liệu và phương pháp

Mô tả tách người, số mẫu từng tập, lấy mẫu, cắt vùng ảnh, nhãn thiếu, mất cân bằng và chọn checkpoint. Giải thích vì sao không lật ngang ảnh mang nhãn trái/phải. Nêu max 20 epoch và dừng sớm, không diễn giải epoch chọn thấp là chưa train đủ. Giữ test tách khỏi chọn tham số.

### Chương 3: thiết kế

Trình bày luồng video -> vùng ảnh -> ba mô hình -> xử lý thời gian -> cảnh báo. Có thể vẽ sơ đồ từ mô tả này. Gọi đây là hệ thống tích hợp các mô hình con, không phải một mạng được huấn luyện chung. Ghi rõ ba nhánh ban đầu dùng camera DMD tương ứng.

### Chương 4: xây dựng và tích hợp

Mô tả notebook, mã chuẩn bị, suy luận, kiểm tra phiên bản và đóng gói. Bổ sung demo webcam như phần triển khai mới với ngày kiểm thử và môi trường thực tế khi nhóm đã chạy. Chỉ dùng ảnh chụp màn hình có sự đồng ý; không lấy ảnh của participant DMD để công khai khi chưa rõ quyền sử dụng.

### Chương 5: kết quả và bàn luận

Giữ riêng ba nhóm bảng: chọn mô hình trên validation, phân loại ảnh test, sự kiện video. Dẫn số mẫu cho mỗi chỉ số. Phải có báo nhầm, unknown và độ trễ bên cạnh recall. Nêu hạn chế ba người, mẫu tương quan và tiêu chí chồng lấp chưa ghép một-một. Không thêm trung bình “độ chính xác toàn hệ thống” bằng cách cộng các nhánh.

### Kết luận và kiến nghị

Kết luận đã hoàn thiện nền tảng nhận diện và đánh giá nghiên cứu trên DMD. Chưa có căn cứ kết luận giảm tai nạn, đạt chuẩn an toàn, chạy realtime trên mọi máy hoặc nhận diện tốt người Việt. Hướng tiếp theo ưu tiên kiểm chứng góc camera và cảnh báo trên video mới trước khi đổi kiến trúc lớn.

## 6. Các tệp cần dùng để viết

- `FINAL_REPORT_VI.md` và `.txt`: bản đầy đủ đã mở rộng; không phải mẫu trắng.
- `RESULTS_DISCUSSION_VI.md`: phần kết quả ngắn, giữ các giới hạn quan trọng.
- `EVIDENCE_MAP.md`: chỉ dẫn số liệu và đường dẫn tương ứng trong repo này.
- `../MODEL_CARD.md`: cấu hình mô hình, intended use và giới hạn.
- `../reports/summary.csv`: bảng sự kiện để đối chiếu khi biên tập.

Các báo cáo cũ ghi đường dẫn của repo phát triển. Khi viết bản nộp, dùng bản đồ minh chứng của repo kết quả để dẫn nguồn hiện có. Không đổi ngày đánh giá thành ngày viết báo cáo hoặc ngày upload GitHub.

## 7. Checklist trước khi chốt bản nộp

1. Đối chiếu tên đề tài, mã số, thành viên và thông tin giảng viên với thuyết minh chính thức.
2. Mỗi bảng ghi đúng ảnh/video, validation/test, số mẫu và nguồn tệp.
3. Giữ nguyên các trường hợp bỏ sót và trễ; không chỉ chọn kết quả tốt.
4. Những mục chưa làm phải được đánh dấu hoặc chuyển sang hướng phát triển.
5. Demo có nhật ký và mô tả thiết bị; nếu chỉ kiểm tra chức năng thì không gọi là đánh giá độ chính xác.
6. Không sửa ngưỡng trên test; thử nghiệm thay đổi phải tạo phiên bản riêng.
7. Rà tài liệu tham khảo, quyền sử dụng hình ảnh và bỏ thông tin cá nhân không cần thiết.

## 8. Bước tiếp theo của nhóm

Mỗi thành viên cài repo, chạy kiểm tra tài sản và một video/webcam ngắn trong môi trường tĩnh. Người phụ trách tổng hợp lỗi cài đặt, khả năng quan sát, unknown và tốc độ trên máy. Sau khi luồng demo ổn định, chọn video mới và gán nhãn trước khi xem dự đoán để bổ sung một đánh giá độc lập. Chỉ sau bước đó mới cập nhật phần kiểm thử thực tế trong Google Docs và báo cáo tổng kết.
