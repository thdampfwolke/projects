# -----------------------------------------------------------
# ../app_core_user/forms.py

from django import forms
from .models import User, UserId, Z_user2userid


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


class Z_user2useridForm(forms.ModelForm):
    class Meta:
        model = Z_user2userid

        fields = ['is_active', 'date_beg', 'date_end' ]

        labels = {
            'is_active': 'is_active',
            'date_beg': 'date_beg (yyyy-mm-dd)',
            'date_end': 'date_end (yyyy-mm-dd)'
        }
# https://stackoverflow.com/questions/5708650/how-do-i-add-a-foreign-key-field-to-a-modelform-in-django
# https://stackoverflow.com/questions/65218232/django-form-calling-foreign-key-field-attributes-in-template
# https://docs.djangoproject.com/en/3.2/topics/forms/modelforms/
# https://qastack.com.de/programming/291945/how-do-i-filter-foreignkey-choices-in-a-django-modelform

#'id',
# 't2t_user.id', 't2t_user.nname', 't2t_user.vname', 't2t_user.geb', 't2t_user.email',
# 't2t_user.is_active', 't2t_user.date_beg', 't2t_user.date_end',
   
       
# id,
# t2t_user.id, t2t_user.nname, t2t_user.vname, t2t_user.geb, t2t_user.email,
# t2t_user.is_active, t2t_user.date_beg, t2t_user.date_end
#
# t2t_userid.id, t2t_userid.uid, t2t_userid.is_active, t2t_userid.date_beg, t2t_userid.date_end
# is_active, date_beg, date_end


# tipps: widgets = {'text': forms.Textarea(attrs={'cols': 80})}
