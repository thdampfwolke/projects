# ../app_pizzas/models.py

from django.db import models


class Pizza(models.Model):
    """pizza: welche soll es sein"""
    name = models.CharField(max_length=50)
    preis = models.DecimalField(max_digits=5, decimal_places=2)
    date_add = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "pizza"

    def __str__(self):
        return self.name


class Topping(models.Model):
    """topping: welche soll es sein"""
    pizza = models.ForeignKey(Pizza, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    preis = models.DecimalField(max_digits=5, decimal_places=2)
    date_add = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "topping"

    def __str__(self):
        return self.name
