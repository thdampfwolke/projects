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
