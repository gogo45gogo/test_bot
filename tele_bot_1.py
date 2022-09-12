import requests
from bs4 import BeautifulSoup
import datetime
import re

import telegram

now = str(datetime.datetime.now())
#print('now :', now)
day = now[0:10].replace('-', '.')
print('오늘의 메뉴 :',day)

req = requests.get("https://stu.sen.go.kr/sts_sci_md01_001.do?schulCode=B100000420&schulCrseScCode=4&schulKndScCode=04&schMmealScCode=2&schYmd="+day)
#print(req.text)
soup = BeautifulSoup(req.text, "html.parser")
#print(soup)
element = soup.find_all("tr")
#print(element[0])
day_info = element[0].find_all('th', {'scope' :'col'})

i = 0
for date in day_info:
    if(re.match(day, date.text)):
        print(date.text)
        break
    i= i+1

#print(i)
element = element[2].find_all('td')
#print(element)

element = element[i]  # num
element = str(element)
element = element.replace('[', '')
element = element.replace(']', '')
element = element.replace('<br/>', '\n')
element = element.replace('<td class="textC last">', '')
element = element.replace('<td class="textC">', '')
element = element.replace('</td>', '')
element = element.replace('(h)', '')
element = element.replace('.', '')
element = re.sub(r"\d", "", element)

#print(element)

my_token = "5498553902:AAFnG_7EgNvv33T-Fg-JwM9ObTRt2a5FTu0"
bot = telegram.Bot(token=my_token)

#봇이 나에게 보내는 메세지 
bot.send_message(5696515180, "안녕~")

#식단 정보보내기
bot.send_message(5696515180, '오늘의 메뉴 :')
bot.send_message(5696515180, day)
bot.send_message(5696515180, element)

