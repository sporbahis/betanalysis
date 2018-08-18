# -*- coding: utf-8 -*-

from pymodm import MongoModel, fields
from Models.DB.WebSites import WebSiteInfo
from Models.DB.MatchesRatios import MatchRatioInfo
from Models.DB.Leages import LeageInfo

# Maç bilgilerini içerir
class MatchInfo(MongoModel):
    Name = fields.CharField(required=True,blank=False)
    FirstTeamName = fields.CharField(required=True,blank=False)
    SecondTeamName = fields.CharField(required=True,blank=False)
    Date = fields.DateTimeField(required=True,blank=False)
    CreateTime = fields.DateTimeField(required=True,blank=False)
    Ratios = fields.EmbeddedDocumentListField(MatchRatioInfo, default=[],blank=True)
    WebSiteMachId = fields.CharField()
    LeageInfo = fields.ReferenceField(LeageInfo, required=True)
    Hour = fields.CharField(required=True,blank=False)
    UniqueKey = fields.CharField(required=True, blank=False)
    #WebSiteInfo = fields.ReferenceField(WebSiteInfo, required=True)

    # Verileri yazdırmak için kullanılan fonksiyon
    @property
    def print(self):
        print("Maç Adı : " + str(self.Name))
        print("İlk Takım Adı : " + str(self.FirstTeamName))
        print("İkinci Takım Adı : " + str(self.SecondTeamName))
        print("Tarihi : " + str(self.Date))