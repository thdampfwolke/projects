# ../app_pizza/admin.py

from django.contrib import admin
from .models import Pizza, Topping

admin.site.register(Pizza)
admin.site.register(Topping)
