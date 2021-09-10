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


def index(request):
    return render(request, 'app_server/index.html')


def index_01(request):
    return render(request, 'app_server/index.html')

# ============================================================================
# tab loeschen; ueber tab_h2h -> tab_t2t fuellen; srv_id und verf_id ermitteln und in tab_t2t schreiben
# ============================================================================

# ------------------------------------------------------------------
#


def f_t2t_old2new():

    # tab vollstaendig loeschen
    t2t_verf2srv.objects.all().delete()

    data_server = srv.objects.all()

    for d in data_server:
        # print(d.id, d.name)
        data_h2h = h2h_verf2srv.objects.get(srv=d.name)          # id srv

        # print(data_h2h.id, data_h2h.srv, data_h2h.verfahren)
        d_verf = verf.objects.get(name=data_h2h.verf)            # id verfahren
        data_4_t2t = t2t_verf2srv(verf=d_verf, srv=d)

        data_4_t2t.save()

# ----------------------------------------------------------------------------


def add_t2t(request):
    f_t2t_old2new()
    return HttpResponse("abc")
