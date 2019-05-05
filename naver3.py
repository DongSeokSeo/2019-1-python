import requests
from bs4 import BeautifulSoup

req = requests.get('https://www.naver.com/')
soup = BeautifulSoup(req.text, 'html.parser')
titles = soup.find_all('div','ah_list')
for title in titles : 
    print(title.get_text())
for i, title in enumerate(titles, 1):
    print(f'{i}위 {title.get_text()}')
