from Models.DB.Matches import MatchInfo
from Models.DB.MatchesRatios import MatchRatioInfo
from Models.InterBahis import InterBahis
from datetime import datetime
from datetime import timedelta
import pprint

#t = InterBahis("http://interbahis246.com")
#t.find_leage()


ratio_list = []

temp_ratio = MatchRatioInfo()
temp_ratio.Type = "T1"
temp_ratio.CreateTime = datetime.utcnow()
temp_ratio.RateName = "N1"
temp_ratio.Rate = 1.9
temp_ratio.WebSiteMatchId = 1
ratio_list.append(temp_ratio)

temp_ratio = MatchRatioInfo()
temp_ratio.Type = "T1"
temp_ratio.CreateTime = datetime.utcnow()
temp_ratio.RateName = "N2"
temp_ratio.Rate = 1.9
temp_ratio.WebSiteMatchId = 1
ratio_list.append(temp_ratio)

temp_ratio = MatchRatioInfo()
temp_ratio.Type = "T1"
temp_ratio.CreateTime = datetime.utcnow()
temp_ratio.RateName = "N3"
temp_ratio.Rate = 1.8
temp_ratio.WebSiteMatchId = 1
ratio_list.append(temp_ratio)

temp_ratio = MatchRatioInfo()
temp_ratio.Type = "T2"
temp_ratio.CreateTime = datetime.utcnow()
temp_ratio.RateName = "N1"
temp_ratio.Rate = 1.7
temp_ratio.WebSiteMatchId = 1
ratio_list.append(temp_ratio)

temp_ratio = MatchRatioInfo()
temp_ratio.Type = "T1"
temp_ratio.CreateTime = datetime.utcnow() + timedelta(minutes=3)
temp_ratio.RateName = "N2"
temp_ratio.Rate = 1.6
temp_ratio.WebSiteMatchId = 1
ratio_list.append(temp_ratio)



ratio_list_new = []

temp_ratio = MatchRatioInfo()
temp_ratio.Type = "T1"
temp_ratio.CreateTime = datetime.utcnow() + timedelta(minutes=3)
temp_ratio.RateName = "N1"
temp_ratio.Rate = 1.9
temp_ratio.WebSiteMatchId = 1
ratio_list_new.append(temp_ratio)

temp_ratio = MatchRatioInfo()
temp_ratio.Type = "T1"
temp_ratio.CreateTime = datetime.utcnow()
temp_ratio.RateName = "N9"
temp_ratio.Rate = 1.9
temp_ratio.WebSiteMatchId = 1
ratio_list_new.append(temp_ratio)

temp_ratio = MatchRatioInfo()
temp_ratio.Type = "T1"
temp_ratio.CreateTime = datetime.utcnow()
temp_ratio.RateName = "N3"
temp_ratio.Rate = 1.5
temp_ratio.WebSiteMatchId = 1
ratio_list_new.append(temp_ratio)


temp_ratio = MatchRatioInfo()
temp_ratio.Type = "T1"
temp_ratio.CreateTime = datetime.utcnow()
temp_ratio.RateName = "N2"
temp_ratio.Rate = 1.6
temp_ratio.WebSiteMatchId = 1
ratio_list_new.append(temp_ratio)

temp_ratio = MatchRatioInfo()
temp_ratio.Type = "T2"
temp_ratio.CreateTime = datetime.utcnow()
temp_ratio.RateName = "N1"
temp_ratio.Rate = 1.8
temp_ratio.WebSiteMatchId = 1
ratio_list_new.append(temp_ratio)


temp_ratio = MatchRatioInfo()
temp_ratio.Type = "T1"
temp_ratio.CreateTime = datetime.utcnow()
temp_ratio.RateName = "N4"
temp_ratio.Rate = 1.6
temp_ratio.WebSiteMatchId = 1
ratio_list_new.append(temp_ratio)

temp_ratio = MatchRatioInfo()
temp_ratio.Type = "T3"
temp_ratio.CreateTime = datetime.utcnow()
temp_ratio.RateName = "N1"
temp_ratio.Rate = 1.5
temp_ratio.WebSiteMatchId = 1
ratio_list_new.append(temp_ratio)

def printmy(l1):
    print(l1.Type + "  " + l1.RateName + " " + str(l1.Rate) + " | " + l1.CreateTime.strftime('%d.%m.%Y %H:%M:%S'))

def filter(list_new,list_old):
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


ratio_list.sort(key=lambda x: (x.Type, x.RateName, x.CreateTime))


match = MatchInfo.objects.raw({"UniqueKey": "65ca687815a2fd3363208d47fd0a60c5de370c31be2e0f081b3f175d5ca5391c"}).all().first()
match.Ratios.sort(key=lambda x: (x.Type, x.RateName, x.CreateTime))
#match.Ratios.sort(key=lambda x: (x.Type, x.RateName, x.CreateTime))