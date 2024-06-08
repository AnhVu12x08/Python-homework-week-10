import requests
from bs4 import BeautifulSoup
import random 

def bai_1():
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


def bai_2a():
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


def bai_2b():
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


def bai_3():
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


def bai_4():
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


def bai_5():
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


def main():
    while True:
        print('*'*5)
        print('MENU: ')
        print('*'*5)
        print('0: Thoát chương trình')
        print('1: Tất cả thông báo trong 5 trang đầu tiên từ trang web khoa CNTT')
        print('2: Tên và Email của BCN Khoa CNTT ')
        print('3: Danh sách 10 việc làm IT mới nhất tại TP.HCM ')
        print('4: Ngày tháng, tên và URL từ mục Latest News của trang python.org')
        print('5: 10 mẫu tin giáo dục từ Dịch vụ Báo thanh niên RSS ')
        
        choice = input('Lựa chọn của bạn là: ')
        if choice == '1':
            bai_1()
        elif choice == '2':
            options = [bai_2a(), bai_2b()]
            random.choice(options)
        elif choice == '3':
            bai_3()
        elif choice == '4':
            bai_4()
        elif choice == '5':
            bai_5()
        elif choice == '0':
            break
        else:
            print('Không hợp lệ, nhập lại')

if __name__=="__main__": 
    main() 


