# ../app_blogs/views.py

from django.views.generic import ListView
from app_blogs.models import Publisher
# from .models import Publisher


class PublisherListView(ListView):
    model = Publisher
    context_object_name = 'my_favorite_publishers'
