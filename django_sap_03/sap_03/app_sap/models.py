# ../app_sap/models.py

from django.db import models

class Mitarbeiter:
    id = int
    nname = str
    vname = str
    img = str
    desc = str
    phone = int
    offer = bool


class Mitarbeiter2(models.Model):
    # id = int
    nname = models.CharField(max_length=120)
    vname = models.CharField(max_length=120)
    img = models.ImageField(upload_to='pics')
    desc = models.TextField()
    phone = models.IntegerField()
    handy = models.IntegerField()
    offer = models.BooleanField(default=False)