# ------------------------------------------------------------------
# ../dj_blog/core/urls.py
# ------------------------------------------------------------------

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('accounts/', include('accounts.urls')),
    path('', include('app_blogs.urls')),
    path('server/', include('app_server.urls'))
]
