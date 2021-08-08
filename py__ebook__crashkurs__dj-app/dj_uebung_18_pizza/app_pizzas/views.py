# ../app_pizzas/views.py

from django.shortcuts import render
from .models import Pizza


def index(request):
    """The home page for pizzeria"""
    return render(request, 'app_pizzas/index.html')


# from django.shortcuts import render, redirect
# from .forms import TopicForm, EntryForm

# def topics(request):
#     """Show all topics."""
#     topics = Topic.objects.order_by('date_added')
#     context = {'topics': topics}
#     return render(request, 'learning_logs/topics.html', context)
#
#
# def topic(request, topic_id):
#     """Show a single topic and all its entries."""
#     topic = Topic.objects.get(id=topic_id)
#     entries = topic.entry_set.order_by('-date_added')
#     context = {'topic': topic, 'entries': entries}
#     return render(request, 'learning_logs/topic.html', context)
