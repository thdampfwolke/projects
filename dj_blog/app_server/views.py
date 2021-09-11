# ------------------------------------------------------------------
# ../dj_blog/app_server/views.py
# ------------------------------------------------------------------

from django.shortcuts import render
from django.http import HttpResponse
# import datetime

# from django.shortcuts import render, redirect, get_object_or_404
# from django.contrib.auth.decorators import login_required

from .models import Server, Verfahren
from .models import H2H_server2verfahren, T2T_server2verfahren
# from .forms import TopicForm, EntryForm


# ============================================================================
# tab loeschen; ueber tab_h2h -> tab_t2t fuellen;
#  srv_id und verf_id ermitteln und in tab_t2t schreiben
# ============================================================================


# ------------------------------------------------------------------
def f_del_t2t():

    # inhalt von tab vollstaendig loeschen
    T2T_server2verfahren.objects.all().delete()


# ------------------------------------------------------------------
def f_add_t2t():

    # inhalt von tab vollstaendig loeschen
    T2T_server2verfahren.objects.all().delete()

    data_server = Server.objects.all()              # neue server tab einlesen
    # print('xxx---', data_server, '---XXX')

    for d_srv in data_server:                       # einezelne server von server tab durchgehen
        # print(d_srv.id, d_srv.name)

        # d_h2h: alle server-infos (id, server, verfahren) von tab_h2h einlesen
        d_h2h = H2H_server2verfahren.objects.get(server=d_srv.name)
        # print(d_h2h.id, d_h2h.server, d_h2h.verfahren)

        d_verf = Verfahren.objects.get(name=d_h2h.verfahren)

        data_4_t2t = T2T_server2verfahren(server=d_srv, verfahren=d_verf)
        data_4_t2t.save()

# ----------------------------------------------------------------------------


def add_t2t(request):
    # f_add_t2t()
    # f_del_t2t
    return HttpResponse("abc")


# ------------------------------------------------------------------
#
def index(request):
    f_del_t2t
    # f_add_t2t()
    return render(request, 'app_server/index.html')


# ------------------------------------------------------------------
#
def index_01(request):
    f_del_t2t
    # f_add_t2t()
    return render(request, 'app_server/index.html')
