# ../core/urls.py

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('server/', include('app_core_server.urls')),
    path('user/', include('app_core_user.urls')),
    path('', include('app_web.urls')),
    # path('', include('app_web.urls')),
    # path('', include('app_core_server.urls')),
    # path('', include('app_core_user.urls')),
]
