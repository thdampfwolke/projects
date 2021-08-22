# ../app_users/urls.py

from django.urls import path, include

from . import views

app_name = 'app_users'

urlpatterns = [
    # Schließt Standard-Authentifizierungs-URLs ein.
    path('', include('django.contrib.auth.urls')),
    #
    # Registrierungsseite.
    path('register/', views.register, name='register'),
]

# !!!
# mkdir ../templates/registration
# ../templates/registration/login.html
# ../templates/registration/logou.html
# . . .
