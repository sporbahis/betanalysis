# -*- coding: utf-8 -*-
import sys
import codecs
import requests
from bs4 import BeautifulSoup
url="http://interbahis246.com/oddspop/14335307/"
url2=""
headers = {'Accept': 'text/html, */*; q=0.01',
           'Accept-Encoding':'gzip, deflate',
           'Accept-Language':'tr-TR,tr;q=0.9,en-US;q=0.8,en;q=0.7',
           'Connection':'keep-alive',
           'device':'d',
           'X-Requested-With':'XMLHttpRequest',
           'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.75 Safari/537.36',
           'Referer':'http://interbahis246.com/sport/',
           'Host':'interbahis246.com',
           'Cookie':'__nxquid=zWk8YQAAAAABk4LtLpr9CA==-1550005; trd=interbahis; websocket-url=socket-g1.pronetstatic.com; lang=1; user_timezone=-180; JSESSIONID=f2430ebb97766dd95bf683e85859; token=fc0b30faf8a17f1c2a53a42be4352cc8; token2=fc0b30faf8a17f1c2a53a42be4352cc8; __nxqsid=15338257200005; comm100_guid2_223564=ygMMlT2AVk6VuEYDoJXC-g'
           }

htmlRequest = requests.get(url,headers=headers)
webSiteCookie = htmlRequest.cookies


soup = BeautifulSoup(htmlRequest.content, 'html.parser')

print(soup.prettify())

#text_file = open("test2.html", "wb")
#text_file.write(htmlRequest.text.encode('utf8'))
#text_file.close()
print("Veriler Hazır")

for item in html.find_all('div', class_="fixture-season-main-wrap"):
    temp_leage = LeageInfo()
    temp_leage.Name = self.find_leage_name(item)
    temp_leage.SeassionName, id = self.find_seassion_name(item)
    print("-------------------------------------")
    print(temp_leage.SeassionName)
    print(id)
    # temp_leage.save()
    # self.find_match(item, temp_leage)
    test = test + 1
    print("-------------------------------------")
    if test > 3:
        print("test" + str(test))
        break