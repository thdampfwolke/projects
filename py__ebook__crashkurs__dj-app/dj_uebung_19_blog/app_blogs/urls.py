# ../app_blogs/urls.py

from django.urls import path
from app_blogs.views import PublisherListView
# from . import views

app_name = 'app_blogs'

urlpatterns = [
    path('publishers/', PublisherListView.as_view()),
]
