# ../app_core_user/views.py

from django.shortcuts import render, redirect

from .models import User, UserId, Z_user2userid
# from .forms import TopicForm, EntryForm


def index(request):
    """hp: index.html  -  stat."""
    return render(request, 'app_core_user/index.html')


def index_02(request):
    """hp: index_02.html  - stat. + base.html"""
    return render(request, 'app_core_user/index_02.html')


def index_03_user(request):
    """hp: index_03_user.html  -  abfrage: alle user"""
    users = User.objects.all()
    context = {'users': users}
    return render(request, 'app_core_user/index_03_user.html', context)


def index_04_userid(request):
    """hp: index_04_userid.html  -  abfrage: alle userids"""
    userids = UserId.objects.order_by('uid')
    context = {'userids': userids}
    return render(request, 'app_core_user/index_04_userid.html', context)


def index_05_user2userid(request):
    """hp: index_05_user2userid.html  -  abfrage: """
    users = Z_user2userid.objects.order_by('id')
    context = {'users': users}
    return render(request, 'app_core_user/index_05_user2userid.html', context)


def index_06_user(request, user_id):
    """hp: index_06/<int:user_id>  -  abfrage: einzelne user durch die user_id"""
    userid = User.objects.get(id=user_id)
    userids = userid.z_user2userid_set.all()
    #userids = userid.z_user2userid_set.order_by('-date_added')
    context = {'userid': userid, 'userids': userids}
    return render(request, 'app_core_user/index_06_user.html', context)

