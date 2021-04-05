# ../app_staff/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('index.html', views.index, name='index'),
    path('index_01.html', views.index_01, name='index_01'),
    path('index_02.html', views.index_02, name='index_02')
]

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
