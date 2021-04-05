# ../app_staff/views.py

from django.shortcuts import render

def index(request):
    return render(request, 'index.html')
    # return render(request, 'index.html')
    # return render(request.POST, 'index.html')
    
