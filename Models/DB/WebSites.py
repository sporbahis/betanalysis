# -*- coding: utf-8 -*-

from pymodm import MongoModel, fields
from Models.DB.DBConnectionSetting import connect


# Bahis sitesindeki ligleri bilgilerini içerir
class WebSiteInfo(MongoModel):
    Name: fields.CharField(required=True,blank=False)
    BaseUrl: fields.CharField(required=True,blank=False)
    Type: fields.CharField(required=True,blank=False)
