from Models.DB.Matches import MatchInfo
from Models.DB.MatchesRatios import MatchRatioInfo
from Models.InterBahis import InterBahis
from datetime import datetime
from datetime import timedelta
import pprint

#t = InterBahis("http://interbahis246.com")
#t.find_leage()


class temp():
    Type = ""
    Name = ""
    labels = []

ratio_list = MatchInfo.objects.limit(10).all()
for match in ratio_list:
    print(set(x.Type for x in match.Ratios))
    break