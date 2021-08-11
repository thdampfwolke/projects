# ../app_pizza/urls.py

from django.urls import path
from . import views

app_name = 'app_pizza'

urlpatterns = [
  path('', views.index, name='index'),
  path('pizza/', views.pizzas, name='pizzas'),
  path('pizza/<int:pizza_id>/', views.pizza, name='pizza'),
]
