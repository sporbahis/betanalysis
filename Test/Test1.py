from Models.DB.MatchesRatios import MatchRatioInfo
from Models.InterBahis import InterBahis
from datetime import datetime
from datetime import timedelta
import pprint

t = InterBahis("http://interbahis247.com")
t.find_leage()
