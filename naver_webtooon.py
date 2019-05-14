import requests as rq
from bs4 import BeautifulSoup

URL = 'https://comic.naver.com/webtoon/weekdayList.nhn?week=mon'

response = rq.get(URL)
html = response.text
soup = BeautifulSoup(html,'html.parser')
stars = soup.find("div", {"class":"rating_type"})
span = div.find_all("span")


for strong in stars:
    print(span.text)







