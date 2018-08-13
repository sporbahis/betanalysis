# -*- coding: utf-8 -*-

from pymodm import fields
from datetime import datetime
from Models.DB.WebSites import WebSiteInfo
from Models.DB.MatchesRatios import MatchRatioInfo
from Models.DB.Leages import LeageInfo
from Models.DB.Matches import MatchInfo

temp_ratio = MatchRatioInfo()
temp_ratio.Type = "Deneme type"
temp_ratio.CreateTime = datetime.now()
temp_ratio.RateName = "Deneme"
temp_ratio.Rate = str("1,9".replace(',','.'))
temp_ratio.save()