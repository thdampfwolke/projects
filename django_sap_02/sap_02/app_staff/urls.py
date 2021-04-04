# ../app_staff/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index')
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
