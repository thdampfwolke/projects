# ------------------------------------------------------------------
# ../dj_blog/app_server/urls.py
# ------------------------------------------------------------------

from django.urls import path
from . import views

app_name = 'app_server'

urlpatterns = [
    path('', views.index, name='index'),
    path('index.html', views.index_01, name='index_01'),
    # path('t2t/', views.add_t2t, name='add_t2t'),
    #path('index_bs5.html', views.index_bs5, name='index_bs5'),
    #path('blog.html', views.blog, name='blog'),
    #path('tag_list.html', views.tag_list, name='tag_list'),
    #path('topic_list.html', views.topic_list, name='topic_list'),
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
