# ../app_pizza/models.py

from django.db import models


class Pizza(models.Model):
    name    = models.CharField(max_length=63)
    preis   = models.DecimalField(max_digits=5, decimal_places=2)
    date_add = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "pizza"

    def __str__(self):
        return self.name


class Beilagen(models.Model):
    pizza = models.ForeignKey(Pizza, on_delete=models.CASCADE)
    name = models.CharField(max_length=63)
    preis = models.DecimalField(max_digits=5, decimal_places=2)
    date_add = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "beilagen"

    def __str__(self):
        return self.name
