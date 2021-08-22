# ../app_learnings_logs/urls.py

from django.urls import path
from . import views

app_name = 'learning_logs'

urlpatterns = [
    path('', views.index, name='index'),
    path('topics/', views.topics, name='topics'),
    path('topics/<int:topic_id>/', views.topic, name='topic'),
    #
    # Seite zum Hinzufügen neuer Fachgebiete
    path('new_topic/', views.new_topic, name='new_topic'),
    #
    # Seite zum Hinzufügen neuer Fachgebiete
    path('new_entry/<int:topic_id>/', views.new_entry, name='new_entry'),
    #
    # Seite zum Bearbeiten eines Eintrags
    path('edit_entry/<int:entry_id>/', views.edit_entry, name='edit_entry'),
]


"""
urlpatterns:
1. Argument von path:   ''      ->      http://127.0.0.1:8000/
2. Argument von path:   gibt an, welche Funktion in views.py
aufgerufen werden soll -> index() in views.py
3. Argument von path:   gibt diesem URL-Muster den Namen index, sodass wir in anderen Codeabschnitten darauf verweisen können
"""
