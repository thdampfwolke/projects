# ../app_staff/views.py

from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def index_01(request):
    return render(request, 'index_01.html')

def index_02(request):
    return render(request, 'index_02.html')
