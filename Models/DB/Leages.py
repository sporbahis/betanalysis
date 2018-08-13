# -*- coding: utf-8 -*-

from pymodm import MongoModel, fields
from Models.DB.DBConnectionSetting import connect

# Bahis sitesindeki ligleri bilgilerini içerir
class LeageInfo(MongoModel):
    Name = fields.CharField(required=True)

    # Verileri yazdırmak için kullanılan fonksiyon
    @property
    def print(self):
        print("Name : " + self.Name)