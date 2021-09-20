# ------------------------------------------------------------------
# ../dj_blog/app_blogs/urls.py
# ------------------------------------------------------------------

from django.urls import path
from . import views

app_name = 'app_blogs'

# core:  path('', include('app_blogs.urls')),

urlpatterns = [
    path('', views.index, name='index'), path(
        'index.html', views.index_01, name='index_01'),
    path('index_bs5.html', views.index_bs5, name='index_bs5'),
    # ------------------------------------------------------------------------------
    # blog
    path('blog.html', views.blog, name='blog'),                         # blog: hp
    # ------------------------------------------------------------------------------
    # list
    path('tag_list.html', views.tag_list, name='tag_list'),             # tag_list
    path('topic_list.html', views.topic_list, name='topic_list'),       # topic_list
    path('post/', views.post_list, name='post_list'),                   # post_list
    path('entry/', views.entry_list, name='entry_list'),                # entry_list
    # ------------------------------------------------------------------------------
    # show
    path('tag/<int:tag_id>/', views.tag_show, name='tag_show'),         # tag_show
    path('topic/<int:topic_id>/', views.topic_show, name='topic_show'), # topic_show
    path('post/<int:post_id>/', views.post_show, name='post_show'),     # post_show
    path('entry/<int:entry_id>/', views.entry_show, name='entry_show'), # entry_show
    # ------------------------------------------------------------------------------
    # add
    path('topic_add/', views.topic_add, name='topic_add'),              # topic_add
    path('tag_add/', views.tag_add, name='tag_add'),                    # tag_add
    path('entry_add/', views.entry_add, name='entry_add'),              # entry_add
    path('post_add/', views.post_add, name='post_add'),                 # entry_add
    # ------------------------------------------------------------------------------
    # edit
    path('tag_edit/<int:tag_id>/', views.tag_edit, name='tag_edit'),            # tag_edit
    path('topic_edit/<int:topic_id>/', views.topic_edit, name='topic_edit'),    # topic_edit
    path('entry_edit/<int:entry_id>/', views.entry_edit, name='entry_edit'),    # entry_edit
    path('post_edit/<int:post_id>/', views.post_edit, name='post_edit'),        # post_edit
    # ------------------------------------------------------------------------------
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

# http://127.0.0.1:8000/
# http://127.0.0.1:8000/index.html
# http://127.0.0.1:8000/blog.html
# http://127.0.0.1:8000/tag_list.html
# http://127.0.0.1:8000/topic_list.html
# http://127.0.0.1:8000/
# http://127.0.0.1:8000/
