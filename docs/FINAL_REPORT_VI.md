# BÁO CÁO TỔNG KẾT ĐỀ TÀI NGHIÊN CỨU KHOA HỌC CỦA SINH VIÊN

## XÂY DỰNG HỆ THỐNG AI NHẬN DIỆN TRẠNG THÁI BUỒN NGỦ HOẶC MẤT TẬP TRUNG CỦA TÀI XẾ

Mã số đề tài: THS2026-77.

Đơn vị: Trường Công nghệ thông tin và Truyền thông, Đại học Cần Thơ.

Chủ nhiệm đề tài: Huỳnh Phúc Hà.

Thành viên: Huỳnh Phúc Hà, Nguyễn Mai Mỹ An, Nguyễn Đình Khôi, Quang Nhựt Minh, Dương Trương Minh Toàn.

Người hướng dẫn: PGS.TS. Phạm Thế Phi.

Thời gian thực hiện theo thuyết minh: tháng 5 đến tháng 10 năm 2026.

Phạm vi cập nhật của báo cáo: kết quả có hồ sơ kiểm chứng đến ngày 08/10/2026. Những nội dung chưa hoàn thành được ghi rõ tại mục tương ứng. Báo cáo không xác nhận hoàn thành toàn bộ các sản phẩm đã đăng ký trong thuyết minh.

## CẤU TRÚC BÁO CÁO

Thông tin kết quả nghiên cứu; tóm tắt tiếng Việt và tiếng Anh; danh mục từ viết tắt.

PHẦN 1. MỞ ĐẦU

1. Tổng quan tình hình nghiên cứu.
2. Lý do chọn đề tài.
3. Mục tiêu nghiên cứu.
4. Đối tượng và phạm vi nghiên cứu.
5. Phương pháp nghiên cứu.
6. Cấu trúc nội dung.

PHẦN 2. NỘI DUNG VÀ KẾT QUẢ NGHIÊN CỨU

Chương 1. Cơ sở lý thuyết và các nghiên cứu liên quan.
Chương 2. Phương pháp nghiên cứu và xây dựng dữ liệu.
Chương 3. Phân tích và thiết kế hệ thống giám sát tài xế.
Chương 4. Xây dựng và tích hợp hệ thống.
Chương 5. Kết quả thực nghiệm và đánh giá.

PHẦN 3. KẾT LUẬN VÀ KIẾN NGHỊ

1. Kết luận.
2. Đóng góp của đề tài.
3. Hạn chế.
4. Kiến nghị và hướng phát triển.

Tài liệu tham khảo.
Phụ lục A. Hồ sơ kiểm chứng kết quả.
Phụ lục B. Nội dung cần bổ sung khi kiểm thử thực tế.

## THÔNG TIN KẾT QUẢ NGHIÊN CỨU

### 1. Mục tiêu đề tài

Xây dựng hệ thống xử lý hình ảnh để nhận diện các dấu hiệu liên quan đến buồn ngủ và mất tập trung của tài xế, từ đó hình thành cảnh báo theo thời gian. Hệ thống tập trung vào ba nhóm thông tin: vùng nhìn, trạng thái mắt và ngáp, hành vi của người lái.

### 2. Tính mới và sáng tạo trong phạm vi đề tài

Đề tài kết hợp các mô hình chuyên biệt với bộ xử lý thời gian, đồng thời tổ chức quy trình kiểm chứng từ dữ liệu, trọng số đến cấu hình cảnh báo. Đóng góp chủ yếu nằm ở việc xây dựng và đánh giá một hệ thống tích hợp có thể truy vết kết quả. Đề tài không đề xuất kiến trúc mạng nền mới và chưa có cơ sở khẳng định vượt trội so với các hệ thống giám sát tài xế hiện có.

### 3. Kết quả nghiên cứu chính

Đã chuẩn bị dữ liệu RGB từ ba phần của DMD; huấn luyện, lựa chọn và đánh giá ba mô hình; xây dựng chương trình suy luận trên video; khóa cấu hình cảnh báo trước đánh giá thời gian cuối. Trên 21 video thuộc ba người trong tập test, hệ thống phát hiện 10/10 sự kiện nhìn lệch, 21/22 sự kiện nhắm mắt kéo dài và 91/98 sự kiện hành vi theo định nghĩa tham chiếu của nghiên cứu.

Các kết quả này phản ánh khả năng phát hiện dấu hiệu được gán nhãn trong DMD. Chúng chưa chứng minh khả năng xác định buồn ngủ sinh lý hoặc hiệu quả cảnh báo khi vận hành trên xe thực tế.

### 4. Sản phẩm hiện có

Sản phẩm gồm mã nguồn chuẩn bị dữ liệu, notebook huấn luyện và đánh giá, ba bộ trọng số đã chọn, cấu hình cảnh báo đã khóa, chương trình chạy video và hồ sơ phân tích kết quả. Chưa hoàn thành kiểm thử webcam của bản tích hợp cuối, video demo và đánh giá toàn hệ thống trên thiết bị mục tiêu.

### 5. Khả năng ứng dụng và chuyển giao

Hệ thống có thể dùng làm nền tảng nghiên cứu, giảng dạy và thử nghiệm giám sát hành vi từ video. Khả năng ứng dụng trên phương tiện thực tế cần được kiểm chứng thêm về góc camera, ánh sáng, độ trễ, cảnh báo nhầm và dữ liệu người dùng mới. Chưa có kết quả chuyển giao hoặc đo lường hiệu quả kinh tế, xã hội.

## TÓM TẮT

Đề tài xây dựng hệ thống AI nhận diện các dấu hiệu liên quan đến buồn ngủ và mất tập trung của tài xế từ video RGB. Phương án triển khai gồm ba mô hình chuyên biệt: nhận diện chín vùng nhìn bằng đặc trưng khuôn mặt và vùng mắt; phân loại trạng thái mắt cùng ba trạng thái ngáp; nhận diện 11 hành vi của tài xế. Các mô hình sử dụng nền ResNet18 và được tinh chỉnh trên dữ liệu DMD với tập huấn luyện, validation và test tách theo người tham gia. Kết quả phân loại được xử lý theo thời gian để hạn chế cảnh báo do dao động tức thời.

Trên tập ảnh test, macro-F1 đạt 84,22% cho vùng nhìn, 96,95% cho trạng thái mắt, 84,28% cho ngáp và 77,96% cho hành vi. Khi giữ nguyên trọng số và cấu hình cảnh báo để đánh giá trên 21 video, recall sự kiện tham chiếu đạt lần lượt 100,00%, 95,45% và 92,86% đối với nhìn lệch, nhắm mắt kéo dài và hành vi. Tuy nhiên, vẫn xuất hiện cảnh báo sai và một trường hợp hành vi có độ trễ khoảng 38,98 giây sau mốc tham chiếu. Hệ thống hiện là bản nghiên cứu đã đánh giá trên dữ liệu ghi sẵn, chưa được xác nhận về hiệu quả cảnh báo trên webcam hoặc khi lái xe thực tế.

Từ khóa: giám sát tài xế, mất tập trung, trạng thái mắt, vùng nhìn, DMD, ResNet18.

## ABSTRACT

This study develops an RGB video-based system for recognizing visual cues associated with driver drowsiness and distraction. Three specialized ResNet18-based models recognize nine gaze regions, eye and yawning states, and eleven driver actions. DMD data are partitioned by participant into training, validation, and test sets. Temporal decision rules convert frame predictions into alerts.

On the prepared test images, macro-F1 scores are 84.22% for gaze, 96.95% for eye state, 84.28% for yawning, and 77.96% for driver actions. With model weights and alert parameters frozen, an additional evaluation on 21 videos detects 10/10 gaze-away events, 21/22 prolonged eye-closure events, and 91/98 action events under the study's reference definitions. False alerts and delayed detections remain, including an action detection delay of approximately 38.98 seconds after the reference onset. These results concern annotated visual cues rather than physiological drowsiness or verified driving risk. The integrated system has not yet undergone final webcam or real-world driving validation.

Keywords: driver monitoring, distraction, eye state, gaze, DMD, ResNet18.

## DANH MỤC TỪ VIẾT TẮT

AI: Artificial Intelligence, trí tuệ nhân tạo.
CNN: Convolutional Neural Network, mạng nơ-ron tích chập.
DMD: Driver Monitoring Dataset, bộ dữ liệu giám sát tài xế của Vicomtech và cộng sự.
DMS: Driver Monitoring System, hệ thống giám sát tài xế.
RGB: Red, Green, Blue, ảnh màu ba kênh.
GRU: Gated Recurrent Unit, một dạng mạng nơ-ron hồi tiếp.
EAR: Eye Aspect Ratio, tỷ lệ hình học vùng mắt.
MAR: Mouth Aspect Ratio, tỷ lệ hình học vùng miệng.
FPS: Frames Per Second, số khung hình mỗi giây.
GPU: Graphics Processing Unit, bộ xử lý đồ họa.
LOSO: Leave-One-Subject-Out, đánh giá luân phiên để riêng một người.

# PHẦN 1. MỞ ĐẦU

## 1. Tổng quan tình hình nghiên cứu

### 1.1. Tình hình nghiên cứu trong nước

Các nghiên cứu trong nước đã tiếp cận việc nhận diện dấu hiệu buồn ngủ thông qua xử lý ảnh khuôn mặt và mắt. Trương Quốc Bảo, Trương Quốc Định và Đinh Thành Nhân trình bày phương pháp xác định trạng thái nhắm, mở mắt bằng xử lý ảnh và phân lớp HOG-SVM [1]. Công trình cho thấy trạng thái mắt là một tín hiệu có thể khai thác bằng thị giác máy tính, nhưng nhận diện mắt không đồng nghĩa với đánh giá đầy đủ mức độ tập trung của người lái.

Đề tài kế thừa hướng tiếp cận từ camera và mở rộng phạm vi sang vùng nhìn cùng hành vi. Báo cáo không so sánh định lượng trực tiếp với công trình trên do khác dữ liệu, cách chia tập và định nghĩa nhiệm vụ.

### 1.2. Tình hình nghiên cứu ngoài nước

Albadawi và cộng sự tổng hợp các hướng phát hiện buồn ngủ dựa trên tín hiệu sinh lý, đặc điểm hình ảnh và hành vi vận hành phương tiện [2]. Mỗi nguồn thông tin có yêu cầu thiết bị và giới hạn riêng. Đối với phạm vi đề tài sinh viên, camera RGB tạo điều kiện triển khai và phân tích dữ liệu mà không yêu cầu cảm biến sinh lý gắn trên người.

Ortega và cộng sự giới thiệu DMD với các tình huống liên quan đến hướng nhìn, buồn ngủ và hành vi, được ghi từ nhiều camera và loại cảm biến [3]. Đề tài chỉ sử dụng phần RGB đã chuẩn bị cho ba nhiệm vụ, không sử dụng toàn bộ dữ liệu hoặc tất cả phương thức cảm biến của DMD.

### 1.3. Vấn đề nghiên cứu

Một bộ phân loại ảnh có kết quả tốt chưa bảo đảm cảnh báo hữu ích trên video. Dự đoán có thể thay đổi giữa các khung hình, một hành vi ngắn có thể hợp lệ theo ngữ cảnh, và cảnh báo đúng nhưng quá chậm vẫn hạn chế giá trị sử dụng. Vì vậy, nghiên cứu cần đánh giá cả nhận diện từng ảnh và xử lý sự kiện theo thời gian, thay vì chỉ báo cáo độ chính xác phân loại.

Từ vấn đề trên, đề tài tập trung vào ba câu hỏi nghiên cứu. Thứ nhất, thông tin khuôn mặt, vùng mắt và toàn thân hỗ trợ nhận diện từng nhóm dấu hiệu đến mức nào trên phần dữ liệu được chọn? Thứ hai, cách xử lý đầu ra theo thời gian ảnh hưởng ra sao đến phát hiện và báo nhầm? Thứ ba, kết quả trên dữ liệu ghi sẵn cho phép kết luận điều gì về hệ thống, và còn thiếu những bằng chứng nào trước khi triển khai trực tiếp? Các câu hỏi này định hướng việc thiết kế thực nghiệm và giới hạn phạm vi kết luận.

## 2. Lý do chọn đề tài

Buồn ngủ và mất tập trung có thể biểu hiện qua nhiều dấu hiệu khác nhau. Chỉ theo dõi mắt có thể bỏ qua sử dụng điện thoại, quay người hoặc nhìn ra ngoài hướng quan sát phía trước. Ngược lại, chỉ phân loại hành vi toàn khung hình có thể không đủ chi tiết để nhận diện trạng thái mắt.

Do đó, đề tài xây dựng hệ thống gồm các mô hình chuyên biệt và một cơ chế tổng hợp theo thời gian. Cách tổ chức này phù hợp với mục tiêu nhận diện nhiều dấu hiệu trong thuyết minh, đồng thời cho phép kiểm tra riêng chất lượng của từng thành phần.

## 3. Mục tiêu nghiên cứu

### 3.1. Mục tiêu tổng quát

Xây dựng và đánh giá hệ thống AI nhận diện dấu hiệu buồn ngủ hoặc mất tập trung của tài xế từ hình ảnh, hướng đến cảnh báo kịp thời và hạn chế báo nhầm.

### 3.2. Mục tiêu cụ thể

- Xây dựng quy trình chuẩn bị dữ liệu có nhãn, kiểm tra chất lượng và tách tập theo người tham gia.
- Huấn luyện các mô hình nhận diện vùng nhìn, trạng thái mắt, ngáp và hành vi.
- Thiết kế quy tắc cảnh báo theo thời gian từ đầu ra mô hình.
- Đánh giá khả năng phân loại, phát hiện sự kiện, cảnh báo sai và độ trễ.
- Chuẩn bị mô hình và chương trình suy luận phục vụ kiểm thử thực tế ở giai đoạn tiếp theo.

Các mục tiêu về dữ liệu người Việt, thử nghiệm NTHU, tối ưu trên thiết bị hạn chế và demo trực tiếp chưa được xem là hoàn thành trong báo cáo này.

## 4. Đối tượng và phạm vi nghiên cứu

### 4.1. Đối tượng nghiên cứu

Đối tượng nghiên cứu là các dấu hiệu quan sát được từ video: vùng nhìn, mắt nhắm hoặc mở, biểu hiện ngáp và một số hành vi liên quan đến mất tập trung. Dữ liệu đầu vào là hình ảnh RGB có nhãn; đầu ra là dự đoán từng nhiệm vụ và trạng thái cảnh báo theo thời gian.

### 4.2. Phạm vi nghiên cứu

Thực nghiệm chính sử dụng phần dữ liệu DMD đã chuẩn bị. Các nhánh được đánh giá trên góc camera tương ứng: camera mặt cho vùng nhìn, mắt và ngáp; camera thân cho hành vi. Chưa có thực nghiệm xác nhận đồng thời cả ba nhánh trên cùng một góc webcam triển khai.

Đề tài không đo tín hiệu sinh lý và không xác định trực tiếp mức độ buồn ngủ y khoa. Nhãn nhìn ngoài phía trước cũng không tự động tương đương hành vi nguy hiểm, vì nhìn gương có thể là thao tác cần thiết. Phần cứng nhúng, điều khiển phương tiện và đánh giá an toàn giao thông thực địa nằm ngoài phần đã hoàn thành.

Về thuật ngữ, báo cáo sử dụng “nhận diện dấu hiệu” khi đề cập đến đầu ra thị giác và “cảnh báo” khi dấu hiệu đạt điều kiện thời gian. “Mất tập trung” trong tên đề tài thể hiện mục tiêu ứng dụng rộng hơn, còn phép đo hiện tại chủ yếu phản ánh vùng nhìn và hành vi có thể quan sát. Chưa đánh giá được trường hợp người lái nhìn thẳng nhưng mất tập trung về nhận thức. Sự phân biệt này tránh mở rộng kết luận vượt quá thông tin mà camera và nhãn dữ liệu cung cấp.

## 5. Phương pháp nghiên cứu

Nghiên cứu kết hợp khảo cứu tài liệu, xây dựng dữ liệu, học chuyển giao và thực nghiệm định lượng. Mô hình được lựa chọn bằng kết quả validation; bộ test dùng để báo cáo sau khi lựa chọn. Quy tắc cảnh báo được phát triển trên video validation rồi khóa trước đánh giá thời gian cuối. Các tệp cấu hình, trọng số và kết quả được lưu để đối chiếu và tái lập.

## 6. Cấu trúc nội dung

Phần 2 gồm năm chương. Chương 1 trình bày cơ sở lý thuyết; Chương 2 mô tả dữ liệu và thực nghiệm; Chương 3 trình bày thiết kế hệ thống; Chương 4 nêu các thành phần đã xây dựng; Chương 5 phân tích kết quả và giới hạn. Phần 3 tổng kết đóng góp, hạn chế và hướng phát triển.

# PHẦN 2. NỘI DUNG VÀ KẾT QUẢ NGHIÊN CỨU

## CHƯƠNG 1. CƠ SỞ LÝ THUYẾT VÀ CÁC NGHIÊN CỨU LIÊN QUAN

### 1.1. Biểu diễn bài toán giám sát tài xế

Ở mức ảnh, hệ thống học ánh xạ từ hình ảnh đến các lớp đã xác định. Ở mức video, chuỗi đầu ra được kết hợp với mốc thời gian để hình thành sự kiện cảnh báo. Hai mức đánh giá giải quyết các câu hỏi khác nhau: ảnh được nhận diện đúng hay không, và sự kiện kéo dài có được cảnh báo với độ trễ phù hợp hay không.

Ba nhánh có vai trò bổ sung. Vùng nhìn phản ánh hướng quan sát; mắt và ngáp cung cấp dấu hiệu liên quan đến mức tỉnh táo; hành vi thể hiện những thao tác như sử dụng điện thoại hoặc với tay. Hệ thống chưa có đủ thông tin để suy luận đầy đủ nguyên nhân hoặc mức nguy hiểm của từng dấu hiệu.

### 1.2. Mạng tích chập và học chuyển giao

Mạng tích chập trích xuất đặc trưng hình ảnh qua nhiều tầng và sử dụng đặc trưng đó cho phân loại. Học chuyển giao sử dụng trọng số đã học trước làm điểm khởi đầu, sau đó tinh chỉnh trên dữ liệu của nhiệm vụ đích. Trong đề tài, mô hình nền được khởi tạo từ trọng số ImageNet, còn các đầu phân loại phù hợp với nhãn DMD được huấn luyện lại.

ResNet sử dụng các kết nối tắt để học phần dư của phép biến đổi, hỗ trợ tối ưu mạng sâu [4]. Đề tài sử dụng ResNet18 làm nền cho ba mô hình chuyên biệt. Việc lựa chọn này là quyết định thực nghiệm trong phạm vi dữ liệu hiện có, không phải kết luận ResNet18 tối ưu cho mọi hệ thống giám sát tài xế.

### 1.3. Định vị khuôn mặt và vùng mắt

MediaPipe Face Landmarker cung cấp các điểm mốc khuôn mặt, hỗ trợ xác định vùng mặt và mắt [5]. Đây là thành phần tiền huấn luyện được sử dụng lại, không phải mô hình do nhóm huấn luyện từ đầu.

Thuyết minh ban đầu đề cập phương án 68 điểm mốc. Bản triển khai sử dụng MediaPipe với 478 điểm mốc theo cấu hình Face Landmarker. Sự thay đổi thuộc khâu định vị vùng ảnh; không có nghĩa toàn bộ 478 điểm được đưa trực tiếp vào các mô hình ResNet18 cuối cùng.

### 1.4. Dấu hiệu hình học và mô hình chuỗi

EAR, MAR và tư thế đầu có thể được dùng làm đặc trưng mô tả trạng thái khuôn mặt. Ở giai đoạn khảo sát ban đầu, dự án đã xây dựng hướng xử lý đặc trưng và mô hình GRU trên RLDD. Hướng này phục vụ nghiên cứu chuỗi thời gian nhưng chưa bao phủ trực tiếp các hành vi mất tập trung.

Phương án cuối trong báo cáo dùng các mô hình ảnh DMD và bộ xử lý thời gian. Vì vậy, không trình bày GRU hoặc LSTM như thành phần đang thực hiện suy luận trong gói ba mô hình đã khóa.

### 1.5. Nhận diện nhiều nhiệm vụ và tích hợp nhiều mô hình

Mô hình nhiều đầu ra có thể chia sẻ một bộ trích xuất đặc trưng nhưng sử dụng các đầu phân loại khác nhau. Nhánh mắt và ngáp của đề tài được tổ chức theo cách này.

Ở cấp hệ thống, ba mô hình có trọng số riêng và được phối hợp bằng bộ điều phối. Đây là hệ thống tích hợp nhiều mô hình, chưa phải một mạng duy nhất được huấn luyện đồng thời cho toàn bộ nhiệm vụ. Đặc điểm này phù hợp với định hướng mô-đun và nhiều dấu hiệu trong thuyết minh, nhưng cần được mô tả chính xác khi trình bày sản phẩm.

### 1.6. Cảnh báo theo thời gian

Ngưỡng phân loại tức thời có thể tạo cảnh báo dao động. Bộ xử lý thời gian bổ sung điều kiện về thời lượng, tỷ lệ mẫu đạt ngưỡng và trạng thái bật, tắt cảnh báo. Ngưỡng thấp thường tăng khả năng phát hiện nhưng cũng có thể tăng báo nhầm; thời gian chờ dài có thể giảm dao động nhưng làm cảnh báo muộn.

Trong nghiên cứu, các tham số được lựa chọn trên validation. Giá trị softmax được dùng làm điểm số quyết định, chưa được xác nhận là xác suất đã hiệu chuẩn về mức độ nguy hiểm.

### 1.7. Các chỉ số đánh giá

Đối với mỗi lớp, precision = TP/(TP + FP), recall = TP/(TP + FN), F1 = 2 × precision × recall/(precision + recall). Macro-F1 là trung bình F1 của các lớp, giúp thể hiện chất lượng khi phân bố nhãn không đồng đều. Accuracy là tỷ lệ mẫu được phân loại đúng.

Đối với video, báo cáo sử dụng recall sự kiện, số lần bắt đầu cảnh báo trên đoạn âm, thời gian cảnh báo chồng đoạn âm và độ trễ. Đoạn âm là đoạn có nhãn tham chiếu không cảnh báo; đoạn chưa rõ nhãn được thống kê riêng. Không lấy số khung hình đúng thay thế cho mức hiệu quả của cảnh báo theo sự kiện.

Recall sự kiện được tính bằng số sự kiện tham chiếu có cảnh báo chồng lấp chia cho tổng số sự kiện tham chiếu. Tỷ lệ thời gian cảnh báo sai được tính bằng tổng thời gian cảnh báo chồng đoạn âm chia cho tổng thời gian âm có nhãn. Hai đại lượng này lần lượt mô tả khả năng phát hiện và mức xuất hiện cảnh báo ở các khoảng không yêu cầu cảnh báo theo nhãn tham chiếu.

Độ trễ cho biết thời gian từ mốc tham chiếu đến lần cảnh báo đầu tiên trong sự kiện, quy về 0 nếu cảnh báo đã hoạt động tại mốc đó. P95 mô tả phân vị 95% của các độ trễ quan sát được; khi số sự kiện ít, chỉ số này cần được đọc cùng giá trị lớn nhất và số lượng mẫu. Những sự kiện không được phát hiện phải được báo cáo riêng, vì loại chúng khỏi thống kê độ trễ có thể làm kết quả thời gian trông tốt hơn khả năng phát hiện thực tế.

### 1.8. Cơ sở lựa chọn hướng tiếp cận

Đề tài lựa chọn kết hợp phân loại ảnh và xử lý thời gian để tách hai nguồn sai số. Sai số nhận diện được xem xét qua nhầm lẫn giữa các lớp; sai số quyết định được xem xét qua ngưỡng, thời gian tích lũy và trạng thái cảnh báo. Việc tách này giúp xác định trường hợp cần bổ sung dữ liệu hoặc huấn luyện lại, và trường hợp có thể xử lý bằng điều chỉnh quy tắc trên validation.

Phương án cũng có giới hạn: bộ xử lý thời gian không học trực tiếp chuyển động từ ảnh và không thể khôi phục thông tin mà mô hình ảnh đã nhận diện sai liên tục. Vì vậy, chính sách cảnh báo chỉ là một thành phần bổ sung cho mô hình thị giác. Khi có đủ dữ liệu chuỗi và nguồn lực, mô hình học đặc trưng không gian, thời gian có thể được nghiên cứu như một hướng thay thế, nhưng chưa được xem là kết quả của bản hiện tại.

## CHƯƠNG 2. PHƯƠNG PHÁP NGHIÊN CỨU VÀ XÂY DỰNG DỮ LIỆU

### 2.1. Quy trình nghiên cứu

Quy trình gồm: lựa chọn nhiệm vụ và dữ liệu; kiểm tra video, nhãn và thời gian; trích xuất ảnh; chia tập theo người; huấn luyện các cấu hình; chọn trọng số trên validation; đánh giá ảnh; phát triển chính sách cảnh báo trên video validation; khóa cấu hình; đánh giá thời gian cuối và phân tích lỗi.

Việc tách các giai đoạn giúp phân biệt cải thiện mô hình ảnh với cải thiện quy tắc cảnh báo. Những thay đổi của chính sách không được gọi là huấn luyện thêm mạng nơ-ron.

### 2.2. Nguồn dữ liệu

DMD là nguồn dữ liệu chính của bản hệ thống hiện tại [3]. Ba phần được sử dụng là Gaze, Drowsiness và Distraction. Nhóm khai thác video RGB cùng nhãn đi kèm, sau đó chuẩn bị dữ liệu theo yêu cầu của từng mô hình.

RLDD đã được dùng trong giai đoạn khảo sát mô hình chuỗi. NTHU được nêu trong định hướng của thuyết minh nhưng chưa có kết quả huấn luyện hoặc đánh giá NTHU được kiểm chứng cho bản báo cáo này. Chưa có bộ dữ liệu người Việt do nhóm thu thập và hoàn tất đánh giá.

Lý do tập trung vào DMD là khả năng tổ chức các nhiệm vụ vùng nhìn, mắt, ngáp và hành vi trong cùng một nguồn dữ liệu, thuận lợi cho xây dựng quy trình chuẩn bị và đánh giá thống nhất. Tuy vậy, “cùng nguồn dữ liệu” không đồng nghĩa mọi nhiệm vụ dùng chung video, camera hoặc nhãn đồng thời. Bản thực nghiệm sử dụng các phần được chuẩn bị cho từng nhánh, không đại diện cho toàn bộ quy mô DMD được công bố.

### 2.3. Kiểm tra video và đồng bộ nhãn

Quá trình chuẩn bị kiểm tra khả năng giải mã video, tần số khung hình, chỉ số khung hình và khoảng nhãn trong dữ liệu OpenLABEL. Độ lệch thời gian giữa các camera được xử lý theo thông tin chú thích trước khi gán nhãn cho ảnh trích xuất.

Trường hợp số khung hình trong metadata khác số khung hình giải mã phải được kiểm tra thay vì tự động bỏ qua lỗi. Dữ liệu sau chuẩn bị được lưu cùng danh sách mẫu, mã người tham gia, phân hoạch và thông tin tiền xử lý. Tên tệp được chuẩn hóa để có thể đóng gói và sử dụng trên Kaggle.

### 2.4. Tiền xử lý và lấy mẫu

Đối với Gaze, dữ liệu ảnh được lấy mẫu ở 2 FPS. Ảnh mặt và dải mắt được chuẩn bị thành hai vùng 224 × 224, ghép ngang thành ảnh 448 × 224. Khi không lấy được vùng mắt, ô ảnh mắt được thay bằng vùng đen theo cấu hình đã xác định. Bộ dữ liệu Gaze có 82 mẫu thiếu vùng mắt trong tổng số 2.435 mẫu.

Đối với Drowsiness, ảnh được lấy mẫu ở 10 FPS, sử dụng vùng mặt với khung cắt vuông mở rộng và đưa về 224 × 224. Nhánh hành vi lấy mẫu ở 2 FPS và sử dụng toàn khung hình camera thân, thay đổi kích thước có đệm để giữ tỷ lệ ảnh.

Ảnh được chuẩn hóa theo cấu hình ImageNet. Tăng cường dữ liệu sử dụng biến đổi độ sáng và độ tương phản nhẹ. Không lật ngang ảnh do thao tác này có thể thay đổi ý nghĩa nhãn trái, phải. Tốc độ lấy mẫu là tham số chuẩn bị dữ liệu, không phải kết quả đo tốc độ xử lý của hệ thống.

### 2.5. Phân chia dữ liệu

Tập huấn luyện, validation và test được tách theo mã người tham gia nhằm hạn chế việc các ảnh gần nhau của cùng người xuất hiện ở nhiều tập. Phân hoạch cấu hình gồm: train với các mã 1, 6, 9, 10, 14, 28, 33, 37; validation với 5, 13, 29; test với 7, 23, 36. Phần Drowsiness đang sử dụng không có dữ liệu người 28.

Bảng 2.1. Số mẫu ảnh đã chuẩn bị.

| Nhánh | Train | Validation | Test | Tổng |
|---|---:|---:|---:|---:|
| Gaze | 1.379 | 449 | 607 | 2.435 |
| Drowsiness | 16.570 | 5.384 | 7.629 | 29.583 |
| Distraction | 13.000 | 4.237 | 6.321 | 23.558 |

Số mẫu Drowsiness trong bảng là số ảnh, không đồng nghĩa tất cả đều có nhãn mắt hợp lệ cho bài toán nhị phân. Tập test có 5.355 mẫu mắt nhắm hoặc mở ổn định được dùng để đánh giá đầu mắt. Các ảnh liên tiếp vẫn tương quan theo thời gian, vì vậy số ảnh lớn không tương đương số quan sát độc lập lớn.

Việc chia ngẫu nhiên từng khung hình không phù hợp với mục tiêu đánh giá trên người chưa có trong tập huấn luyện. Những khung hình gần nhau có thể chứa cùng khuôn mặt, trang phục, nền và tư thế, làm giảm mức khác biệt giữa train và test. Vì vậy, chương trình kiểm tra giao nhau theo người, phiên ghi hình và đường dẫn ảnh trước khi huấn luyện. Tách theo người giảm một nguồn rò rỉ dữ liệu quan trọng, nhưng không loại bỏ toàn bộ tương đồng về môi trường hoặc thiết bị ghi hình giữa các tập.

### 2.6. Tổ chức nhãn

Gaze gồm chín vùng: gương giữa, phía trước, phía trước bên phải, khu vực giải trí, bên trái, gương trái, bên phải, gương phải và vô lăng.

Drowsiness sử dụng hai đầu phân loại. Đầu mắt nhận diện close và open. Hai trạng thái chuyển tiếp closing, opening không tham gia tính mất mát và chỉ số của đầu mắt; ảnh vẫn có thể được sử dụng cho đầu ngáp nếu có nhãn hợp lệ. Đầu ngáp gồm không ngáp, ngáp có tay che và ngáp không có tay che.

Distraction gồm 11 lớp: uống nước, chỉnh tóc hoặc trang điểm, gọi điện trái, gọi điện phải, chỉnh radio, với ra ghế sau, với sang bên, lái xe bình thường, nói chuyện với hành khách, nhắn tin trái và nhắn tin phải. Hai nhãn change_gear và standstill_or_waiting không thuộc cấu hình 11 lớp do giới hạn độ phủ dữ liệu trong thiết kế hiện tại; chúng không được đổi thành nhãn lái xe bình thường.

Đối với đầu mắt, loại trạng thái chuyển tiếp khỏi hàm mất mát giúp tập trung vào hai trạng thái quan sát ổn định. Cách làm này đồng thời thu hẹp nhiệm vụ: mô hình cuối không được đánh giá về khả năng phân biệt mắt đang đóng với mắt đang mở. Tương tự, các đoạn chưa có nhãn hợp lệ không được suy diễn thành mẫu âm. Đây là những quy tắc xử lý nhãn cần giữ nguyên khi tái lập hoặc mở rộng bộ dữ liệu.

### 2.7. Cấu hình huấn luyện

Mô hình được huấn luyện bằng PyTorch với bộ tối ưu AdamW. Tốc độ học khởi đầu là 0,0001 cho bộ trích xuất đặc trưng và 0,0005 cho đầu phân loại; weight decay là 0,001. Cấu hình sử dụng dropout 0,2, label smoothing 0,05 và giới hạn chuẩn gradient ở 1.

Hai epoch đầu giữ cố định bộ trích xuất đặc trưng, sau đó tinh chỉnh mô hình. Số epoch tối đa là 20; có giảm tốc độ học và dừng sớm khi điểm validation không cải thiện. Vì vậy, epoch tốt nhất có thể nhỏ hơn 20 mà không có nghĩa quá trình huấn luyện chưa hoàn tất.

Thực nghiệm sử dụng ba seed 42, 43 và 44. Lấy mẫu có trọng số theo lớp và người tham gia giúp giảm ảnh hưởng của mất cân bằng. Với mô hình nhiều đầu ra, mất mát được tính trên các nhãn hợp lệ. Trọng số được chọn theo macro-F1 validation; riêng Drowsiness dùng trung bình macro-F1 của hai đầu.

Với đầu ra h, hàm mất mát được tính trên tập mẫu có nhãn hợp lệ V_h. Mất mát của một lô là trung bình các mất mát cross-entropy của những đầu có ít nhất một nhãn hợp lệ trong lô đó. Do đó, một ảnh bị bỏ qua ở đầu mắt vẫn có thể đóng góp vào học đặc trưng qua đầu ngáp. Nhãn thiếu không được thay bằng một lớp bất kỳ để đủ số lượng mẫu.

Chọn trọng số theo trung bình macro-F1 của hai đầu thể hiện yêu cầu duy trì cả hai nhiệm vụ. Nếu chỉ tối ưu đầu mắt, mô hình có thể được chọn dù kết quả ngáp kém hơn. Tuy nhiên, lấy trung bình cũng là một quy ước thiết kế, chưa phải trọng số phản ánh mức quan trọng thực tế của từng loại cảnh báo.

### 2.8. Thiết kế đánh giá và kiểm soát sai lệch

Đánh giá ảnh sử dụng nhãn có điểm số lớn nhất, không điều chỉnh ngưỡng bằng tập test. Sau đó, các video validation của người 5, 13 và 29 được dùng để phát triển bộ xử lý thời gian. Có kiểm tra luân phiên để riêng một người đối với chính sách; đây chỉ là kiểm tra ở mức chọn quy tắc, không phải LOSO độc lập cho toàn bộ quá trình huấn luyện mô hình.

Trọng số và chính sách cuối được lưu bằng mã băm trước khi chạy đánh giá thời gian. Tập video cuối gồm người 7, 23 và 36. Những người này đã được đánh giá ở mức ảnh, nên thực nghiệm video là đánh giá bổ sung theo thời gian trên nhóm test hiện có, không phải một quần thể hoàn toàn mới.

### 2.9. Mất cân bằng và độ phủ dữ liệu

Trong tập huấn luyện Distraction, lớp safe_drive có 5.067 mẫu, trong khi reach_backseat chỉ có 205 mẫu và talking_to_passenger có 369 mẫu. Ở Drowsiness, số mẫu mắt mở ổn định là 10.966, cao hơn số mẫu nhắm mắt là 1.760. Những khác biệt này là cơ sở để sử dụng macro-F1 và lấy mẫu có trọng số, thay vì chỉ tối ưu tỷ lệ đúng trên toàn tập.

Lấy mẫu lại làm thay đổi tần suất xuất hiện của các mẫu trong huấn luyện, nhưng không tạo thêm người tham gia hoặc tình huống mới. Nếu một lớp chỉ có ít ví dụ đa dạng, việc lặp lại các mẫu vẫn có thể dẫn đến học phụ thuộc bối cảnh. Do đó, cân bằng tần suất là giải pháp hỗ trợ, không thay thế việc bổ sung dữ liệu đại diện.

### 2.10. Cấu trúc dữ liệu phục vụ tái lập

Mỗi mẫu được lưu cùng đường dẫn ảnh, mã người tham gia, phiên ghi hình, phân hoạch và nhãn của các đầu ra. Tệp metadata mô tả thứ tự lớp, kích thước ảnh và tiền xử lý. Thứ tự lớp phải thống nhất giữa dữ liệu, đầu phân loại và chương trình suy luận, vì cùng một chỉ số đầu ra có thể mang ý nghĩa khác nếu danh sách lớp thay đổi.

Các tệp manifest và metadata được lưu mã băm để phát hiện thay đổi ngoài dự kiến. Mã băm hỗ trợ kiểm tra đúng phiên bản dữ liệu, nhưng không chứng minh nhãn đúng về ngữ nghĩa hoặc video độc lập về nội dung. Hai yêu cầu sau vẫn cần kiểm tra dữ liệu và thiết kế thực nghiệm phù hợp.

## CHƯƠNG 3. PHÂN TÍCH VÀ THIẾT KẾ HỆ THỐNG GIÁM SÁT TÀI XẾ

### 3.1. Yêu cầu chức năng

Hệ thống cần đọc video, xác định vùng ảnh phù hợp, chạy các mô hình đã chọn, kết hợp dự đoán theo thời gian và lưu kết quả. Khi thiếu quan sát, hệ thống phải thể hiện trạng thái chưa xác định, tránh mặc định người lái đang an toàn. Các kết quả cần truy vết được về phiên bản mô hình và cấu hình cảnh báo.

### 3.2. Yêu cầu phi chức năng

Thiết kế ưu tiên khả năng tái lập, thay thế từng mô-đun và kiểm tra lỗi. Khả năng hoạt động thời gian thực là yêu cầu hướng tới, chưa phải thuộc tính đã được xác nhận cho toàn bộ hệ thống. Hiệu quả triển khai còn phụ thuộc thiết bị, góc camera và chất lượng ảnh đầu vào.

### 3.3. Kiến trúc tổng thể

Luồng xử lý được mô tả như sau:

Video RGB → giải mã và lấy mẫu → chuẩn bị vùng ảnh → các mô hình chuyên biệt → xử lý thời gian → trạng thái cảnh báo và nhật ký kết quả.

Nhánh mặt phục vụ Gaze và Drowsiness; nhánh toàn khung hình có thân và tay phục vụ Distraction. Bộ điều phối lưu riêng các loại tín hiệu. Hệ thống chưa có một chỉ số nguy cơ tổng hợp đã được hiệu chuẩn hoặc đánh giá độc lập.

### 3.4. Thiết kế các mô hình

Mô hình Gaze dùng ResNet18 chia sẻ bộ mã hóa cho ảnh mặt và ảnh mắt. Hai vector đặc trưng được ghép trước lớp phân loại chín vùng nhìn. Thiết kế này cho phép khai thác thông tin tổng thể của khuôn mặt cùng chi tiết ở mắt.

Mô hình Drowsiness dùng một bộ mã hóa ResNet18 và hai đầu phân loại riêng cho mắt, ngáp. Mô hình Distraction dùng ResNet18 với đầu ra 11 lớp từ ảnh camera thân. Ba bộ trọng số được giữ riêng để kiểm tra và cập nhật độc lập.

Cụ thể, gọi E là bộ mã hóa ResNet18, x_f là ảnh mặt và x_e là ảnh mắt. Biểu diễn của Gaze có dạng z = [E(x_f), mE(x_e)], trong đó m = 1 khi có vùng mắt hợp lệ và m = 0 khi thiếu vùng mắt. Mỗi nhánh tạo vector 512 chiều; ghép hai nhánh tạo vector 1.024 chiều cho đầu phân loại. Việc đặt đặc trưng mắt bằng 0 khi thiếu ảnh tránh đưa một vùng thay thế vào mô hình như thể đó là mắt quan sát được.

Chia sẻ bộ mã hóa giúp hai vùng ảnh dùng chung trọng số, nhưng vẫn phải xử lý cả hai vùng ở bước suy luận. Vì vậy, không thể suy ra chi phí tính toán của Gaze bằng đúng một lần phân loại ảnh mặt. Mặt khác, ghép đặc trưng tạo điều kiện để đầu phân loại sử dụng đồng thời thông tin tư thế mặt và chi tiết mắt, thay vì chỉ nhận ảnh ghép như một khung hình thông thường.

Đối với Drowsiness, có thể biểu diễn đầu ra là y_mắt = H_mắt(E(x_f)) và y_ngáp = H_ngáp(E(x_f)). Hai đầu dùng chung đặc trưng ảnh mặt nhưng có số lớp và nhãn hợp lệ khác nhau. Nhánh Distraction dùng biểu diễn E(x_b) của ảnh thân x_b. Cách phân tách đầu vào này giải thích vì sao không thể xem ba mô hình là những bộ phân loại có thể thay thế lẫn nhau.

### 3.5. Thiết kế chính sách cảnh báo cuối

Nhánh mắt dùng điểm số close; nhánh nhìn lệch dùng 1 - P(front). Hai nhánh này xét tỷ lệ thời gian có bằng chứng vượt ngưỡng trong cửa sổ quan sát. Nhánh hành vi cộng điểm số theo ba nhóm và sử dụng điều kiện duy trì cùng ngưỡng bật, tắt khác nhau.

Bảng 3.1. Các tham số chính của chính sách đã khóa.

| Tín hiệu | Ngưỡng bật | Điều kiện thời gian |
|---|---:|---|
| Mắt nhắm | 0,40 | Cửa sổ 0,8 giây; tỷ lệ thời gian dương 0,60 |
| Nhìn ngoài front | 0,90 | Cửa sổ 0,8 giây; tỷ lệ thời gian dương 0,60 |
| Điện thoại | 0,60 | Duy trì 1,2 giây |
| Hành vi khác | 0,50 | Duy trì 1,2 giây |
| Nói chuyện | 0,90 | Duy trì 3,0 giây |

Nhóm điện thoại gồm gọi điện và nhắn tin ở hai phía. Nhóm hành vi khác gồm uống nước, chỉnh tóc hoặc trang điểm, chỉnh radio, với ra sau và với sang bên. Ngưỡng tắt của các nhóm hành vi thấp hơn ngưỡng bật 0,10; thời gian chống lặp là 1 giây. Các tham số phụ được lưu trong cấu hình khóa để tái lập chính xác.

Ngáp được ghi nhận như tín hiệu hỗ trợ, chưa dùng độc lập để kết luận buồn ngủ. Các ngưỡng trong bảng là tham số thực nghiệm trên DMD, không phải ngưỡng y khoa hoặc tiêu chuẩn cảnh báo đã được chứng nhận.

Cửa sổ của Gaze và mắt được tính theo mốc thời gian, không chỉ đếm số khung hình. Chương trình yêu cầu đủ lịch sử cho cửa sổ; một khoảng giữa hai quan sát chỉ được tính là dương khi cả hai đầu đều vượt ngưỡng. Cảnh báo còn yêu cầu quan sát hiện tại đạt điều kiện. Cách xử lý này hạn chế việc kéo dài bằng chứng từ một mẫu dương đơn lẻ khi các quan sát sau không còn phù hợp.

Đối với hành vi, cộng điểm số trong nhóm điện thoại cho phép duy trì tín hiệu khi mô hình dao động giữa gọi điện và nhắn tin. Tuy nhiên, nếu điểm số chuyển sang safe_drive, việc gom nhóm không tự khắc phục được lỗi. Khoảng hụt tín hiệu ngắn có thể giữ lại bằng chứng tích lũy theo tham số bridge, nhưng không được cộng thành thời gian dương. Ngưỡng bật, ngưỡng tắt và khoảng chống lặp giúp kiểm soát sự thay đổi trạng thái; tác động của chúng phải được kiểm tra trên video, không suy ra chỉ từ ma trận nhầm lẫn ảnh.

### 3.6. Xử lý thiếu quan sát và giới hạn góc camera

Khi không có dự đoán hợp lệ, bằng chứng đang tích lũy được đặt lại. Khoảng gián đoạn quá dài không được coi là một chuỗi quan sát liên tục. Ở luồng video cuối, mất mặt được ghi là thiếu quan sát thay vì thay bằng toàn khung hình cho nhánh mặt.

Nhánh hành vi cần góc quay thấy thân và tay. Tùy chọn xác nhận vùng thân trong chương trình do người vận hành thiết lập, chưa phải cơ chế tự động xác định camera có đủ thông tin. Vì vậy, không thể mặc nhiên dùng camera chỉ chụp mặt để thay thế camera thân.

### 3.7. Thiết kế đầu ra

Đầu ra gồm mốc thời gian, nhãn dự đoán, điểm số lớp, trạng thái thiếu quan sát và trạng thái cảnh báo. Kết quả được lưu để tính chỉ số và xem lại sự kiện. Giao diện webcam, âm thanh cảnh báo và tương tác người dùng của bản tích hợp cuối thuộc phần cần bổ sung, không được trình bày như sản phẩm đã kiểm chứng.

### 3.8. Luồng vận hành và trách nhiệm của từng thành phần

Khi bắt đầu một phiên, chương trình nạp cấu hình cùng trọng số và khởi tạo trạng thái thời gian rỗng. Mỗi mẫu video được gắn thời điểm để các chính sách sử dụng cùng cơ sở tính thời lượng. Khối tiền xử lý tạo vùng ảnh; khối mô hình cung cấp điểm số; khối chính sách cập nhật cảnh báo. Nhật ký lưu kết quả tương ứng để có thể phân biệt lỗi quan sát, lỗi phân loại và lỗi xử lý thời gian.

Ba trạng thái cần phân biệt là có cảnh báo, chưa có cảnh báo đang hoạt động và thiếu quan sát. “Chưa có cảnh báo” chỉ có nghĩa chưa đạt quy tắc hiện tại, không phải xác nhận người lái an toàn tuyệt đối. Trạng thái thiếu quan sát cho biết hệ thống chưa đủ thông tin ở ít nhất một nhánh; đây cũng là dữ liệu cần thống kê khi đánh giá, không chỉ là thông báo kỹ thuật.

Thiết kế theo mô-đun thuận lợi cho thay thế từng mô hình và phân tích nguyên nhân lỗi. Đổi lại, phải quản lý nhiều bộ trọng số và bảo đảm các đầu vào phù hợp. Phương án một mạng đa nhiệm có thể được nghiên cứu sau, nhưng cần đo lợi ích về tài nguyên cùng tác động đến chất lượng từng nhánh trước khi thay thế bản hiện tại.

## CHƯƠNG 4. XÂY DỰNG VÀ TÍCH HỢP HỆ THỐNG

### 4.1. Môi trường và công nghệ

Python được sử dụng cho xử lý dữ liệu và suy luận; PyTorch phục vụ huấn luyện; OpenCV và FFmpeg/FFprobe hỗ trợ đọc, kiểm tra video; MediaPipe phục vụ định vị khuôn mặt và mắt. Các notebook được chuẩn bị để chạy huấn luyện, đánh giá trên Kaggle với GPU T4. Dữ liệu trung gian và kết quả được đóng gói để chuyển giữa máy cá nhân và môi trường thực nghiệm.

### 4.2. Xây dựng chương trình chuẩn bị dữ liệu

Chương trình chuẩn bị dữ liệu đọc video và nhãn, xác định mẫu hợp lệ, cắt vùng ảnh và xuất danh sách mẫu. Trước huấn luyện, hệ thống kiểm tra tính nhất quán giữa dữ liệu, cấu hình lớp và phân hoạch người tham gia. Việc lưu dữ liệu đã xử lý giúp tránh trích xuất lại video ở mỗi lần huấn luyện.

Dữ liệu sau xử lý được tổ chức để notebook sử dụng trực tiếp ảnh và nhãn, không phải giải mã lại toàn bộ video ở từng epoch. Điều này giải thích vì sao thời gian huấn luyện trên dữ liệu đã chuẩn bị có thể ngắn hơn đáng kể giai đoạn trích xuất. Thời gian chạy ngắn tự nó không chứng minh mô hình học đủ hoặc thiếu; cần xem số mẫu thực tế, lịch sử validation và điều kiện dừng.

Quy trình cũng tách nhiệm vụ huấn luyện ảnh với đánh giá video. Dữ liệu ảnh hỗ trợ thử nghiệm cấu hình mô hình, còn video cùng nhãn thời gian được giữ để đánh giá diễn biến liên tục. Không lấy thứ tự các ảnh rời trong một lô huấn luyện làm thứ tự thời gian của video.

### 4.3. Xây dựng chương trình huấn luyện và lựa chọn mô hình

Quy trình huấn luyện lưu lịch sử theo epoch, trọng số tốt nhất và dự đoán validation. Mỗi nhiệm vụ được chạy với ba seed để quan sát mức biến động. Dữ liệu test được tách khỏi bước lựa chọn; chương trình đánh giá cuối sử dụng trọng số đã khóa.

Không gộp trực tiếp trọng số của ba mô hình thành một tệp mạng duy nhất. Gói hệ thống chứa các mô hình con và cấu hình điều phối, cho phép nhận diện nhiều nhóm dấu hiệu trong cùng một quy trình phần mềm.

### 4.4. Tích hợp suy luận trên video

Chương trình suy luận lần lượt đọc các mẫu theo mốc thời gian, tạo đầu vào tương ứng, chạy mô hình và cập nhật chính sách cảnh báo. Việc giữ nhất quán tiền xử lý giữa huấn luyện và suy luận được kiểm tra để hạn chế sai khác khi chuyển môi trường.

Luồng video có cách xử lý mất mặt chặt chẽ hơn khâu chuẩn bị ảnh trước đó: dự đoán không hợp lệ được ghi nhận và tách khỏi trạng thái an toàn. Sự khác biệt này, cùng tần suất lấy mẫu, là lý do chỉ số ảnh đóng gói và chỉ số khung hình trong video không hoàn toàn trùng nhau.

### 4.5. Đóng gói và kiểm chứng

Gói tích hợp gồm trọng số Gaze, Drowsiness, Distraction và chính sách thời gian v3. Mã băm được dùng để xác nhận đúng bộ trọng số, cấu hình và báo cáo. Kết quả video đã được kiểm tra lại bằng ma trận nhầm lẫn và chạy lại chính sách trên chuỗi dự đoán lưu sẵn.

Các kiểm tra này hỗ trợ tính nhất quán và khả năng tái lập. Chúng không thay thế kiểm thử quan sát trực tiếp hoặc chứng minh hiệu quả trên phương tiện thực tế.

Việc kiểm chứng được tổ chức ở ba mức. Mức dữ liệu kiểm tra manifest, phân hoạch và thứ tự lớp. Mức mô hình kiểm tra đúng trọng số và cấu hình tiền xử lý. Mức đánh giá đối chiếu dự đoán với ma trận nhầm lẫn, sau đó tái chạy chính sách từ chuỗi điểm số để kiểm tra thống kê sự kiện. Một kết quả chỉ được đưa vào bảng tổng hợp khi xác định được nhiệm vụ và phạm vi mẫu tương ứng.

Khi có thay đổi ở một trong ba mức này, cần tạo phiên bản kết quả mới thay vì trộn số liệu cũ và mới. Chẳng hạn, kết quả mắt bốn lớp không thể thay trực tiếp cho mắt hai lớp; cấu hình chỉ ảnh mặt không thay cho mặt kết hợp mắt; ngưỡng cảnh báo khác cũng không dùng chung bảng sự kiện. Quy tắc quản lý phiên bản giúp bảo đảm báo cáo mô tả đúng hệ thống đã được đánh giá.

### 4.6. Tình trạng các nội dung theo thuyết minh

Bảng 4.1. Đối chiếu nội dung đăng ký và kết quả hiện tại.

| Nội dung | Tình trạng đến 08/10/2026 |
|---|---|
| Khảo cứu và xây dựng quy trình xử lý hình ảnh | Đã thực hiện |
| Huấn luyện nhận diện nhiều dấu hiệu | Đã thực hiện trên các phần DMD đã chuẩn bị |
| Tích hợp các mô hình với quy tắc thời gian | Đã có chương trình chạy video và kết quả kiểm chứng |
| Đánh giá phân loại và sự kiện | Đã có trên nhóm test DMD hiện tại |
| Thu thập, tinh chỉnh và đánh giá dữ liệu người Việt | Chưa hoàn thành |
| Huấn luyện hoặc đánh giá bổ sung trên NTHU | Chưa có kết quả kiểm chứng |
| So sánh đầy đủ các kiến trúc nêu trong thuyết minh | Chưa hoàn thành |
| Quantization, pruning và thử thiết bị cấu hình thấp | Chưa hoàn thành |
| Kiểm thử webcam, âm thanh và FPS toàn hệ thống cuối | Chưa có kết quả xác nhận |
| Video demo, sản phẩm truyền thông và chuyển giao | Chưa có minh chứng hoàn thành trong hồ sơ đang tổng hợp |

### 4.7. Kiểm thử webcam và demo

[CHƯA THỰC HIỆN KIỂM CHỨNG BẢN TÍCH HỢP CUỐI]

Chưa điền số người tham gia, cấu hình camera, FPS, độ trễ hiển thị và âm thanh hoặc mức cảnh báo nhầm khi dùng webcam. Phần này chỉ được bổ sung sau khi có thực nghiệm và nhật ký tương ứng. Không sử dụng số liệu xử lý video ghi sẵn để thay thế.

## CHƯƠNG 5. KẾT QUẢ THỰC NGHIỆM VÀ ĐÁNH GIÁ

### 5.1. Tổ chức thực nghiệm

Kết quả được trình bày theo ba mức: lựa chọn mô hình trên validation, phân loại trên tập ảnh test và cảnh báo trên video. Các mức có tập mẫu và cách tính khác nhau nên không gộp thành một độ chính xác chung của hệ thống.

### 5.2. Kết quả lựa chọn mô hình

Bảng 5.1. Macro-F1 validation theo seed, đơn vị phần trăm.

| Cấu hình | Seed 42 | Seed 43 | Seed 44 |
|---|---:|---:|---:|
| Gaze, chỉ ảnh mặt | 68,88 | 54,66 | 65,33 |
| Gaze, ảnh mặt và mắt | 73,94 | 79,56 | 78,60 |
| Drowsiness, trung bình hai đầu | 90,14 | 94,48 | 92,86 |
| Distraction, 11 lớp | 80,35 | 82,37 | 82,35 |

Đối với Gaze, macro-F1 trung bình ba seed tăng từ 62,96% lên 77,36% khi thêm vùng mắt. Đây là so sánh trong cùng quy trình và tập validation, cho thấy biểu diễn ảnh mặt kết hợp mắt có lợi trong thực nghiệm này. Kết quả chưa phải bằng chứng về mức cải thiện tương tự trên mọi tập dữ liệu.

Drowsiness đã được điều chỉnh từ bốn trạng thái mắt sang hai trạng thái ổn định. Cấu hình này phù hợp hơn với mục tiêu theo dõi nhắm mắt kéo dài. Không so trực tiếp macro-F1 của bài toán bốn lớp với bài toán hai lớp để kết luận mức tăng chất lượng, do nhãn và mẫu đánh giá đã thay đổi.

Ba mô hình cuối đều chọn seed 43. Epoch tốt nhất lần lượt là 7 cho Gaze, 6 cho Drowsiness và 8 cho Distraction. Riêng Drowsiness được chọn theo trung bình hai đầu, không chỉ theo chỉ số mắt cao nhất.

### 5.3. Kết quả phân loại trên tập ảnh test

Bảng 5.2. Kết quả phân loại ảnh sau khi khóa mô hình.

| Nhiệm vụ | Mẫu đánh giá | Accuracy | Macro-F1 |
|---|---:|---:|---:|
| Vùng nhìn, 9 lớp | 607 | 84,84% | 84,22% |
| Mắt nhắm hoặc mở ổn định | 5.355 | 98,67% | 96,95% |
| Ngáp, 3 lớp | 7.629 | 92,78% | 84,28% |
| Hành vi, 11 lớp | 6.321 | 83,31% | 77,96% |

Đầu mắt nhận diện đúng 630/652 mẫu nhắm mắt, tương ứng recall 96,63%; có 49/4.703 mẫu mắt mở bị nhận diện thành nhắm mắt. Đây là lỗi ở mức ảnh, chưa phải số lần báo nhầm của hệ thống theo thời gian.

Đầu ngáp còn hạn chế ở lớp ngáp không có tay che, với precision khoảng 63,69%. Nhánh hành vi có macro-F1 thấp hơn accuracy, cho thấy chất lượng giữa các lớp chưa đồng đều. Do đó, cần xem thêm nhầm lẫn theo lớp thay vì chỉ sử dụng accuracy để kết luận mô hình đã đủ tốt.

Bảng 5.3. Một số lớp còn hạn chế trong tập ảnh test.

| Nhiệm vụ và lớp | Số mẫu thật | Precision | Recall | F1 |
|---|---:|---:|---:|---:|
| Gaze: phía trước bên phải | 66 | 80,43% | 56,06% | 66,07% |
| Gaze: gương trái | 59 | 73,58% | 66,10% | 69,64% |
| Gaze: gương phải | 56 | 68,75% | 98,21% | 80,88% |
| Hành vi: với ra ghế sau | 80 | 40,85% | 72,50% | 52,25% |
| Hành vi: nói chuyện với hành khách | 150 | 38,46% | 66,67% | 48,78% |
| Hành vi: với sang bên | 631 | 91,50% | 64,82% | 75,88% |

Các lớp trong bảng được chọn để phân tích hạn chế, không phải toàn bộ danh sách lớp. Gương phải có recall cao nhưng precision thấp hơn, nghĩa là mô hình nhận diện được phần lớn mẫu thuộc lớp này đồng thời gán nhãn gương phải cho một số mẫu khác. Ngược lại, phía trước bên phải và với sang bên có recall thấp hơn, cho thấy còn bỏ sót nhiều mẫu thật dù precision tương đối cao. Hai dạng lỗi cần hướng cải thiện khác nhau.

Ở hành vi nói chuyện, precision 38,46% cho thấy nhãn dự đoán dễ xuất hiện ngoài các mẫu thật của lớp. Đây là căn cứ để thận trọng khi dùng nhãn tức thời làm cảnh báo. Với ra ghế sau cũng có F1 thấp và chỉ 80 mẫu test; việc bổ sung ví dụ đa dạng là hướng cần xem xét. Các con số chưa xác định được nguyên nhân như che khuất hoặc góc camera nếu chưa đối chiếu hình ảnh cụ thể.

So sánh trong nội bộ từng nhiệm vụ có ý nghĩa hơn so sánh trực tiếp giữa nhiệm vụ. Macro-F1 mắt cao hơn hành vi không có nghĩa kiến trúc ở nhánh mắt tốt hơn về mọi mặt, vì số lớp, độ khó và phạm vi nhãn khác nhau. Các kết quả này chỉ ra mức đáp ứng của từng mô hình đối với bài toán riêng.

### 5.4. Phát triển chính sách cảnh báo trên validation

Chính sách ban đầu yêu cầu điểm số và thời lượng liên tục đạt điều kiện. Trên video validation, phương án này phát hiện 4/10 sự kiện nhìn lệch, 1/12 sự kiện nhắm mắt và 39/83 sự kiện hành vi. Kết quả cho thấy quy tắc liên tục dễ bị gián đoạn bởi dao động dự đoán.

Các phiên bản tiếp theo dùng tích lũy theo cửa sổ và nhóm hành vi. Trong kiểm tra luân phiên để riêng một người ở giai đoạn phát triển chính sách, phiên bản hành vi v2 phát hiện 70/83 sự kiện với 32 lần bắt đầu sai; v3 phát hiện 72/83 với 3 lần bắt đầu sai. Kết quả này được dùng để lựa chọn phương án, không được báo cáo như test độc lập của toàn hệ thống.

Sau bước lựa chọn, trọng số và chính sách v3 được khóa để đánh giá video cuối. Không điều chỉnh tiếp ngưỡng bằng kết quả của lần đánh giá này.

### 5.5. Định nghĩa sự kiện tham chiếu

Sự kiện tham chiếu được suy ra từ nhãn video: mắt nhắm đủ 1,5 giây; nhìn ngoài front hoặc hành vi ngoài safe_drive đủ 2 giây. Đây là định nghĩa phục vụ thực nghiệm, không phải xác nhận mỗi sự kiện đều nguy hiểm hoặc biểu hiện buồn ngủ sinh lý.

Một sự kiện được tính là phát hiện khi có ít nhất một mẫu cảnh báo chồng lấp khoảng tham chiếu. Phép tính hiện tại không ghép một-một cảnh báo với sự kiện; một cảnh báo dài có thể chồng nhiều sự kiện. Vì vậy, recall cần đọc cùng thời gian cảnh báo sai và độ trễ.

### 5.6. Kết quả phát hiện sự kiện trên video cuối

Đánh giá gồm 21 video của người 7, 23 và 36: 4 video Gaze, 4 video Drowsiness và 13 video Distraction. Các nhánh được đánh giá trên video và góc camera tương ứng, chưa phải thử nghiệm đồng bộ toàn hệ thống trong một tình huống triển khai chung.

Bảng 5.4. Kết quả phát hiện sự kiện tham chiếu.

| Nhánh | Phát hiện/tổng | Recall | Bỏ sót | Bắt đầu sai trên đoạn âm | Bắt đầu ở đoạn chưa rõ nhãn |
|---|---:|---:|---:|---:|---:|
| Nhìn lệch | 10/10 | 100,00% | 0 | 1 | 25 |
| Nhắm mắt kéo dài | 21/22 | 95,45% | 1 | 7 | 36 |
| Hành vi | 91/98 | 92,86% | 7 | 2 | 5 |

Recall cao cho thấy hệ thống phát hiện phần lớn sự kiện theo định nghĩa đã dùng. Tuy nhiên, Gaze chỉ có 10 sự kiện; con số 100% không đủ để khẳng định khả năng phát hiện hoàn hảo. Các lần bắt đầu cảnh báo ở vùng chưa rõ nhãn không được xem là đúng hoặc sai và không nên bỏ qua khi đánh giá mức sẵn sàng triển khai.

Bảng 5.5. Số sự kiện phát hiện được theo từng người trong đánh giá video.

| Mã người | Nhìn lệch | Nhắm mắt kéo dài | Hành vi |
|---|---:|---:|---:|
| 7 | 3/3 | 5/6 | 21/23 |
| 23 | 5/5 | 11/11 | 48/52 |
| 36 | 2/2 | 5/5 | 22/23 |

Bảng theo người cho thấy bỏ sót mắt xuất hiện ở người 7, còn bỏ sót hành vi xuất hiện ở cả ba người. Người 23 đóng góp 52/98 sự kiện hành vi, nên chỉ số gộp chịu ảnh hưởng đáng kể từ nhóm dữ liệu này. Bảng giúp tránh hiểu nhầm rằng recall tổng thể đồng nghĩa mức đáp ứng giống nhau ở mọi người. Tuy nhiên, với chỉ ba người và số sự kiện khác nhau, chưa đủ cơ sở xác định độ ổn định trên quần thể rộng.

### 5.7. Cảnh báo trên đoạn âm

Bảng 5.6. Thời lượng cảnh báo chồng các đoạn âm có nhãn.

| Nhánh | Thời gian âm | Thời gian cảnh báo chồng đoạn âm | Tỷ lệ |
|---|---:|---:|---:|
| Nhìn lệch | 56,89 giây | 2,39 giây | 4,19% |
| Nhắm mắt kéo dài | 422,98 giây | 3,49 giây | 0,83% |
| Hành vi | 1.354,37 giây | 4,54 giây | 0,33% |

Số lần bắt đầu sai không phản ánh đầy đủ trường hợp cảnh báo bắt đầu trước đó rồi kéo dài sang đoạn âm. Vì vậy, bảng thời lượng bổ sung thông tin cho bảng sự kiện. Đặc biệt, dữ liệu âm của Gaze chưa đến một phút, chưa đủ cơ sở suy rộng mức báo nhầm trong nhiều giờ sử dụng.

### 5.8. Độ trễ và tính kịp thời

Bảng 5.7. Độ trễ tính từ mốc sự kiện tham chiếu.

| Nhánh | P95 trên sự kiện phát hiện | Trễ lớn nhất | Phát hiện trong 2 giây/tổng sự kiện |
|---|---:|---:|---:|
| Nhìn lệch | 5,80 giây | 5,98 giây | 7/10 |
| Nhắm mắt kéo dài | 0,00 giây | 0,00 giây | 21/22 |
| Hành vi | 2,40 giây | 38,98 giây | 84/98 |

Các thống kê độ trễ chỉ tính trên sự kiện phát hiện được. Cột cuối giữ cả sự kiện bỏ sót trong mẫu số. Mốc 2 giây là thống kê mô tả bổ sung sau đánh giá, chưa phải tiêu chí nghiệm thu đặt trước.

Độ trễ bằng 0 không có nghĩa cảnh báo tức thì từ lúc hành vi bắt đầu. Mốc tham chiếu đã bao gồm thời gian chờ 1,5 hoặc 2 giây, trong khi chính sách dự đoán có thể bật trước mốc này.

Trường hợp hành vi chậm nhất liên quan đến gọi điện bên trái, trễ 38,98 giây sau mốc tham chiếu, khoảng 40,99 giây sau lúc hành vi bắt đầu. Trong đoạn này, nhiều mẫu bị nhận diện thành safe_drive. Kết quả chỉ ra hạn chế về tính kịp thời dù recall sự kiện tổng thể cao; chưa thể kết luận nguyên nhân hình ảnh nếu chưa kiểm tra trực tiếp video tương ứng.

Trường hợp cảnh báo muộn cho thấy sự khác biệt giữa “phát hiện được” và “phát hiện đủ sớm”. Một sự kiện dài vẫn được tính là phát hiện nếu cảnh báo xuất hiện ở cuối đoạn. Vì vậy, recall hành vi 92,86% phải được đọc cùng tỷ lệ 84/98 sự kiện được phát hiện trong 2 giây sau mốc tham chiếu. Chỉ số thứ hai làm rõ hơn hạn chế về thời điểm, nhưng vẫn phụ thuộc định nghĩa mốc tham chiếu và chưa phải tiêu chuẩn an toàn.

Đánh giá độ trễ hiện tại cũng chưa bao gồm toàn bộ thời gian từ thu nhận ảnh đến phát âm thanh trên thiết bị. Đây là độ trễ theo chuỗi dự đoán và nhãn video. Khi kiểm thử webcam, phải đo thêm giải mã, định vị, suy luận, cập nhật chính sách và đưa cảnh báo tới người dùng trước khi kết luận về thời gian đáp ứng toàn hệ thống.

### 5.9. Chất lượng phân loại trong luồng video

Bảng 5.8. Chỉ số khung hình gộp trong đánh giá video.

| Nhiệm vụ | Mẫu có nhãn phù hợp | Accuracy | Macro-F1 | Độ phủ dự đoán |
|---|---:|---:|---:|---:|
| Gaze | 3.027 | 80,87% | 80,74% | 97,49% |
| Mắt | 5.355 | 98,64% | 96,94% | 99,96% |
| Ngáp | 7.629 | 92,76% | 84,28% | 99,96% |
| Hành vi | 31.585 | 83,59% | 78,10% | 100,00% |

Accuracy ở bảng này tính thiếu dự đoán là lỗi. Các chỉ số được tính trên kết quả gộp, không lấy trung bình F1 của những video có thể thiếu lớp. Số mẫu khác bảng ảnh test do lấy mẫu video ở 10 FPS, phạm vi nhãn và xử lý thiếu quan sát. Độ phủ dự đoán cao không có nghĩa tất cả dự đoán đều đúng.

### 5.10. Phân tích hạn chế của mô hình

Nhánh Gaze vẫn có ba sự kiện trễ hơn 2 giây sau mốc tham chiếu, thuộc các khoảng nhìn trái hoặc gương trái. Cách xem mọi vùng ngoài front là nhìn lệch cũng chưa xét ngữ cảnh quan sát giao thông.

Nhánh mắt bỏ sót một sự kiện của người 7. Trong 17 mẫu thuộc khoảng tham chiếu bị bỏ sót, 14 mẫu được dự đoán là mở mắt. Kết quả cho thấy sai số phân loại vẫn có thể dẫn đến bỏ sót một đoạn nhắm mắt ngắn.

Nhánh hành vi bỏ sót bảy sự kiện và còn một số cảnh báo muộn. Một số sự kiện tham chiếu chỉ còn ít mẫu sau khi đạt điều kiện thời lượng; cần xem cả diễn biến trước mốc tham chiếu để phân tích, không mặc định đây là lỗi nhãn hoặc chỉ do mô hình.

Tập video cuối chỉ gồm ba người và người 23 đóng góp nhiều video hơn. Việc lựa chọn cấu hình qua nhiều lần thử trên validation có thể tạo thiên lệch lựa chọn. Báo cáo chưa có phân tích độ bất định theo người hoặc đánh giá trên một bộ dữ liệu ngoài DMD.

Từ các kết quả, có thể chia vấn đề cần cải thiện thành ba nhóm. Nhóm thứ nhất là thông tin đầu vào, gồm mất vùng mặt, thiếu vùng mắt hoặc góc quay không thấy thao tác. Nhóm thứ hai là nhận diện, thể hiện qua nhầm giữa các lớp hoặc nhầm hành vi với safe_drive. Nhóm thứ ba là quyết định theo thời gian, gồm tích lũy bị gián đoạn và chờ quá lâu. Cách phân nhóm này giúp lựa chọn can thiệp đúng chỗ, thay vì mặc định mọi sai sót đều cần tăng số epoch.

Nếu ảnh đầu vào không đủ thông tin, cần cải thiện thu nhận hoặc quy định điều kiện sử dụng. Nếu nhầm lớp lặp lại trên ảnh rõ, cần xem nhãn và bổ sung dữ liệu huấn luyện phù hợp. Nếu dự đoán ảnh đủ tốt nhưng cảnh báo không ổn định, cần nghiên cứu chính sách thời gian trên một tập phát triển riêng. Đây là định hướng từ kết quả hiện có, chưa phải những cải thiện đã được thực nghiệm xác nhận.

### 5.11. Đánh giá tổng thể

Hệ thống đã hình thành quy trình nhận diện nhiều dấu hiệu và xử lý sự kiện có thể tái lập. Các kết quả ủng hộ việc tiếp tục kiểm thử trên video mới, nhưng chưa đủ cơ sở kết luận hệ thống đáp ứng yêu cầu cảnh báo kịp thời trong điều kiện sử dụng thực tế.

Về chất lượng mô hình, đầu mắt có kết quả tốt nhất trong phạm vi nhiệm vụ tương ứng; Gaze và Distraction còn dư địa cải thiện. Về hệ thống, yêu cầu quan trọng tiếp theo là kiểm chứng góc camera triển khai, cảnh báo trên đoạn bình thường dài và độ trễ toàn luồng. Không thể chỉ tăng recall bằng giảm ngưỡng rồi xem đó là hoàn thiện mô hình.

# PHẦN 3. KẾT LUẬN VÀ KIẾN NGHỊ

## 1. Kết luận

Đề tài đã xây dựng hệ thống nghiên cứu nhận diện dấu hiệu buồn ngủ và mất tập trung từ video RGB, gồm ba mô hình chuyên biệt cùng bộ xử lý thời gian. Quy trình đã bao gồm chuẩn bị dữ liệu, huấn luyện, lựa chọn mô hình, khóa cấu hình và kiểm chứng kết quả trên DMD.

Kết quả cho thấy khả năng phân loại các dấu hiệu và phát hiện phần lớn sự kiện tham chiếu. Tuy nhiên, cảnh báo sai, độ trễ dài ở một số hành vi và giới hạn dữ liệu vẫn ảnh hưởng đến mức sẵn sàng ứng dụng. Mục tiêu xây dựng nền tảng nhận diện và đánh giá trên video đã đạt được ở mức nghiên cứu; mục tiêu kiểm chứng cảnh báo trực tiếp trong điều kiện thực tế chưa hoàn thành.

## 2. Đóng góp của đề tài

- Xây dựng quy trình chuẩn bị ba phần dữ liệu DMD với nhãn và phân hoạch có thể kiểm tra.
- Huấn luyện và đánh giá các mô hình nhận diện vùng nhìn, trạng thái mắt, ngáp và hành vi.
- Tích hợp đầu ra mô hình với chính sách thời gian, xử lý thiếu quan sát và lưu nhật ký.
- Xây dựng hồ sơ kiểm chứng trọng số, cấu hình và kết quả, đồng thời phân tích cảnh báo sai, bỏ sót và độ trễ.

Các đóng góp thuộc hướng ứng dụng, thực nghiệm và tích hợp hệ thống. Chưa xác lập đóng góp về kiến trúc học sâu mới hoặc kết quả vượt trội trên một benchmark chuẩn dùng chung.

## 3. Hạn chế

Dữ liệu đánh giá cuối có ít người tham gia, các khung hình tương quan theo thời gian và chưa đại diện điều kiện người dùng mục tiêu. Ba nhánh sử dụng góc camera khác nhau, chưa xác nhận chất lượng khi triển khai đồng thời. Nhãn hành vi và trạng thái mắt không cung cấp đầy đủ thông tin về nguy hiểm hoặc buồn ngủ sinh lý.

Phương pháp tính sự kiện hiện tại chưa ghép một-một cảnh báo với tham chiếu; vùng thiếu nhãn còn đáng kể. Chưa có đo FPS, độ trễ đầu cuối và hiệu quả cảnh báo âm thanh của bản tích hợp trên webcam. Dữ liệu người Việt, NTHU, tối ưu lượng tử hóa hoặc cắt tỉa và demo cuối còn thiếu kết quả.

## 4. Kiến nghị và hướng phát triển

Trước mắt, cần giữ nguyên mô hình và cấu hình đã đánh giá làm mốc đối chiếu. Bước tiếp theo là kiểm thử trên video mới có nhãn sự kiện, tách biệt với dữ liệu đã dùng lựa chọn tham số. Nên ưu tiên các đoạn quan sát bình thường đủ dài, thay đổi góc nhìn, kính và che khuất để đo rõ cảnh báo nhầm.

Khi bổ sung webcam, cần đo FPS và độ trễ từ thu nhận ảnh đến hiển thị hoặc âm thanh; đồng thời kiểm tra khả năng quan sát mặt, thân và tay. Các thử nghiệm hành vi nên thực hiện trong môi trường mô phỏng hoặc khi phương tiện đứng yên. Phần kết quả webcam chỉ được đưa vào báo cáo sau khi có dữ liệu thực nghiệm.

Về mô hình, hướng cải thiện ưu tiên là các trường hợp gọi điện trái bị nhầm với lái xe bình thường, phân biệt vùng nhìn khó và ngáp bị che khuất. Dữ liệu mới dùng tinh chỉnh phải tách khỏi dữ liệu đánh giá độc lập. Chỉ xem xét gộp thành một mạng đa nhiệm hoặc tối ưu lượng tử hóa sau khi có đường cơ sở rõ ràng về chất lượng và tốc độ.

Về phương pháp đánh giá, cần bổ sung ghép một-một sự kiện, chỉ số phát hiện trong giới hạn thời gian định trước và độ bất định theo người tham gia. NTHU có thể được dùng cho kiểm tra bổ sung sau khi đối chiếu nhãn và phạm vi nhiệm vụ; không mặc định dữ liệu mới có thể ghép trực tiếp với DMD.

# TÀI LIỆU THAM KHẢO

[1] Trương Quốc Bảo, Trương Quốc Định và Đinh Thành Nhân (2016). “Xác định trạng thái nhắm mở mắt sử dụng kỹ thuật xử lý ảnh và máy học nhận dạng”. Đo lường điều khiển và Tự động hóa, số 17, tr. 36-45. Thông tin và tóm tắt công bố tại [cơ sở dữ liệu Đại học Cần Thơ](https://qldiem.ctu.edu.vn/ql/docgia/tapchitrongnuoc-2016/baibao-51246.html?page_current=2). Phạm vi tham khảo: tóm tắt phương pháp, không sử dụng số liệu so sánh của bài báo.

[2] Albadawi, Y., Takruri, M., & Awad, M. (2022). “A Review of Recent Developments in Driver Drowsiness Detection Systems”. Sensors, 22(5), 2069. [DOI: 10.3390/s22052069](https://doi.org/10.3390/s22052069).

[3] Ortega, J. D., Kose, N., Cañas, P., Chao, M.-A., Unnervik, A., Nieto, M., Otaegui, O., & Salgado, L. (2020). “DMD: A Large-Scale Multi-Modal Driver Monitoring Dataset for Attention and Alertness Analysis”. [arXiv:2008.12085](https://arxiv.org/abs/2008.12085).

[4] He, K., Zhang, X., Ren, S., & Sun, J. (2016). “Deep Residual Learning for Image Recognition”. Proceedings of the IEEE Conference on Computer Vision and Pattern Recognition, tr. 770-778. [Bản công bố tại Computer Vision Foundation](https://www.cv-foundation.org/openaccess/content_cvpr_2016/html/He_Deep_Residual_Learning_CVPR_2016_paper.html).

[5] Google AI Edge. “Face landmark detection guide”. Tài liệu MediaPipe Face Landmarker, truy cập ngày 08/10/2026. [Tài liệu chính thức](https://developers.google.com/edge/mediapipe/solutions/vision/face_landmarker?hl=en).

[6] Nhóm thực hiện đề tài THS2026-77 (2026). “Xây dựng hệ thống AI nhận diện trạng thái buồn ngủ hoặc mất tập trung của tài xế”. Thuyết minh đề tài nghiên cứu khoa học của sinh viên, Đại học Cần Thơ. Tài liệu nội bộ: ThuyetMinhDeTai_fin.docx.

[7] Nhóm thực hiện đề tài THS2026-77 (2026). Mã nguồn, cấu hình khóa và hồ sơ thực nghiệm hệ thống giám sát tài xế. Tài liệu nội bộ, phiên bản tổng hợp ngày 08/10/2026. Danh sách minh chứng tại Phụ lục A.

# PHỤ LỤC A. HỒ SƠ KIỂM CHỨNG KẾT QUẢ

Các đường dẫn dưới đây tính từ thư mục gốc dự án driver_monitoring. Đây là nguồn số liệu thực nghiệm của báo cáo, không phải tài liệu nghiên cứu bên ngoài.

1. reports/gaze_v3_verified_results.json: kết quả validation và so sánh Gaze chỉ mặt với mặt kết hợp mắt.
2. reports/gaze_final_test_verified.json: kết quả phân loại Gaze trên tập ảnh test.
3. reports/drowsiness_v3_verified_results.json: kết quả validation và lựa chọn mô hình mắt, ngáp.
4. reports/drowsiness_v3_test_verified.json: kết quả mắt, ngáp trên tập ảnh test.
5. reports/distraction11_verified_results.json và reports/results_6_7_verified.json: validation và test mô hình hành vi.
6. reports/temporal_final_lock.json: trọng số và chính sách khóa trước đánh giá thời gian cuối.
7. reports/temporal_final_verified.json: kết quả kiểm chứng 21 video, sự kiện, độ trễ và chỉ số khung hình.
8. reports/final_analysis_20261008/: danh sách sự kiện, cảnh báo trên đoạn âm và các trường hợp bỏ sót hoặc chậm.
9. exports/driver_system_candidate_v3.zip: gói mô hình và chương trình suy luận tương ứng.

Không dùng hai báo cáo mẫu làm nguồn số liệu cho đề tài. Hai mẫu chỉ được tham khảo về bố cục; các số liệu trong nội dung được lấy từ hồ sơ thực nghiệm của dự án.

# PHỤ LỤC B. NỘI DUNG CẦN BỔ SUNG KHI KIỂM THỬ THỰC TẾ

Trạng thái: chưa có kết quả kiểm chứng cho bản tích hợp cuối.

- Ngày và địa điểm thực nghiệm: [CHƯA BỔ SUNG].
- Thiết bị, cấu hình máy và camera: [CHƯA BỔ SUNG].
- Góc đặt camera và vùng quan sát: [CHƯA BỔ SUNG].
- Số người tham gia, thời lượng và điều kiện ánh sáng: [CHƯA BỔ SUNG].
- Quy trình gán nhãn và tách dữ liệu hiệu chỉnh, đánh giá: [CHƯA BỔ SUNG].
- FPS và độ trễ đầu cuối: [CHƯA ĐO].
- Kết quả sự kiện, cảnh báo sai và thiếu quan sát: [CHƯA ĐÁNH GIÁ].
- Kiểm tra hiển thị và âm thanh cảnh báo: [CHƯA KIỂM CHỨNG].
- Hình ảnh minh chứng và video demo: [CHƯA BỔ SUNG].

Các mục này được giữ trống có chủ đích để tránh trình bày nội dung dự kiến như kết quả đã thực hiện.
