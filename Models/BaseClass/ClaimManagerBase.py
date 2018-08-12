# -*- coding: utf-8 -*-
"""
Bahis Sitelerinden oranları çekmek için oluşturulmuş temel sınıf
"""

class ClaimManagerBase:
    base_url = ""
    host = ""
    cookies = ""
    headers = {'Accept': '*/*;',
               'Accept-Encoding': 'gzip, deflate',
               'Accept-Language': 'tr-TR,tr;q=0.9,en-US;q=0.8,en;q=0.7',
               'Connection': 'keep-alive',
               'device': 'd',
               'X-Requested-With': 'XMLHttpRequest',
               'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.75 Safari/537.36',
               'Referer': 'interbahis246.com/sport/',
               'Host': 'interbahis246.com',
               'Cookie': '__nxquid=zWk8YQAAAAABk4LtLpr9CA==-1550005; trd=interbahis; websocket-url=socket-g1.pronetstatic.com; lang=1; user_timezone=-180; JSESSIONID=f2430ebb97766dd95bf683e85859; token=fc0b30faf8a17f1c2a53a42be4352cc8; token2=fc0b30faf8a17f1c2a53a42be4352cc8; __nxqsid=15338257200005; comm100_guid2_223564=ygMMlT2AVk6VuEYDoJXC-g'
               }
    def __init__(self):
        if self.base_url.startswith("http://"):
            self.headers["Host"] = self.base_url[7:]
        elif self.base_url.startswith("http://"):
            self.headers["Host"] = self.base_url[8:]
        self.headers["Referer"] = self.base_url

