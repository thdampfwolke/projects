# ../app_core_user/urls.py

from django.contrib.staticfiles.storage import staticfiles_storage
from django.urls import path
from django.views.generic.base import RedirectView

from . import views

app_name = 'app_core_user'

urlpatterns = [
    # path('', views.index, name='index'),
    path('index.html', views.index, name='index'),
    path('index_02.html', views.index_02, name='index_02'),
    path('index_03_user.html', views.index_03_user, name='index_03_user'),
    path('index_04_userid.html', views.index_04_userid, name='index_04_userid'),
    path('index_05_user2userid.html', views.index_05_user2userid,
         name='index_05_user2userid'),
    path('index_06/<int:user_id>/', views.index_06_user, name='index_06_user'),
    #
    path("favicon.ico", RedirectView.as_view(
        url=staticfiles_storage.url("favicon.ico"))),
    # path('topics/', views.topics, name='topics'),
    # path('topics/<int:topic_id>/', views.topic, name='topic'),
    # # Seite zum Hinzufügen neuer Fachgebiete
    # path('new_topic/', views.new_topic, name='new_topic'),
    # # Seite zum Hinzufügen neuer Fachgebiete
    # path('new_entry/<int:topic_id>/', views.new_entry, name='new_entry'),
]
