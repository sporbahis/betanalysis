# -*- coding: utf-8 -*-

from pymodm import EmbeddedMongoModel, fields
from Models.DB.MatchesRatios import MatchRatioInfo
from Models.DB.WebSites import WebSiteInfo
from Models.DB.DBConnectionSetting import connect

# Maç bilgilerini içerir
class MatchInfo(EmbeddedMongoModel):
    Name = fields.CharField(required=True,blank=False)
    FirstTeamName = fields.CharField(required=True,blank=False)
    SecondTeamName = fields.CharField(required=True,blank=False)
    Date = fields.DateTimeField(required=True,blank=False)
    CreateTime = fields.TimestampField(required=True,blank=False)
    Ratios = []
    WebSiteInfo = fields.ReferenceField(WebSiteInfo, required=True)
    WebSiteMachId = fields.CharField()

    # Verileri yazdırmak için kullanılan fonksiyon
    @property
    def print(self):
        print("Maç Adı : " + str(self.Name))
        print("İlk Takım Adı : " + str(self.FirstTeamName))
        print("İkinci Takım Adı : " + str(self.SecondTeamName))
        print("Tarihi : " + str(self.Date))