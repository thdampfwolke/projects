# ../app_core_user/views.py

from django.shortcuts import render, redirect

from .models import User, UserId
# from .forms import TopicForm, EntryForm


def index(request):
    """hp: index.html"""
    return render(request, 'app_core_user/index.html')
