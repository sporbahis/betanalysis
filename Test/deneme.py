import hashlib

from Models.DB.Leages import LeageInfo
from Models.DB.Matches import MatchInfo
from Models.DB.MatchesRatios import MatchRatioInfo
from Models.InterBahis import InterBahis
from datetime import datetime
from datetime import timedelta
import pprint
import re

def group_by_type(list):
    temp_dict = dict()
    for x in list:
        temp_name = re.sub('[^a-zA-Z0-9]+', '', x.Type).lower()
        temp_dict.setdefault(temp_name,[]).append(x)
    return temp_dict



test = matches = MatchInfo.objects.limit(10).all().first()

group_by_type(test.Ratios)