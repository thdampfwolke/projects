# ../app_test/models.py

from django.db import models

class Staff(models.Model):
    # id = int
    nname          = models.CharField(max_length=120)
    vname          = models.CharField(max_length=120)
    geb            = models.DateField()
    pic            = models.ImageField(upload_to='pics')
    email          = models.CharField(max_length=254)
    desc           = models.TextField()
    check          = models.BooleanField(default=False)
    is_active      = models.BooleanField(default=True)
    date_beg       = models.DateField()
    date_end       = models.DateField()
    date_created   = models.DateTimeField(auto_now_add=True)
    date_modified  = models.DateTimeField(auto_now=True)


# class Mitarbeiter2(models.Model):
#     # id = int
#     nname = models.CharField(max_length=120)
#     vname = models.CharField(max_length=120)
#     img = models.ImageField(upload_to='pics')
#     desc = models.TextField()
#     phone = models.IntegerField()
#     handy = models.IntegerField()
#     offer = models.BooleanField(default=False)