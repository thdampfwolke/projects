# ------------------------------------------------------------------
# ../dj_blog/app_blogs/urls.py
# ------------------------------------------------------------------

from django.urls import path
from . import views

app_name = 'app_blogs'

urlpatterns = [
    path('', views.index, name='index'),
    path('index.html', views.index_01, name='index_01'),
    #
    path('index_bs5.html', views.index_bs5, name='index_bs5'),
    path('blog.html', views.blog, name='blog'),
    #
    # list: topics (all)
    #path('topics/', views.topics, name='topics'),
    #
    # list: topic (one)
    #path('topics/<int:topic_id>/', views.topic, name='topic'),
    #
    # add: topic (Fachgebiet)
    #path('new_topic/', views.new_topic, name='new_topic'),
    #
    # add: entry (Eintrag)
    #path('new_entry/<int:topic_id>/', views.new_entry, name='new_entry'),
    #
    # edit: entry (Eintrag)
    #path('edit_entry/<int:entry_id>/', views.edit_entry, name='edit_entry'),
]