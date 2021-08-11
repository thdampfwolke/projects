# ../app_pizza/admin.py

from django.contrib import admin
from .models import Pizza
from .models import Beilagen

admin.site.register(Pizza)
admin.site.register(Beilagen)
