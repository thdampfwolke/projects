# ----------------------------------------------------------------------------
# ../users/urls.py
# ----------------------------------------------------------------------------

from django.urls import path, include

from . import views

app_name = 'users'

urlpatterns = [
    # Django: Standard-Authentifizierungs-URLs
    path('', include('django.contrib.auth.urls')),
    #
    # Registrierungsseite
    path('register/', views.register, name='register'),
]



# http://127.0.0.1:8000/users/login/
# http://localhost:8000/users/register/
