# ../app_sap/views.py

from django.shortcuts import render
from django.contrib.auth.models import User, auth
#from .models import Mitarbeiter
#from .models import Mitarbeiter2

def test_01(request):
    return render(request, 'test/test_01.html')
