'''
Bài 4. Xây dựng một chương trình python trích xuất ngày tháng, tên và URL từ mục Latest
News của trang https://www.python.org/
'''
import requests
from bs4 import BeautifulSoup
url = 'https://python.org/'
response = requests.get(url)

if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser')
else:
    print(f'Lỗi mở trang. Mã lỗi: {response.status_code}')
    
    
print('Trích xuất ngày tháng, tên và URL từ mục Latest News của trang https://www.python.org/\n')
ele = soup.find('div', class_="medium-widget blog-widget")
news = ele.find_all('li')
for new in news:
    url = new.find('a')['href']
    title = new.find('a')
    time = new.find('time')
    print(f'Tên bài đăng: {title.text}')
    print(f'Ngày đăng: {time.text}')
    print(f'URL: {url}')
    print('-'*20)




