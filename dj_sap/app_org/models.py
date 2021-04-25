# ../app_org/models.py

from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


# app_org_zmitarbeiter_rollen
# id  zmitarbeiter_id     zrolle_id
# 1   1                   1
# 2   1                   3

class Zmitarbeiter(models.Model):
    # id = int
    nachname = models.CharField(max_length=120, null=False)
    vorname = models.CharField(max_length=120, null=False)
    geburtstag = models.DateField(null=True, blank=True)
    bild = models.ImageField(upload_to='images', null=True, blank=True)
    email = models.CharField(max_length=254, null=True, blank=True)
    beschreibung = models.TextField(null=True, blank=True)
    check = models.BooleanField(null=False, default=False)
    is_active = models.BooleanField(null=False, default=True)
    date_beg = models.DateField(null=False)
    date_end = models.DateField(null=False, default='2099-12-31')
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
    rollen = models.ManyToManyField("Zrolle", blank=True)   # tab: app_org_zmitarbeiter_rollen

    def __str__(self):
        return f"{self.nachname}, {self.vorname}, {self.email}, {self.geburtstag}"

    class Meta:
        verbose_name_plural = "Mitarbeiter"
        unique_together = ("nachname", "vorname", "geburtstag", )


class Zrolle(models.Model):
    # id = int
    rolle = models.CharField(max_length=120)
    beschreibung = models.TextField(null=True, blank=True)
    check = models.BooleanField(null=False, default=False)
    is_active = models.BooleanField(null=False, default=True)
    date_beg = models.DateField(null=False)
    date_end = models.DateField(null=False, default='2099-12-31')
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.rolle}, {self.beschreibung}"

    class Meta:
        verbose_name_plural = "Rolle"
