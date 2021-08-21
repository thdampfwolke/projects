# -----------------------------------------------------------
# ../app_core_user/forms.py

from django import forms
from .models import User


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['nname', 'vname']
        labels = {'nname': '', 'vname': ''}		# keine beschriftung

    ## id = int
    #nname = models.CharField(max_length=32, null=False)
    #vname = models.CharField(max_length=32, null=False)
    #geb = models.DateField(null=True, blank=True)
    # email = models.EmailField(
    #    max_length=64, null=True, blank=True, unique=True)
    #is_active = models.BooleanField(null=False, default=True)
    #date_beg = models.DateField(null=False, default='2000-01-01')
    #date_end = models.DateField(null=False, default='2099-12-31')
    #date_created = models.DateTimeField(auto_now_add=True)
    #date_modified = models.DateTimeField(auto_now=True)


# class UserIdForm(forms.ModelForm):
#    class Meta:
#        model = Entry
#        fields = ['text']
#        labels = {'text': ''}       # keine beschriftung
#        widgets = {'text': forms.Textarea(attrs={'cols': 80})}
