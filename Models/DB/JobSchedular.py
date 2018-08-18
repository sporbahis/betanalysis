# -*- coding: utf-8 -*-

from pymodm import MongoModel, fields
from Models.DB.DBConnectionSetting import connect


# Bahis sitesindeki ligleri bilgilerini içerir
class JobSchedular(MongoModel):
    FinishDate = fields.DateTimeField(required=False, blank=True)
    StartDate = fields.DateTimeField(required=True, blank=False)
    State = fields.CharField(required=True, blank=False)
    JobName = fields.CharField()

