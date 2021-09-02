# ----------------------------------------------------------------------------
# ../app_learnings_logs/urls.py
# ----------------------------------------------------------------------------

from django.urls import path
from . import views

app_name = 'learning_logs'

urlpatterns = [
    path('', views.index, name='index'),
    #
    # list: topics (all)
    path('topics/', views.topics, name='topics'),
    #
    # list: topic (one)
    path('topics/<int:topic_id>/', views.topic, name='topic'),
    #
    # add: topic (Fachgebiet)
    path('new_topic/', views.new_topic, name='new_topic'),
    #
    # add: entry (Eintrag)
    path('new_entry/<int:topic_id>/', views.new_entry, name='new_entry'),
    #
    # edit: entry (Eintrag)
    path('edit_entry/<int:entry_id>/', views.edit_entry, name='edit_entry'),
]
