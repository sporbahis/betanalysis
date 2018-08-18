# -*- coding: utf-8 -*-

# interbayis sitesinden oranları çekmek için hazırlanan sınıf
# Link : http://interbahis246.com/sports/1/
# Bu link Maçların 3 günlük verilerini çekmek için
# Görsele Göre Yanlış olabilir

import requests
import urllib.parse
import hashlib
from datetime import datetime
from bs4 import BeautifulSoup
from collections import namedtuple
from Models.BaseClass.ClaimManagerBase import ClaimManagerBase
from Models.DB.MatchesRatios import MatchRatioInfo
from Models.DB.Leages import LeageInfo
from Models.DB.Matches import MatchInfo


class InterBahis(ClaimManagerBase):
    def __init__(self, base_url):
        ClaimManagerBase.base_url = base_url
        ClaimManagerBase.__init__(self)
        self._set_cookie()

    def find_ratio_type(self, ratioList):
        ratio_type = None
        for item in ratioList.find_all("div", class_="sub-rate-title"):
            for item2 in item.find_all("span"):
                ratio_type = item2.contents[0]
        return ratio_type

    def find_ratio_name(self, ratioList):
        name = "???????????"
        for item in ratioList.find_all("span", class_="main-team"):
            name = item.contents[0]
        return name

    def find_ratio_rate(self, ratioList):
        rate = "-0"
        for item in ratioList.find_all("span", class_="main-rate"):
            rate = item.contents[0]
        return str(rate.replace(',', '.'))

    def find_ratio(self, ratioList, type, match, leage):
        ratio_list = []
        for item1 in ratioList.find_all("div", class_="fixturelayout-rate"):
            for item2 in item1.find_all("li"):
                for item3 in item2.find_all("a", class_="anaoran"):
                    temp_ratio = MatchRatioInfo()
                    temp_ratio.Type = type
                    temp_ratio.CreateTime = datetime.utcnow()
                    temp_ratio.RateName = self.find_ratio_name(item3)
                    temp_ratio.Rate = self.find_ratio_rate(item3)
                    temp_ratio.WebSiteMatchId = 1
                    ratio_list.append(temp_ratio)
        return ratio_list

    def find_match_ratio(self, temp_match, leage):
        url = ClaimManagerBase.base_url + "/oddspop/" + str(temp_match.WebSiteMachId) + "/"
        html_request = requests.get(url, headers=ClaimManagerBase.headers, timeout=500000, allow_redirects=False)
        html = BeautifulSoup(html_request.content, 'html.parser')
        ratio_list = []
        for item in html.find_all('div', class_="sub-main-well"):
            ratio_type = self.find_ratio_type(item)
            test = self.find_ratio(item, ratio_type, temp_match, leage)
            ratio_list = ratio_list + test
        return ratio_list

    def find_match_detail_id(self, html):
        match_detail_link = None
        for item in html.find_all('a', class_='fixture-bet-others-button'):
            match_detail_link = str(item["onclick"]).strip("showdynoddspop(")[:-2]
        return match_detail_link

    def find_match(self, html, leage):
        match_list = []
        now = datetime.now()

        for item in html.find_all("div", class_="fixturelayout"):
            f_team = self.find_match_first_team_name(item)
            s_team = self.find_match_second_team_name(item)
            s_date = self.find_match_date(item)
            s_hour = self.find_match_hour(item)
            s_date = datetime.strptime(s_date + "." + str(now.year) + s_hour, '%d.%m.%Y%H:%M')
            unique_key = self.encrypt_string(f_team + s_team + s_date.strftime("%y-%m-%d-%H-%M"))
            try:
                match = MatchInfo.objects.raw({"UniqueKey": unique_key}).all().first()
                match.WebSiteMachId = self.find_match_detail_id(item)
                match.Ratios.sort(key=lambda x: (x.Type, x.RateName, x.CreateTime))
                temp_ratios = self.find_match_ratio(match, leage)
                match.Ratios = match.Ratios + self.filter(temp_ratios,match.Ratios)
                match.save()
            except MatchInfo.DoesNotExist:
                match = MatchInfo()
                match.WebSiteMachId = self.find_match_detail_id(item)
                match.FirstTeamName = f_team
                match.SecondTeamName = s_team
                match.Hour = s_hour
                match.Date = s_date
                match.CreateTime = datetime.utcnow()
                match.Name = f_team + " - " + s_team
                match.LeageInfo = leage._id
                match.Ratios = match.Ratios + self.find_match_ratio(match, leage)
                match.UniqueKey = unique_key
                match.save()
                match_list.append(match)
        return match_list


    def find_match_first_team_name(self, html):
        first_team_name = "??????????????????????????????????"
        for item1 in html.find_all("li", class_="fixture-event-name"):
            for item2 in item1.find_all("a", class_="fixture-stats-team"):
                first_team_name = item2.contents[0]
                break
        return first_team_name


    def find_match_second_team_name(self, html):
        second_team_name = "??????????????????????????????????"
        for item1 in html.find_all("li", class_="fixture-event-name"):
            for item2 in item1.find_all("a", class_="fixture-stats-team"):
                second_team_name = item2.contents[0]
        return second_team_name


    def find_match_hour(self, html):
        hour = "??????????????????????????????????"
        for item in html.find_all("li", class_="fixture-time"):
            hour = item.contents[0]
        return hour


    def find_match_date(self, html):
        date = ""
        for item in html.find_all("li", class_="fixture-date"):
            date = item.contents[0]
        return date


    def find_leage_name(self, html):
        leage_name = "??????????????????????????????????"
        for item in html.find_all("div", class_="main-date-title"):
            for item2 in item.find_all("strong"):
                leage_name = item2.contents[0]
        return leage_name


    def find_seassion_name(self, html, ):
        seassion_name = ""
        id = ""
        for item in html.find_all("span", class_="fixtureseasons-title"):
            temp = str(item.parent["data-target"])
            if temp[:1] == "#":
                seassion_name = item.contents
                id = item.parent["data-target"].strip("#")
        return (seassion_name, id)


    def find_leage(self):
        url = urllib.parse.urljoin(ClaimManagerBase.base_url, 'sports/1/')
        html_request = requests.get(url, headers=ClaimManagerBase.headers, timeout=500000, allow_redirects=False)
        html = BeautifulSoup(html_request.content, 'html.parser')

        for item in html.find_all("span", class_="fixtureseasons-title"):
            temp = str(item.parent["data-target"])
            if temp[:1] == "#":
                id = item.parent["data-target"].strip("#")
                name = self.find_leage_name(item.parent.parent.parent)
                seassion_name = item.contents[0]
                unique_key = self.encrypt_string(name + seassion_name)
                try:
                    leage = LeageInfo.objects.raw({"UniqueKey": unique_key})
                except LeageInfo.DoesNotExist:
                    leage = LeageInfo()
                    leage.Name = name
                    leage.SeassionName = item.contents[0]
                    leage.UniqueKey = self.encrypt_string(leage.Name + leage.SeassionName)
                    leage.save()
                session_html = item.parent.parent.find_all("div", {'id': id})
                self.find_match(session_html[0],leage)

    def filter(self,list_new, list_old):
        update_list = []
        for item in list_new:
            for item1 in list_old:
                if item.Type == item1.Type and item.RateName == item1.RateName and item1.Rate != item.Rate:
                    update_list.append(item)
                elif item.Type == item1.Type and item.RateName == item1.RateName and item1.Rate == item.Rate:
                    break
                elif item.Type != item1.Type or item.RateName != item1.RateName:
                    update_list.append(item)
                    break
        update_list.sort(key=lambda x: (x.Type, x.RateName, x.CreateTime))
        return update_list


    def encrypt_string(self, hash_string):
        sha_signature = hashlib.sha256(hash_string.encode()).hexdigest()
        return sha_signature


    def _set_cookie(self):
        try:
            html_request = requests.get(ClaimManagerBase.base_url, headers=ClaimManagerBase.headers, timeout=500000,
                                        allow_redirects=False)
            if html_request.status_code == 200:
                ClaimManagerBase.cookies = html_request.cookies
        except Exception:
            print("Hata Testi")
