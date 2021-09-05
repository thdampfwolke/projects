# ----------------------------------------------------------------------------
# ../app_learnings_logs/views.py
# ----------------------------------------------------------------------------

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required

from .models import Topic, Entry
from .forms import TopicForm, EntryForm

# ----------------------------------------------------------------------------


def index(request):
    """The home page for Learning Log"""
    # path('', views.index, name='index'),
    return render(request, 'learning_logs/index.html')


@login_required
def topics(request):
    """Show all topics"""
    # path('topics/', views.topics, name='topics'),
    # topics = Topic.objects.order_by('date_added')
    topics = Topic.objects.filter(owner=request.user).order_by('date_added')
    context = {'topics': topics}
    return render(request, 'learning_logs/topics.html', context)


@login_required
def topic(request, topic_id):
    """Show a single topic and all its entries."""
    # path('topics/<int:topic_id>/', views.topic, name='topic'),
    # topic = Topic.objects.get(id=topic_id)
    topic = get_object_or_404(Topic, id=topic_id)
    # Überprüft, ob das Fachgebiet dem aktuellen Benutzer gehört.
    if topic.owner != request.user:
        raise Http404
    entries = topic.entry_set.order_by('-date_added')
    context = {'topic': topic, 'entries': entries}
    return render(request, 'learning_logs/topic.html', context)


@login_required
def new_topic(request):
    """Add a new topic."""
    # path('new_topic/', views.new_topic, name='new_topic'),

    if request.method != 'POST':
        # Keine Daten übermittelt; es wird ein leeres Formular erstellt
        form = TopicForm()
    else:
        # POST-Daten übermittelt; Daten werden verarbeitet
        form = TopicForm(data=request.POST)
        if form.is_valid():
            # form.save()
            new_topic = form.save(commit=False)
            new_topic.owner = request.user
            new_topic.save()
            return redirect('learning_logs:topics')

    # Zeigt ein leeres oder ein als ungültiges erkanntes Formular an.
    context = {'form': form}
    return render(request, 'learning_logs/new_topic.html', context)


@login_required
def new_entry(request, topic_id):
    """Add a new entry for a particular topic (480)"""
    # path('new_entry/<int:topic_id>/', views.new_entry, name='new_entry'),

    topic = Topic.objects.get(id=topic_id)
    if request.method != 'POST':
        # Keine Daten übermittelt; es wird ein leeres Formular erstellt.
        form = EntryForm()
    else:
        # POST-Daten übermittelt; Daten werden verarbeitet.
        form = EntryForm(data=request.POST)
        if form.is_valid():
            if topic.owner == request.user:
                new_entry = form.save(commit=False)
                new_entry.topic = topic
                new_entry.save()
                return redirect('learning_logs:topic', topic_id=topic_id)
            else:
                raise Http404
            
    # Zeigt ein leeres oder ein als ungültiges erkanntes Formular an.
    context = {'topic': topic, 'form': form}
    return render(request, 'learning_logs/new_entry.html', context)


@login_required
def edit_entry(request, entry_id):
    """Edit an existing entry (484)"""
    # path('edit_entry/<int:entry_id>/', views.edit_entry, name='edit_entry'),
    entry = Entry.objects.get(id=entry_id)
    topic = entry.topic
    if topic.owner != request.user:
        raise Http404
    if request.method != 'POST':
        # Ursprüngliche Anforderung; das mit dem jetzigen
        # Eintrag vorab ausgefüllte Formular wird angezeigt
        form = EntryForm(instance=entry)
    else:
        # POST-Daten übermittelt; Daten werden verarbeitet.
        form = EntryForm(instance=entry, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('learning_logs:topic', topic_id=topic.id)

    context = {'entry': entry, 'topic': topic, 'form': form}
    return render(request, 'learning_logs/edit_entry.html', context)


# @login_required
