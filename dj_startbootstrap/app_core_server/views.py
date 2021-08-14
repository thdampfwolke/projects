# ../app_core_server/views.py

from django.shortcuts import render, redirect

# from .models import User
# from .forms import TopicForm, EntryForm


def index(request):
    """hp: index.html"""
    return render(request, 'app_core_server/index.html')
