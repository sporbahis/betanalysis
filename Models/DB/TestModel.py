# -*- coding: utf-8 -*-

from pymodm import MongoModel, fields
from Models.DB.DBConnectionSetting import connect


# Bahis sitesindeki ligleri bilgilerini içerir
class TestModel(MongoModel):
    Date = fields.DateTimeField(required=True, blank=False)

