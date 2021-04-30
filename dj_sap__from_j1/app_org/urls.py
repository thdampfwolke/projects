# ../app_org/urls.py


from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('index.html', views.index, name='index'),
    # path('test_01_dyn.html', views.test_01_dyn, name='test_01_dyn'),
    # path('test_02_dyn_db.html', views.test_02_dyn_db, name='test_02_dyn_db'),
    # path('abc', include('app_xxx.urls')),
]