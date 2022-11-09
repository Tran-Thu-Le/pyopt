# What is Python?

Trong bài viết này chúng ta sẽ trả lời những câu hỏi thường gặp nhất về Python nhé!

:writing_hand: **Mục Lục**

1. Python là gì?
2. Tại sao phải là Python mà không là một ngôn ngữ khác?
3. Python có nhược điểm hay không?
4. Tôi nên bắt đầu từ đâu?
5. Tại sao nên dùng Python cho Tối ưu?

---

:airplane: **Let's go**

️:trumpet: **1. Python là gì?** Python là một ngôn ngữ lập trình, nghĩa là nó cho phép bạn giao tiếp và yêu cầu máy tình thực hiện những nhiệm vụ mong muốn.

️:saxophone:**2. Tại sao phải là Python mà không là một ngôn ngữ khác?**

- **Đối với người chưa biết gì về lập trình**: Python là ngôn ngữ đơn giản và "trong sáng" nhất
- **Đối với người đam mê thuật toán**: Python là ngôn ngữ chủ lực trong học máy, trí tuệ nhân tạo, ....
- ** Đối với người lập trình**:

* Python cho phép bạn bỏ qua khái niệm _"bộ nhớ"_ khi làm việc, thứ bạn cần tập trung duy nhất là logic
* Python là ngôn ngữ bậc cao _đơn giản nhất_ nghĩa là nó rất gần gũi với ngôn ngữ chúng ta sử dụng hằng ngày
* Python là ngôn ngữ _"hướng đối tượng"_ mạnh mẽ thứ hai hiện nay (sau Java), cho phép bạn lập trình với hiệu suất cao
* Python rất _linh hoạt_ với kiểu dữ liệu động thích hợp cho các thuật toán có độ phức tạp cao

:guitar:**3. Python có nhược điểm hay không?**
Có, vì không có gì là hoàn hảo! Nếu bạn thấy những thứ dưới đây thật rối rắm, không sao, hãy bỏ qua vì các nhược điểm này là chung cho các ngôn ngữ bậc cao có kiểu dữ liệu động:

- **Python không bảo mật:** Đây là nhược điểm lớn nhất, nghĩa là không hề có khái niệm "riêng tư" trong Python! Nếu bạn muốn dùng Python để lập trình cho Ngân hàng, hay Web thì rất tiếc, bạn không nên dùng Python! Tuy nhiên, Python cũng có hỗ trợ các phương thức "hạn chế" các attributes trong objects, tuy nhiên đó không phải là thứ mà chúng ta quan tâm ở đây, khi mà bạn đang tập trung vào logic.
- **Python là dynamically typed:** Đây là điểm mạnh và cũng là một điểm yếu của Python. Các kiểu dữ liệu trong Python luôn có khả năng thay đổi, ví dụ `x="1"` là một ký tự, nhưng nếu bạn vô tình gán lại `x=1` thì nó lại thành một số, mà các tính toán với hai loại dữ liệu này là tương đối khác nhau từ đó khiến bạn dễ mắc lỗi. Hiện nay, phiên bản Python 3.10 đã có hỗ trợ Static typing giúp hạn chế các lỗi khi thao tác với các kiểu dữ liệu.
- **Python khá "chậm":** Đừng lo nó không chậm như bạn đang nghĩ đâu. Thậm chí nó vẫn nhanh hơn nhiều so với các ngôn ngữ khác như R hay MATLAB. Chậm là đặc trưng của tất cả các ngôn ngữ bậc cao, do nó cần thời gian để chuyển đổi thành ngôn ngữ bậc thấp để giao tiếp với máy tính (chỉ là `0` và `1`). Nếu muốn nhanh hơn, bạn bắt buộc phải làm việc với bộ nhớ, trong nhiều trường hợp, điều này là vô cùng phiền toái. Châm một chút sẽ không là vấn đề gì khi mà bạn có thể nói một cách "dễ hiểu" hơn với mọi người đúng không!

:violin:**4. Tôi nên bắt đầu từ đâu?**

- **Code Python ngay mà không cần cài đặt:** Google Colab: https://colab.research.google.com/
- **Học Python trong 1 ngày (Lý thuyết bài tập code trực tuyến):** W3Schools https://www.w3schools.com/python/

Ví dụ, bạn muốn máy tính chào bạn, với Python rất đơn giản, gõ như sau và bấm nút "run":

```py
print("Hello World!")
```

️:drum: **5. Tại sao nên dùng Python cho Tối ưu?**
Tối ưu (Optimization) là một lĩnh vực toán học giúp bạn đưa ra những quyết định một cách hiệu quả nhất. Bạn có một danh mục cổ phiếu và bạn muốn tối ưu lợi nhuận hoặc tối thiểu hóa rủi ro? Bạn có một mạch điện hay mạch điều khiển robot và muốn nó hoạt động hiệu quả? Bạn muốn sử lý sóng vô tuyến, nhận diện giọng nói, nhận diện gương mặt, .... Welcome to Optimization! Để xử lý những vấn đề cực kỳ phức tạp kia, tối ưu sử dụng rất nhiều thuật toán, và sẽ thật rối rắm khi bạn phải chỉ cho máy tính lưu cái gì ở đâu, thứ bạn cần duy nhất là dạy cho máy tính phải "tư duy" như thế nào? Do đó, không ngôn ngữ nào phù hợp hơn là Python để làm điều đó, vì Python vừa đơn giản vừa mạnh mẽ.

**Python hỗ trợ cộng đồng** một lượng lớn thư viện (package) phong phú và mạnh mẽ:

- Numpy: Tính toán với ma trận và vector
- Matplotlib: Vẽ hình
- Pandas: Dữ liệu lớn
- Scipy: Machine learning
- Torch, TensorFlow: Tensor và Deep Learning

**Cộng đồng hỗ trợ Python**

- Google Colab: cung cấp một trình soạn thảo ONLINE với RAM và bộ nhớ mạnh mẽ
- Anaconda: Trình soạn thảo tích hợp, thân thiện
- Github: Nơi lưu trữ và chia sẻ code hàng đầu

️:musical_keyboard: Vậy là chúng ta đã cùng tìm hiểu cơ bản về Python. Hãy để lại bình luận và trao đổi của bạn phía dưới nếu có nhé. Chúc bạn có những trải nghiệm thú vị cùng Python!
