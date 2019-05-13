import requests
from bs4 import BeautifulSoup

req = requests.get('https://www.daum.net/')
soup = BeautifulSoup(req.text, 'html.parser')
titles = soup.select('.hotissue_mini a[class*=link_issue]')
for title in titles : 
    print(title.get_text())
for i, title in enumerate(titles, 1):
    print(f'{i}위 {title.get_text()}')