import requests
from bs4 import BeautifulSoup

days=['mon','tue','wed','thu','fri','sat','sun']
day = days[0]
url = 'https://comic.naver.com/webtoon/weekdayList.nhn?week='+day
#  https://comic.naver.com/webtoon/weekdayList.nhn?week=mon


response = requests.get(url)
html = response.text
soup = BeautifulSoup(html,'html.parser')
titles = soup.find_all('dt')

print (titles)
for title in titles:
    print(title.text)


    
