# ../app_staff/views.py

from django.shortcuts import render
from .models import Mitarbeiter

def index(request):
    return render(request, 'index.html')

def index_01(request):
    # static:
    return render(request, 'index_01.html')

def index_02(request):
    # dyn: ohne db: var2 in ../app_staff/views.py
    return render(request, 'index_02.html', {'var2': 222})

def index_03(request):
    # dyn: ohne db: var in ../app_staff/models.py
    ma01 = Mitarbeiter()
    ma01.nname = 'ma01-nname-03'
    ma01.vname = 'ma01-vname-03'
    ma01.img = 'img_01.jpg'
    ma01.desc = 'ma01-desc-03'
    ma01.phone = 121

    ma02 = Mitarbeiter()
    ma02.nname = 'ma02-nname-03'
    ma02.vname = 'ma02-vname-03'
    ma02.img = 'img_02.jpg'
    ma02.desc = 'ma02-desc-03'
    ma02.phone = 232

    ma03 = Mitarbeiter()
    ma03.nname = 'ma03-nname-03'
    ma03.vname = 'ma03-vname-03'
    ma03.img = 'img_03.jpg'
    ma03.desc = 'ma03-desc-03'
    ma03.phone = 343

    return render(request, 'index_03.html', {'ma01': ma01, 'ma02': ma02, 'ma03': ma03 })


def index_04(request):
    # dyn: ohne db: var in ../app_staff/models.py
    ma04 = Mitarbeiter()
    ma04.nname = 'ma04-nname-04'
    ma04.vname = 'ma04-vname-04'
    ma04.img = 'img_04.jpg'
    ma04.desc = 'ma04-desc-04'
    ma04.phone = 454

    ma05 = Mitarbeiter()
    ma05.nname = 'ma05-nname-04'
    ma05.vname = 'ma05-vname-04'
    ma05.img = 'img_05.jpg'
    ma05.desc = 'ma05-desc-04'
    ma05.phone = 565

    ma06 = Mitarbeiter()
    ma06.nname = 'ma06-nname-04'
    ma06.vname = 'ma06-vname-04'
    ma06.img = 'img_06.jpg'
    ma06.desc = 'ma06-desc-04'
    ma06.phone = 676

    ma = [ma04, ma05, ma06]
    return render(request, 'index_04.html', {'ma': ma })

