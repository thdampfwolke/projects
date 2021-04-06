# ../app_sap/views.py

from django.shortcuts import render
from .models import Mitarbeiter

def fun_index(request):
    return render(request, 'index.html')

def fun_index_01(request):
    # dyn: ohne db: var in ../app_staff/models.py
    ma01 = Mitarbeiter()
    ma01.nname = 'ma01-nname-01'
    ma01.vname = 'ma01-vname-01'
    ma01.img = 'img_01.jpg'
    ma01.desc = 'ma01-desc-01'
    ma01.phone = 121
    ma01.offer = False

    ma02 = Mitarbeiter()
    ma02.nname = 'ma02-nname-01'
    ma02.vname = 'ma02-vname-01'
    ma02.img = 'img_02.jpg'
    ma02.desc = 'ma02-desc-01'
    ma02.phone = 232
    ma02.offer = True

    ma = [ma01, ma02]
    return render(request, 'index_01_dyn.html', {'ma': ma })


#def index_01(request):
#    # static:
#    return render(request, 'index_01.html')
#
#def index_02(request):
#    # dyn: ohne db: var2 in ../app_staff/views.py
#    return render(request, 'index_02.html', {'var2': 222})
#
#def index_03(request):
#    # dyn: ohne db: var in ../app_staff/models.py
#    ma01 = Mitarbeiter()
#    ma01.nname = 'ma01-nname-03'
#    ma01.vname = 'ma01-vname-03'
#    ma01.img = 'img_01.jpg'
#    ma01.desc = 'ma01-desc-03'
#    ma01.phone = 121
#    ma01.offer = False
#
#    ma02 = Mitarbeiter()
#    ma02.nname = 'ma02-nname-03'
#    ma02.vname = 'ma02-vname-03'
#    ma02.img = 'img_02.jpg'
#    ma02.desc = 'ma02-desc-03'
#    ma02.phone = 232
#    ma02.offer = True
#
#    ma03 = Mitarbeiter()
#    ma03.nname = 'ma03-nname-03'
#    ma03.vname = 'ma03-vname-03'
#    ma03.img = 'img_03.jpg'
#    ma03.desc = 'ma03-desc-03'
#    ma03.phone = 343
#    ma03.offer = False
#
#    return render(request, 'index_03.html', {'ma01': ma01, 'ma02': ma02, 'ma03': ma03 })