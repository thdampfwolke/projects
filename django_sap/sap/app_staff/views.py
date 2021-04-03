# ../app_staff/views.py

from django.shortcuts import render
# from django.http import HttpResponse

def home(request):
    # return HttpResponse("Hello World")    # 04
    # return render(request, 'home.html')   # 05
    return render(request, 'home.html', {'name':'name'})

def add(request):
    # val1 = int(request.GET['num1'])
    # val2 = int(request.GET['num2'])
    val1 = int(request.POST['num1'])
    val2 = int(request.POST['num2'])
    res  = val1 + val2
    return render(request, 'result.html', {'result':res})
