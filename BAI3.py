'''
Bài 3. Xây dựng một chương trình python hiển thị danh sách 10 việc làm IT mới nhất làm
việc ở TPHCM từ trang https://topdev.vn/
'''
import requests
from bs4 import BeautifulSoup
url = 'https://topdev.vn/viec-lam-it/ho-chi-minh-kl79'
response = requests.get(url)

if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser')
else:
    print(f'Lỗi mở trang. Mã lỗi: {response.status_code}')

print('Danh sách 10 việc làm IT mới nhất tại TP.HCM\n')
ele = soup.find('div', class_="col-span-2")
jobs = ele.find_all('div', class_="flex items-start justify-between gap-6 p-4")
i = 1

for job in jobs[:10]:
    name = job.find('h3', class_="line-clamp-1")
    add = job.find('div',class_="flex flex-wrap items-end gap-2 text-gray-500")
    time = job.find('p', class_ = 'whitespace-nowrap text-sm text-gray-400')
    print(f'Công việc thứ {i}: {name.text}')
    i = i+1
    print(f'Địa chỉ: {add.text}')
    print(f'Thời gian: {time.text}')
    print('-'*20)







