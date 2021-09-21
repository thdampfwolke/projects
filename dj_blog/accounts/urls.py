# ------------------------------------------------------------------
# ../dj_blog/accounts/urls.py
# ------------------------------------------------------------------

from django.urls import path
from . import views

app_name = 'accounts'

# path('accounts/', include('accounts.urls')),

urlpatterns = [
    path('', views.index, name='index'), path(
        'index.html', views.index_01, name='index_01'),
    path('index_bs5.html', views.index_bs5, name='index_bs5'),
    # ------------------------------------------------------------------------------
    
    # ------------------------------------------------------------------------------
    # app_blog:
    # path('blog.html', views.blog, name='blog'),
    # path('tag_list.html', views.tag_list, name='tag_list'),
    # path('tag/<int:tag_id>/', views.tag_show, name='tag_show'),
    # path('tag_add/', views.tag_add, name='tag_add'),
    # path('tag_edit/<int:tag_id>/', views.tag_edit, name='tag_edit'),
    # ------------------------------------------------------------------------------
]

# http://127.0.0.1:8000/accounts
# http://127.0.0.1:8000/index.html
# http://127.0.0.1:8000/blog.html
# http://127.0.0.1:8000/tag_list.html
# http://127.0.0.1:8000/topic_list.html
# http://127.0.0.1:8000/
# http://127.0.0.1:8000/
