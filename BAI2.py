'''
Bài 2. Xây dựng một chương trình python trích xuất tên và email của BCN Khoa CNTT từ
trang https://fit.huit.edu.vn/gioi-thieu/ban-chu-nhiem-khoa
'''
import requests
from bs4 import BeautifulSoup
url = 'https://fit.huit.edu.vn/gioi-thieu/ban-chu-nhiem-khoa'
response = requests.get(url)

if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser')
else:
    print(f'Lỗi mở trang. Mã lỗi: {response.status_code}')

elt = soup.find('div', class_="post-body not-copy content_bold")
ell = elt.find('tr', style="height: 318.525px;")
members = ell.find_all('td')

print('Tên và Email của BCN Khoa CNTT\n')
for member in members:
    name = member.contents[3]
    email = member.contents[-2]
    print(f'Tên: {name.text}')
    print(f'Email: {email.text}')
    print('-'*20)

# Cach 2 
import requests
from bs4 import BeautifulSoup
url = 'https://fit.huit.edu.vn/gioi-thieu/ban-chu-nhiem-khoa'
response = requests.get(url)

if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser')
else:
    print(f'Lỗi mở trang. Mã lỗi: {response.status_code}')

elt = soup.find('div', class_="post-body not-copy content_bold")
ell = elt.find('tr', style="height: 318.525px;")
members = ell.find_all('td')
print('Tên và Email của BCN Khoa CNTT\n')

for i in range(len(members)):
    mem = members[i].find_all('p')

    name = mem[1]
    email = mem[-1]
    print(f'Tên: {name.text}')
    print(f'{email.text}')
    print('-'*20)




    
    
    



