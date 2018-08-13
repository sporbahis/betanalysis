# -*- coding: utf-8 -*-

from pymodm import EmbeddedMongoModel, fields

# Bir maçtaki aynı kategorideki oranların bilgilerini içerir
class MatchRatioInfo(EmbeddedMongoModel):
    Type = fields.CharField(required=True, blank=False)
    Rate = fields.Decimal128Field()
    RateName = fields.CharField(required=True,blank=False)
    WebSiteMatchId = fields.CharField()
    CreateTime = fields.DateTimeField(required=True,blank=False)
    #MatchInfo = fields.ReferenceField(MatchInfo, required=True)

    # Verileri yazdırmak için kullanılan fonksiyon
    @property
    def print(self):
        print("Tipi : " + str(self.Type))
        print("Oran Adı : " + str(self.Name))
        print("Oran : " + str(self.Rate))
        print("Oluşturulma Zamanı : " + str(self.CreateTime))