# ../app_test/models.py

from django.db import models

class Staff(models.Model):
    # id = int
    nname          = models.CharField(max_length=120, null=False)
    vname          = models.CharField(max_length=120, null=False)
    geb            = models.DateField(null=True, blank=True)
    pic            = models.ImageField(upload_to='pics', null=True, blank=True)
    email          = models.CharField(max_length=254, null=True, blank=True)
    desc           = models.TextField(null=True, blank=True)
    check          = models.BooleanField(null=False, default=False)
    is_active      = models.BooleanField(null=False, default=True)
    date_beg       = models.DateField(null=False)
    date_end       = models.DateField(null=False, default='2099-12-31')
    date_created   = models.DateTimeField(auto_now_add=True)
    date_modified  = models.DateTimeField(auto_now=True)


# (null=True, blank=True)

# class Mitarbeiter2(models.Model):
#     # id = int
#     nname = models.CharField(max_length=120)
#     vname = models.CharField(max_length=120)
#     img = models.ImageField(upload_to='pics')
#     desc = models.TextField()
#     phone = models.IntegerField()
#     handy = models.IntegerField()
#     offer = models.BooleanField(default=False)