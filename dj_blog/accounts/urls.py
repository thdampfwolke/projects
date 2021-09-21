# ------------------------------------------------------------------
# ../dj_blog/accounts/urls.py
# ------------------------------------------------------------------

from django.urls import path, include
# from . import views

app_name = 'accounts'

# path('accounts/', include('accounts.urls')),

urlpatterns = [
    # ------------------------------------------------------------------------------
    path('', include('django.contrib.auth.urls')), 
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

# ----------------------------------------------------------------------------
# https://docs.djangoproject.com/en/3.2/topics/auth/default/#user-objects
# django.contrib.auth.urls
# 
# urlpatterns = [   path('accounts/', include('django.contrib.auth.urls'))  ]
# 
# This will include the following URL patterns:
# accounts/login/ [name='login']
# accounts/logout/ [name='logout']
# accounts/password_change/ [name='password_change']
# accounts/password_change/done/ [name='password_change_done']
# accounts/password_reset/ [name='password_reset']
# accounts/password_reset/done/ [name='password_reset_done']
# accounts/reset/<uidb64>/<token>/ [name='password_reset_confirm']
# accounts/reset/done/ [name='password_reset_complete']
