# -*- coding: utf-8 -*-

import requests
from bs4 import BeautifulSoup







url="http://interbahis246.com/sports/1/"
headers = {'Accept': '*/*',
           'Accept-Encoding':'gzip, deflate',
           'Accept-Language':'tr-TR,tr;q=0.9,en-US;q=0.8,en;q=0.7',
           'Connection':'keep-alive',
           'device':'d',
           'X-Requested-With':'XMLHttpRequest',
           'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.75 Safari/537.36',
           'Referer':'http://interbahis246.com/sport/',
           'Host':'interbahis246.com',
           'Cookie':'__nxquid=zWk8YQAAAAABk4LtLpr9CA==-1550005; trd=interbahis; websocket-url=socket-g1.pronetstatic.com; lang=1; user_timezone=-180; __nxqsid=15338257200005; comm100_guid2_223564=ygMMlT2AVk6VuEYDoJXC-g; JSESSIONID=f5eda808d511b3e83ac5e3af351c; token=cb4e68b80f99d156a2d6d0f704f72cbe; token2=cb4e68b80f99d156a2d6d0f704f72cbe'
           }

htmlRequest = requests.get(url,headers=headers)
webSiteCookie = htmlRequest.cookies

soup = BeautifulSoup(htmlRequest.content, 'html.parser')

list = soup.find_all('a', class_='fixture-bet-others-button')

for a in list:
    print(a["onclick"])
#text_file = open("test.html", "wb")

#text_file.write(htmlRequest.text.encode('utf8'))
#text_file.close()
print("Veriler Hazır")