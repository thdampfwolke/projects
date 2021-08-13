# ../app_web/urls.py

from django.urls import path
from . import views

app_name = 'app_web'

urlpatterns = [
    path('', views.index, name='index'),
    # path('topics/', views.topics, name='topics'),
    # path('topics/<int:topic_id>/', views.topic, name='topic'),
    # # Seite zum Hinzufügen neuer Fachgebiete
    # path('new_topic/', views.new_topic, name='new_topic'),
    # # Seite zum Hinzufügen neuer Fachgebiete
    # path('new_entry/<int:topic_id>/', views.new_entry, name='new_entry'),
]
