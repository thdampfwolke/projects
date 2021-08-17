# ../app_core_user/views.py

from django.shortcuts import render, redirect

from .models import User, UserId
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


# def index_05_userid(request, userid_id):
#    """hp: index_05/<int:user_id>  -  abfrage: alle userids"""
#    userid = UserId.objects.get(id=userid_id)
#    entries = userid.uid_set.order_by('-date_added')
#    context = {'userids': userids}
#    return render(request, 'app_core_user/index_04_userid.html', context)


#def index_05_user2userid(request, user_id):
#    """hp: ...  -  abfrage: """
#    user = User.objects.get(id=user_id)
#    userids = user.uid_set.order_by('-date_added')
##    context = {'userids': userids}
##    return render(request, 'app_core_user/index_04_userid.html', context)

# path('index_05/<int:user_id>/', views.index_05_userid, name='index_05_userid'),
