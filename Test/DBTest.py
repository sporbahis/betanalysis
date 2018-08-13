# -*- coding: utf-8 -*-

from pymodm import fields
from datetime import datetime
from Models.DB.WebSites import WebSiteInfo
from Models.DB.MatchesRatios import MatchRatioInfo
from Models.DB.Leages import LeageInfo
from Models.DB.Matches import MatchInfo


# Create Web Site
web_site = WebSiteInfo()
web_site.Name = "Inter Bahis"
web_site.BaseUrl = "http://interbahis246.com"
web_site.Type = "InterBahis"
web_site.save()


# Create MatchRatio
macth_ratio = MatchRatioInfo()
macth_ratio.Type = "MAÇ SONUCU"
macth_ratio.Rate = "2.96"
macth_ratio.RateName = "Çaykur Rizespor"
macth_ratio.WebSiteMatchId = "869019265"
macth_ratio.CreateTime = datetime.now()
#macth_ratio.MatchInfo = "1"
macth_ratio.save()


# Create Match
match = MatchInfo()
match.Name = "Çaykur Rizespor - Kasımpaşa"
match.FirstTeamName = "Çaykur Rizespor"
match.SecondTeamName = "Kasımpaşa"
match.Date = datetime.now()
match.CreateTime = datetime.now()
match.WebSiteInfo = web_site._id
match.WebSiteMachId = "334324234"

# Create Leage
leage = LeageInfo()
leage.Name = "Türkiye Süper Lig"
leage.Matches = [match]
leage.save()



print("Veriler Hazır")