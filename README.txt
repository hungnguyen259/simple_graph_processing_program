---------------Chương trình xử lý một số thuật toán trên đồ thị-------------------

I. Cài đặt
- Cài đặt biến môi trường người dùng và biến môi trường hệ thống dẫn đến thư mục Graph\Graphviz\bin
Ngoài ra, nếu chạy bằng Python, phải cài đặt biến môi trường người dùng và biến môi trường hệ thống dẫn đến thư mục
Scripts trong thư mục cài đặt Python trên máy người dùng. 
Chương trình sử dụng các thư viện: PyQt5, networkx, pip, Pillow, graphviz

II. Một số lưu ý khi sử dụng chương trình
- Chương trình chỉ áp dụng cho ĐƠN ĐỒ THỊ, không áp dụng cho ĐA ĐỒ THỊ
- Các thuật toán BFS, DFS, Dijkstra, Bellman Ford áp dụng cho đồ thị có hướng và vô hướng.
  Thuật toán Prim và Kruskal chỉ áp dụng cho đồ thị vô hướng.
- Thuật toán Dijkstra không áp dụng cho đồ thị có trọng số âm.
- Thuật toán Bellman Ford không áp dụng cho đồ thị có hướng có chu trình âm hoặc đồ thị vô hướng có trọng số âm.
- Cần nhập điểm xuất phát đối với thuật toán BFS, DFS, Prim. 
  Trong trường hợp có nhiều thành phần liên thông trên đồ thị, thuật toán chỉ thực hiện trên thành phần liên thông
  chứa điểm xuất phát.
- Cần nhập điểm xuất phát và điểm kết thúc đối với thuật toán Dijkstra, Bellman Ford.
