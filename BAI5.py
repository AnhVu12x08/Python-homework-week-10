'''
Bài 5. Tìm hiểu về dịch vụ RSS và xây dựng một chương trình python trích xuất 10 mẫu tin
giáo dục từ Dịch vụ Báo thanh niên RSS: https://thanhnien.vn/rss/giao-duc.rss
Chú ý rằng do dữ liệu RSS Feed là XML nên khi tạo đối tượng soup, thêm vào thông số xml
soup = BeautifulSoup(response.text, 'xml')
'''
import requests
from bs4 import BeautifulSoup

# URL của RSS Feed
url = 'https://thanhnien.vn/rss/giao-duc.rss'

# Gửi yêu cầu HTTP GET tới URL
response = requests.get(url)

# Kiểm tra nếu yêu cầu thành công (mã trạng thái 200)
if response.status_code == 200:
    # Phân tích nội dung XML của RSS Feed
    soup = BeautifulSoup(response.text, 'xml')

    # Tìm tất cả các mục tin tức
    news_items = soup.findAll('item')
    # Duyệt qua 10 mục tin tức đầu tiên
    print('Trích xuất 10 mẫu tin giáo dục từ Dịch vụ Báo thanh niên RSS: https://thanhnien.vn/rss/giao-duc.rss\n')

    for i, news_item in enumerate(news_items[:10], 1):
        title_html = news_item.find('title').text
        title_soup = BeautifulSoup(title_html, 'html.parser')
        title = title_soup.getText()
        
        pub_date = news_item.find('pubDate').text
        link = news_item.find('link').text
        
        description_html = news_item.find('description').text
        description_soup = BeautifulSoup(description_html, 'html.parser')
        description = description_soup.get_text()

        # In ra thông tin chi tiết của từng tin tức
        print(f'Tin số {i}: {title}')
        print(f'Ngày đăng: {pub_date}')
        print(f'Link: {link}')
        print(f'Mô tả: {description}')
        print('-'*20)
else:
    print(f'Lỗi mở trang. Mã lỗi: {response.status_code}')






