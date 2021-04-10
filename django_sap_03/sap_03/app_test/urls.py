# ../app_test/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.test_01, name='test_01'),
    path('test_01.html', views.test_01, name='test_01'),
]

    #path('', views.fun_index, name='fun_index'),
    #path('index.html', views.fun_index, name='fun_index'),
    #path('index_01_dyn.html', views.fun_index_01, name='fun_index_01'),
    #path('index_02_db.html', views.fun_index_02, name='fun_index_02'),
    #path('index_03.html', views.index_03, name='index_03'),
    #path('index_04.html', views.index_04, name='index_04')

# urlpatterns = [
#     path('', views.home, name='home'),
#     path('add', views.add, name='add')
# ]

# ../telusko/urls.py
# from django.contrib import admin
# from django.urls import path, include
# 
# urlpatterns = [
#     # path('', include('calc.urls')),
#     path('', include('travello.urls')),
#     path('admin/', admin.site.urls),
# ]