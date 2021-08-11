# ../app_pizza/views.py

from django.shortcuts import render
from .models import Pizza

def index(request):
  return render(request, 'app_pizza/index.html')

def pizzas(request):
  pizzas = Pizza.objects.order_by('date_add')
  context = {'pizzas': pizzas}
  return render(request, 'app_pizza/pizzas.html', context)

def pizza(request, pizza_id):
  pizza = Pizza.objects.get(id=topic_id)
  beilagen = pizza.beilagen_set.order_by('-date_add')
  context = {'pizza': pizza, 'beilagen': beilagen}
  return render(request, 'app_pizza/pizza.html', context)
