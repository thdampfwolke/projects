# ../core/urls.py

from django.contrib import admin
from django.urls import path, include
# from django.conf import settings
# from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/', include('app_users.urls')),
    path('server/', include('app_core_server.urls')),
    path('user/', include('app_core_user.urls')),
    path('', include('app_web.urls')),
    # path('', include('app_web.urls')),
    # path('', include('app_core_server.urls')),
    # path('', include('app_core_user.urls')),
]
