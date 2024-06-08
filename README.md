## Bài 1
Xây dựng một chương trình python trích xuất tất cả thông báo trong 5 trang đầu tiên từ trang web khoa CNTT. Thông tin trích xuất bao gồm: Tiêu đề, Ngày đăng và URL.

## Bài 2
Xây dựng một chương trình python trích xuất tên và email của BCN Khoa CNTT từ trang [https://fit.huit.edu.vn/gioi-thieu/ban-chu-nhiem-khoa](https://fit.huit.edu.vn/gioi-thieu/ban-chu-nhiem-khoa).

## Bài 3
Xây dựng một chương trình python hiển thị danh sách 10 việc làm IT mới nhất làm việc ở TPHCM từ trang [https://topdev.vn/](https://topdev.vn/).

## Bài 4
Xây dựng một chương trình python trích xuất ngày tháng, tên và URL từ mục Latest News của trang [https://www.python.org/](https://www.python.org/).

## Bài 5
Tìm hiểu về dịch vụ RSS và xây dựng một chương trình python trích xuất 10 mẫu tin giáo dục từ Dịch vụ Báo thanh niên RSS: [https://thanhnien.vn/rss/giao-duc.rss](https://thanhnien.vn/rss/giao-duc.rss).

Chú ý rằng do dữ liệu RSS Feed là XML nên khi tạo đối tượng soup, thêm vào thông số xml:
```python
soup = BeautifulSoup(response.text, 'xml')
