# ../app_org/views.py


from django.shortcuts import render
from django.contrib.auth.models import User, auth
# from .models import Mitarbeiter
# from .models import Mitarbeiter2


def index(request):
    return render(request, 'index.html')


#def test_01(request):
#    # dyn: ohne db: var in ../app_org/models.py
#    ma01 = Mitarbeiter()
#    ma01.nname = 'ma01-nname-01'
#    ma01.vname = 'ma01-vname-01'
#    ma01.img = 'img_01.jpg'
#    ma01.desc = 'ma01-desc-01'
#    ma01.phone = 121
#    ma01.offer = False
#
#    ma02 = Mitarbeiter()
#    ma02.nname = 'ma02-nname-01'
#    ma02.vname = 'ma02-vname-01'
#    ma02.img = 'img_02.jpg'
#    ma02.desc = 'ma02-desc-01'
#    ma02.phone = 232
#    ma02.offer = True
#
#    ma = [ma01, ma02]
#    return render(request, 'test_01_dyn.html', {'ma': ma })


#def test_02(request):
#    # dyn: mit db: ../app_org/models.py - Mitarbeiter2
#    staff = Mitarbeiter2.objects.all
#    return render(request, 'test_02_dyn_db.html', {'staff': staff})
