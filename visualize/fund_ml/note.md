# Note khi thực hành sách ML cơ bản.

## Thuật toán K-nearest neighbors:
1. Thư viện sklearn có 2 cách đánh trọng số. 1 là uniform trong đó mọi điểm có trọng số như nhau, 2 là distance, khoảng cách càng gần thì trọng số càng cao.
Ngoài ra, thư viện còn cho phép tự định nghĩa một cách đánh trọng số riêng cho các điểm dữ liệu. trong đó lấy một dãy các distances làm dữ liệu đầu vào và trả về một dãy trọng số có cùng dạng với dãy distance truyền vào.

## Thuật toán K-mean clustering

1. Hàm np.random.choice()

Tham số *replace* Nếu setup = True, các điểm ngẫu nhiên có thể được lựa chọn lại nhiều lần, nếu =False, các điểm ngẫu nhiên chỉ được lựa chọn một lần.

2. scipy.spatial.distance.cdist

Tính toán khoảng cách giữa 2 điểm bất kỳ trong hai tập dữ liệu được nhập.
Mỗi tập dữ liệu được nhập vào là một mảng dữ liệu có số thuộc tính bằng nhau.
Với thuật toán  kmeans, số centroid được nhập luôn có số lượng nhỏ hơn số điểm dữ liệu được chứa đựng trong X.

3. np.argmin

Trả về chỉ số của giá trị nhỏ nhất theo axis được chọn.


