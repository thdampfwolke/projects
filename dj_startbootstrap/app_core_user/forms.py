# -----------------------------------------------------------
# ../app_core_user/forms.py

from django import forms
from .models import User, UserId


class UserForm(forms.ModelForm):
    class Meta:
        model = User

        fields = ['nname', 'vname', 'geb', 'email',
                  'is_active', 'date_beg', 'date_end']

        labels = {
            'nname': 'nname',
            'vname': 'vname',
            'geb': 'geb (yyyy-mm-dd)',
            'email': 'email',
            'is_active': 'is_active',
            'date_beg': 'date_beg (yyyy-mm-dd)',
            'date_end': 'date_end (yyyy-mm-dd)'
        }


class UserIdForm(forms.ModelForm):
    class Meta:
        model = UserId

        fields = ['uid', 'is_active', 'date_beg', 'date_end']

        labels = {
            'uid': 'uid',
            'is_active': 'is_active',
            'date_beg': 'date_beg (yyyy-mm-dd)',
            'date_end': 'date_end (yyyy-mm-dd)'
        }

# class UserIdForm(forms.ModelForm):
#    class Meta:
#        model = Entry
#        fields = ['text']
#        labels = {'text': ''}       # keine beschriftung
#        widgets = {'text': forms.Textarea(attrs={'cols': 80})}
