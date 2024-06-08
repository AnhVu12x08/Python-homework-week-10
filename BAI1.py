'''
Bài 1. Xây dựng một chương trình python trích xuất tất cả thông báo trong 5 trang đầu tiên
từ trang web khoa CNTT. Thông tin trích xuất bao gồm: Tiêu đề, Ngày đăng và URL.
'''
import requests
from bs4 import BeautifulSoup


response = []
soup = []
for i in range(1, 6):
    link = (f'https://fit.huit.edu.vn/thong-bao?page={i}')
    response.append(requests.get(link))

for i in range(1,6):
    if response[i-1].status_code == 200:
        soup.append(BeautifulSoup(response[i-1].text, 'html.parser'))
    else:
        print(f'Lỗi mở trang. Mã lỗi: {response.status_code}')
u = 1
print('Trích xuất tất cả thông báo trong 5 trang đầu tiên từ trang web khoa CNTT\n')
for i in range(1,6):
    notifications = soup[i-1].find_all('div', class_='news-list-row')
    print('='*30)
    print(f'Trang {i}, Số thông báo: {len(notifications)}')
    print('='*30)
    for notification in notifications:
        url = notification.find('a', href=True)['href']
        title = notification.find('h3')
        time_element = notification.find('span')
        time = time_element.find('a').contents[-1].strip()
        print(f'Thông báo số {u}: {title.text}')
        u = u + 1
        print(f'Ngày đăng: {time}')
        print(f'https://fit.huit.edu.vn{url}')
        print('-'*20)




