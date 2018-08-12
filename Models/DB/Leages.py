# -*- coding: utf-8 -*-

from pymodm import MongoModel, fields
from Models.DB.Matches import MatchInfo
from Models.DB.DBConnectionSetting import connect

# Bahis sitesindeki ligleri bilgilerini içerir
class LeageInfo(MongoModel):
    Name = fields.CharField(required=True)
    Matches = fields.EmbeddedDocumentListField(MatchInfo, default=[])

    # Verileri yazdırmak için kullanılan fonksiyon
    @property
    def print(self):
        print("Name : " + self.Name)