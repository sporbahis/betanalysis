# -*- coding: utf-8 -*-

# interbayis sitesinden oranları çekmek için hazırlanan sınıf
# Link : http://interbahis246.com/sports/1/
# Bu link Maçların 3 günlük verilerini çekmek için
# Görsele Göre Yanlış olabilir

import requests
import urllib.parse
from datetime import datetime
from bs4 import BeautifulSoup
from Models.BaseClass.ClaimManagerBase import ClaimManagerBase
from Models.DB.MatchesRatios import MatchRatioInfo
from Models.DB.Leages import LeageInfo
from Models.DB.Matches import MatchInfo


class InterBahis(ClaimManagerBase):
    def __init__(self,base_url):
        ClaimManagerBase.base_url = base_url
        ClaimManagerBase.__init__(self)
        self._set_cookie()

    def find_ratio_type(self,ratioList):
        ratio_type = None
        for item in ratioList.find_all("div",class_="sub-rate-title"):
            for item2 in item.find_all("span"):
                ratio_type = item2.contents[0]
        return ratio_type

    def find_ratio_name(self,ratioList):
        name = "???????????"
        for item in ratioList.find_all("span",class_="main-team"):
            name = item.contents[0]
        return name

    def find_ratio_rate(self,ratioList):
        rate = "???????????"
        for item in ratioList.find_all("span",class_="main-rate"):
            rate = item.contents[0]
        return rate

    def find_ratio(self,ratioList,type,match,leage):
        ratio_list = []
        for item1 in ratioList.find_all("div",class_="fixturelayout-rate"):
            for item2 in item1.find_all("li"):
                for item3 in item2.find_all("a",class_="anaoran"):
                    if len(item3) > 0:
                        temp_ratio = MatchRatioInfo()
                        temp_ratio.Type = type
                        temp_ratio.CreateTime = datetime.now()
                        temp_ratio.Name = self.find_ratio_name(item3)
                        temp_ratio.Rate = self.find_ratio_rate(item3)
                        print("_____________________________________________________________________________________________________")
                        leage.print()
                        match.print()
                        temp_ratio.print()
                        print("_____________________________________________________________________________________________________")
                        ratio_list.append(temp_ratio)
        return ratio_list

    def find_match_ratio(self,temp_match,leage):
        url = ClaimManagerBase.base_url + "/oddspop/" + str(temp_match.WebsiteId) + "/"
        html_request = requests.get(url, headers=ClaimManagerBase.headers, timeout=500000, allow_redirects=False)
        html = BeautifulSoup(html_request.content, 'html.parser')
        ratio_list = []
        for item in html.find_all('div',class_="sub-main-well"):
            ratio_type = self.find_ratio_type(item)
            ratio_list.append(self.find_ratio(item,ratio_type,temp_match,leage))
        return ratio_list

    def find_match_detail_id(self,html):
        match_detail_link = None
        for item in html.find_all('a', class_='fixture-bet-others-button'):
            match_detail_link = str(item["onclick"]).strip("showdynoddspop(")[:-2]
        return match_detail_link

    def find_match(self,html,leage):
        match_list = []
        for item in html.find_all("div",class_="fixturelayout"):
            temp_match = MatchInfo()
            temp_match.WebsiteId = self.find_match_detail_id(item)
            temp_match.FirstTeamName = self.find_match_first_team_name(item)
            temp_match.SecondTeamName = self.find_match_second_team_name(item)
            temp_match.Hour = self.find_match_hour(item)
            temp_match.Date = self.find_match_date(item)
            temp_match.RecordTime = datetime.now()
            temp_match.Name = temp_match.FirstTeamName+" - "+temp_match.SecondTeamName
            temp_match.Ratios.append(self.find_match_ratio(temp_match,leage))
            match_list.append(temp_match)
            if len(match_list) > 2:
                break
        return match_list


    def find_match_first_team_name(self,html):
        first_team_name = "??????????????????????????????????"
        for item1 in html.find_all("li",class_="fixture-event-name"):
            for item2 in item1.find_all("a",class_="fixture-stats-team"):
                first_team_name = item2.contents[0]
                break
        return first_team_name

    def find_match_second_team_name(self,html):
        second_team_name = "??????????????????????????????????"
        for item1 in html.find_all("li", class_="fixture-event-name"):
            for item2 in item1.find_all("a", class_="fixture-stats-team"):
                second_team_name = item2.contents[0]
        return second_team_name

    def find_match_hour(self,html):
        hour = "??????????????????????????????????"
        for item in html.find_all("li", class_="fixture-time"):
            hour = item.contents[0]
        return hour

    def find_match_date(self,html):
        date = "??????????????????????????????????"
        for item in html.find_all("li", class_="fixture-date"):
            date = item.contents[0]
        return date


    def find_leage_name(self,html):
        leage_name = "??????????????????????????????????"
        for item in html.find_all("div",class_="main-date-title"):
            for item2 in item.find_all("strong"):
                leage_name = item2.contents[0]
        return  leage_name


    def find_leage(self):
        url = urllib.parse.urljoin(ClaimManagerBase.base_url, 'sports/1/')
        html_request = requests.get(url, headers=ClaimManagerBase.headers, timeout=500000, allow_redirects=False)
        html = BeautifulSoup(html_request.content, 'html.parser')

        for item in html.find_all('div',class_="fixture-season-main-wrap"):
            temp_leage = LeageInfo()
            temp_leage.Name = self.find_leage_name(item)
            temp_leage.Matches.append(self.find_match(item,temp_leage))


    def _set_cookie(self):
       try:
           html_request = requests.get(ClaimManagerBase.base_url, headers=ClaimManagerBase.headers,timeout=500000,allow_redirects=False)
           if html_request.status_code == 200:
               ClaimManagerBase.cookies = html_request.cookies
       except Exception:
            print("Hata Testi")
