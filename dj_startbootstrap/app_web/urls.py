# ../app_web/urls.py

from django.contrib.staticfiles.storage import staticfiles_storage
from django.urls import path
from django.views.generic.base import RedirectView

from . import views


app_name = 'app_web'

urlpatterns = [
    path('tables.html', views.tables, name='tables'),
    path('', views.index, name='index'),
    path("favicon.ico", RedirectView.as_view(
        url=staticfiles_storage.url("favicon.ico"))),
    # path('topics/', views.topics, name='topics'),
    # path('topics/<int:topic_id>/', views.topic, name='topic'),
    # # Seite zum Hinzufügen neuer Fachgebiete
    # path('new_topic/', views.new_topic, name='new_topic'),
    # # Seite zum Hinzufügen neuer Fachgebiete
    # path('new_entry/<int:topic_id>/', views.new_entry, name='new_entry'),
]
