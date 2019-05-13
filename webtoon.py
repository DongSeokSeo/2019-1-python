import requests
from bs4 import BeautifulSoup
import re
days=['mon','tue','wed','thu','fri','sat','sun']
day = days[0]
url = 'https://comic.naver.com/webtoon/weekdayList.nhn?week'+day
# - https://comic.naver.com/webtoon/weekdayList.nhn?week=mon
response = requests.get(url)
html = response.text
soup = BeautifulSoup(html,'html.parser')
title_pattern = re.compile('/webtoon/list.nhn?titleId=')
titles = soup.find_all('a', attrs={'herf': title_pattern})

for title in titles :
    print (title.text)

    
