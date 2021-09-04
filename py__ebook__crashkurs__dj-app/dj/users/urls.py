# ----------------------------------------------------------------------------
# ../users/urls.py
# ----------------------------------------------------------------------------

from django.urls import path, include

# from . import views

app_name = 'users'

urlpatterns = [
    # Schließt Standard-Authentifizierungs-URLs ein
    path('', include('django.contrib.auth.urls')),
]



# http://127.0.0.1:8000/users/login/
