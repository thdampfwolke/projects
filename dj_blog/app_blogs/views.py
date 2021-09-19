# ------------------------------------------------------------------
# ../dj_blog/app_blogs/views.py
# ------------------------------------------------------------------

from django.shortcuts import render, redirect
from .forms import EntryForm, TagForm, TopicForm, PostForm

# from django.shortcuts import render, redirect, get_object_or_404
# from django.contrib.auth.decorators import login_required

from .models import Tag, Topic, Post, Entry


# ============================================================================
#

def index(request):
    """HP: app_blogs"""
    # path('', views.index, name='index'),
    return render(request, 'app_blogs/index.html')


def index_01(request):
    """HP: app_blogs"""
    # path('index.html', views.index_01, name='index_01'),
    return render(request, 'app_blogs/index.html')


def index_bs5(request):
    """HP: app_blogs"""
    # path('index_bs5.html', views.index_bs5, name='index_bs5'),
    return render(request, 'app_blogs/index_bs5.html')


# ============================================================================
# blog:

# -----------------------------------------------
def blog(request):
    """HP: app_blogs"""
    # path('blog.html', views.blog, name='blog'),
    return render(request, 'app_blogs/blog.html')


# ============================================================================
# list:

# -----------------------------------------------
def tag_list(request):
    """Show all tags"""
    # path('tag_list.html', views.tag_list, name='tag_list'),
    data = Tag.objects.order_by('tag')
    # data = Tag.objects.order_by('date_modified')
    # data = Tag.objects.filter(owner=request.user).order_by('date_modified')
    context = {'data': data}
    return render(request, 'app_blogs/tag_list.html', context)

# -----------------------------------------------
def topic_list(request):
    """Show all topics"""
    # path('topic_list.html', views.topic_list, name='topic_list'),
    data = Topic.objects.order_by('id')
    context = {'data': data}
    return render(request, 'app_blogs/topic_list.html', context)

# -----------------------------------------------
def post_list(request):
    """Show all posts"""
    # path('post/', views.post_list, name='post_list'),
    data = Post.objects.order_by('-date_modified')
    context = {'data': data}
    return render(request, 'app_blogs/post_list.html', context)


# ============================================================================
# show:

# -----------------------------------------------
def tag_show(request, tag_id):
    """Show a single entry"""
    # path('tag/<int:tag_id>/', views.tag_show, name='tag_show')
    data = Tag.objects.get(id=tag_id)
    context = {'data': data}
    return render(request, 'app_blogs/tag_show.html', context)

# -----------------------------------------------
def topic_show(request, topic_id):
    """Show a single entry"""
    # path('topic/<int:topic_id>/', views.topic_show, name='topic_show')
    data = Topic.objects.get(id=topic_id)
    context = {'data': data}
    return render(request, 'app_blogs/topic_show.html', context)

# -----------------------------------------------
def entry_show(request, entry_id):
    """Show a single entry"""
    # path('entry/<int:entry_id>/', views.entry_show, name='entry_show')
    data = Entry.objects.get(id=entry_id)
    context = {'data': data}
    return render(request, 'app_blogs/entry_show.html', context)

# -----------------------------------------------
def post_show(request, post_id):
    """Show a single post"""
    # path('post/<int:post_id>/', views.post_show, name='post_show'),
    data = Post.objects.get(id=post_id)
    entries = data.entry_set.order_by('-date_modified')
    context = {'data': data, 'entries': entries}
    return render(request, 'app_blogs/post_show.html', context)


# ============================================================================
# add:

# -----------------------------------------------
def post_add(request):
    """Add a new post"""
    #path('post_add/', views.post_add, name='post_add'),
    if request.method != 'POST':
        # keine daten; erstelle ein neues leeres formular
        form = PostForm()
    else:
        # POST-Daten uebermittelt; Daten werden verarbeitet
        form = PostForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('app_blogs:post_list')

    # zeigt ein leeres oder ein als ungueltiges erkanntes Formular an
    context = {'form': form}
    return render(request, 'app_blogs/post_add.html', context)


# -----------------------------------------------
def entry_add(request):
    """Add a new entry"""
    # path('entry_add/', views.entry_add, name='entry_add'),
    if request.method != 'POST':
        # keine daten; erstelle ein neues leeres formular
        form = EntryForm()
    else:
        # POST-Daten uebermittelt; Daten werden verarbeitet
        form = EntryForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('app_blogs:post_list')

    # zeigt ein leeres oder ein als ungueltiges erkanntes Formular an
    context = {'form': form}
    return render(request, 'app_blogs/entry_add.html', context)

# -----------------------------------------------
def tag_add(request):
    """Add a new tag"""
    # path('tag_add/', views.tag_add, name='tag_add'),
    if request.method != 'POST':
        # keine daten; erstelle ein neues leeres formular
        form = TagForm()
    else:
        # POST-Daten uebermittelt; Daten werden verarbeitet
        form = TagForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('app_blogs:tag_list')

    # zeigt ein leeres oder ein als ungueltiges erkanntes Formular an
    context = {'form': form}
    return render(request, 'app_blogs/tag_add.html', context)

# -----------------------------------------------
def topic_add(request):
    """Add a new topic"""
    # path('topic_add/', views.topic_add, name='topic_add'),
    if request.method != 'POST':
        # keine daten; erstelle ein neues leeres formular
        form = TopicForm()
    else:
        # POST-Daten uebermittelt; Daten werden verarbeitet
        form = TopicForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('app_blogs:topic_list')

    # zeigt ein leeres oder ein als ungueltiges erkanntes Formular an
    context = {'form': form}
    return render(request, 'app_blogs/topic_add.html', context)


# ============================================================================
# edit:

# -----------------------------------------------
def tag_edit(request, tag_id):
    """edit a tag"""
    # path('tag_edit/<int:tag_id>/', views.tag_edit, name='tag_edit'),

    tag = Tag.objects.get(id=tag_id)

    if request.method != 'POST':
        # Ursprüngliche Anforderung; das mit dem jetzigen
        # Eintrag vorab ausgefuellte Formular wird angezeigt
        form = TagForm(instance=tag)
    else:
        # POST-Daten uebermittelt; Daten werden verarbeitet
        form = TagForm(instance=tag, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('app_blogs:tag_list')
            # return redirect('app_blogs:tag_show', tag_id=tag.id)
            
    context = {'tag': tag, 'form': form}
    return render(request, 'app_blogs/tag_edit.html', context)

# -----------------------------------------------
def topic_edit(request, topic_id):
    """edit a topic"""
    # path('topic_edit/<int:topic_id>/', views.topic_edit, name='topic_edit'),

    topic = Topic.objects.get(id=topic_id)

    if request.method != 'POST':
        # Ursprüngliche Anforderung; das mit dem jetzigen
        # Eintrag vorab ausgefuellte Formular wird angezeigt
        form = TopicForm(instance=topic)
    else:
        # POST-Daten uebermittelt; Daten werden verarbeitet
        form = TopicForm(instance=topic, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('app_blogs:topic_list')
            # return redirect('app_blogs:topic_show', topic_id=topic.id)
            
    context = {'topic': topic, 'form': form}
    return render(request, 'app_blogs/topic_edit.html', context)






# ============================================================================
# 


# ==================================================================
#   path('blog.html', views.blog, name='blog'),                         # blog: hp
#   path('tag_list.html', views.tag_list, name='tag_list'),             # tag_list
#   path('topic_list.html', views.topic_list, name='topic_list'),       # topic_list
#   path('post/', views.post_list, name='post_list'),                   # post_list
#   path('post/<int:post_id>/', views.post_show, name='post_show'),     # post_show
#   path('post/<int:entry_id>/', views.entry_show, name='entry_show')   # entry_show
#   path('topic_add/', views.topic_add, name='topic_add'),
#   path('tag_add/', views.tag_add, name='tag_add'),                    # tag_add
#   path('entry_add/', views.entry_add, name='entry_add'),              # entry_add
# ==================================================================
# old:
# ==================================================================

# @login_required
# def topics(request):
#     """Show all topics"""
#     # path('topics/', views.topics, name='topics'),
#     # topics = Topic.objects.order_by('date_added')
#     topics = Topic.objects.filter(owner=request.user).order_by('date_added')
#     context = {'topics': topics}
#     return render(request, 'learning_logs/topics.html', context)
#
#
# @login_required
# def topic(request, topic_id):
#     """Show a single topic and all its entries."""
#     # path('topics/<int:topic_id>/', views.topic, name='topic'),
#     # topic = Topic.objects.get(id=topic_id)
#     topic = get_object_or_404(Topic, id=topic_id)
#     # Überprüft, ob das Fachgebiet dem aktuellen Benutzer gehört.
#     if topic.owner != request.user:
#         raise Http404
#     entries = topic.entry_set.order_by('-date_added')
#     context = {'topic': topic, 'entries': entries}
#     return render(request, 'learning_logs/topic.html', context)
#
#
# @login_required
# def new_topic(request):
#     """Add a new topic."""
#     # path('new_topic/', views.new_topic, name='new_topic'),
#
#     if request.method != 'POST':
#         # Keine Daten übermittelt; es wird ein leeres Formular erstellt
#         form = TopicForm()
#     else:
#         # POST-Daten übermittelt; Daten werden verarbeitet
#         form = TopicForm(data=request.POST)
#         if form.is_valid():
#             # form.save()
#             new_topic = form.save(commit=False)
#             new_topic.owner = request.user
#             new_topic.save()
#             return redirect('learning_logs:topics')
#
#     # Zeigt ein leeres oder ein als ungültiges erkanntes Formular an.
#     context = {'form': form}
#     return render(request, 'learning_logs/new_topic.html', context)
#
#
# @login_required
# def new_entry(request, topic_id):
#     """Add a new entry for a particular topic (480)"""
#     # path('new_entry/<int:topic_id>/', views.new_entry, name='new_entry'),
#
#     topic = Topic.objects.get(id=topic_id)
#     if request.method != 'POST':
#         # Keine Daten übermittelt; es wird ein leeres Formular erstellt.
#         form = EntryForm()
#     else:
#         # POST-Daten übermittelt; Daten werden verarbeitet.
#         form = EntryForm(data=request.POST)
#         if form.is_valid():
#             if topic.owner == request.user:
#                 new_entry = form.save(commit=False)
#                 new_entry.topic = topic
#                 new_entry.save()
#                 return redirect('learning_logs:topic', topic_id=topic_id)
#             else:
#                 raise Http404
#
#     # Zeigt ein leeres oder ein als ungültiges erkanntes Formular an.
#     context = {'topic': topic, 'form': form}
#     return render(request, 'learning_logs/new_entry.html', context)
#
#
# @login_required
# def edit_entry(request, entry_id):
#     """Edit an existing entry (484)"""
#     # path('edit_entry/<int:entry_id>/', views.edit_entry, name='edit_entry'),
#     entry = Entry.objects.get(id=entry_id)
#     topic = entry.topic
#     if topic.owner != request.user:
#         raise Http404
#     if request.method != 'POST':
#         # Ursprüngliche Anforderung; das mit dem jetzigen
#         # Eintrag vorab ausgefüllte Formular wird angezeigt
#         form = EntryForm(instance=entry)
#     else:
#         # POST-Daten übermittelt; Daten werden verarbeitet.
#         form = EntryForm(instance=entry, data=request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('learning_logs:topic', topic_id=topic.id)
#
#     context = {'entry': entry, 'topic': topic, 'form': form}
#     return render(request, 'learning_logs/edit_entry.html', context)
