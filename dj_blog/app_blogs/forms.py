# ------------------------------------------------------------------
# ../dj_blog/app_blogs/forms.py
# ------------------------------------------------------------------

from django import forms
from .models import Tag, Topic


# class TagForm(forms.ModelForm):
#     class Meta:
#         model = Tag
#         fields = ['text']
#         labels = {'text': ''}


class TopicForm(forms.ModelForm):
    class Meta:
        model = Topic
        fields = ['topic']
        labels = {'topic': ''}



# {{ form.as_table }}   will render them as table cells wrapped in <tr> tags
# {{ form.as_p }}       will render them wrapped in <p> tags
# {{ form.as_ul }}      will render them wrapped in <li> tags
