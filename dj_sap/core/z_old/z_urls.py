# ../..settings../urls.py

from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', include('app_sap.urls')),
    path('admin/', admin.site.urls),
    path('accounts/', include('app_accounts.urls')),
    path('test/', include('app_test.urls')),
]

urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
