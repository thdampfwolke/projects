# ../app_sap/views.py

from django.shortcuts import render
from django.contrib.auth.models import User, auth

from .models import Staff


def test_01(request):
    return render(request, 'test/test_01.html')

def test_02(request):
    # dyn: mit db: ../app_test/models.py
    staff = Staff.objects.all
    return render(request, 'test/test_02.html', {'staff': staff})