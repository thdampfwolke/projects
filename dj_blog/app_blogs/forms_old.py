# ------------------------------------------------------------------
# ../dj_blog/app_blogs/forms.py
# ------------------------------------------------------------------

from django import forms
# from django.forms import ModelForm, Textarea
# django.forms.ModelChoiceField             ChoiceField
# django.forms.ModelMultipleChoiceField     MultipleChoiceField
from .models import Entry, Tag, Topic, Post


# ==================================================================
# Topic:    id, topic, is_checked, is_active, date_beg, date_end, date_created, date_modified
# Tag:      id, tag, is_checked, is_active, date_beg, date_end, date_created, date_modified
# Post:     id, title, text, fk: topic, mm: tag, is_checked, is_active, date_beg, date_end, date_created, date_modified
# Entry:    id, fk:post, text, is_checked, is_active, date_beg, date_end, date_created, date_modified
# ==================================================================


# ==================================================================
# class XXXForm(forms.ModelForm):
#     class Meta:
#         model = XXX
#         # fields = '__all__'
#         # fields = ['name', 'text', 'is_checked', 'is_active', 'date_beg', 'date_end']
#         fields = ['name', 'text']
#         lables = {'name': 'Name', 'text': 'Text'}
#         widgets = {'text': forms.Textarea(attrs={'cols': 80, 'rows': 5})}

# -----------------------------------------------
# Post: id, title, text, fk: topic, mm: tag, is_checked, is_active, date_beg, date_end, date_created, date_modified

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = '__all__'

# -----------------------------------------------
# Entry:    id, fk:post, text, is_checked, is_active, date_beg, date_end, date_created, date_modified


class EntryForm(forms.ModelForm):
    class Meta:
        model = Entry
        fields = '__all__'

# -----------------------------------------------
# Tag:  id, tag, is_checked, is_active, date_beg, date_end, date_created, date_modified


class TagForm(forms.ModelForm):
    class Meta:
        model = Tag
<<<<<<< HEAD
        fields = ['tag']
        labels = {'tag': 'tag'}
=======
        fields = '__all__'
>>>>>>> f8ce636595e6364082bda2ac0266d6ea11a21148

# -----------------------------------------------
# Topic:    id, topic, is_checked, is_active, date_beg, date_end, date_created, date_modified


class TopicForm(forms.ModelForm):
    class Meta:
        model = Topic
        fields = '__all__'


# ----------------------------------------------------------------------------
# {{ form.as_table }}   will render them as table cells wrapped in <tr> tags
# {{ form.as_p }}       will render them wrapped in <p> tags
# {{ form.as_ul }}      will render them wrapped in <li> tags
