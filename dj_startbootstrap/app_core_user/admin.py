# ../app_core_user/admin.py

from django.contrib import admin

from django_admin_listfilter_dropdown.filters import (
    DropdownFilter, ChoiceDropdownFilter, RelatedDropdownFilter
)

from .models import User, UserId, Z_user2userid

# ----------------------------------------------------------------------------
# admin.site.register(UserId)
# admin.site.register(User)
# admin.site.register(Z_user2userid)
# ----------------------------------------------------------------------------


# ----------------------------------------------------------------------------
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['id', 'nname', 'vname', 'geb', 'email', 'is_active',
                    'date_beg', 'date_end', 'date_created', 'date_modified']
    list_filter = ['nname', 'vname']


# ----------------------------------------------------------------------------
@admin.register(UserId)
class UserIdAdmin(admin.ModelAdmin):
    list_display = ['id', 'uid', 'is_active', 'date_beg',
                    'date_end', 'date_created', 'date_modified']
    list_filter = ['uid']

# ----------------------------------------------------------------------------


@admin.register(Z_user2userid)
class Z_user2useridAdmin(admin.ModelAdmin):
    list_display = ['id', 't2t_user', 't2t_userid', 'is_active',
                    'date_beg', 'date_end', 'date_created', 'date_modified']
    list_filter = ['t2t_user', 't2t_userid']
    # list_filter = (
    #     ('t2t_user', RelatedDropdownFilter),
    #     ('t2t_userid', RelatedDropdownFilter),
    # )
