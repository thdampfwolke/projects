# ../app_staff/views.py

from django.shortcuts import render
# from django.http import HttpResponse

def home(request):
    # return HttpResponse("Hello World")    # 04
    # return render(request, 'home.html')   # 05
    return render(request, 'home.html', {'name':'Navin'})   # 06
