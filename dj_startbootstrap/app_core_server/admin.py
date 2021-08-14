# ../app_core_server/admin.py

from django.contrib import admin

from django_admin_listfilter_dropdown.filters import (
    DropdownFilter, ChoiceDropdownFilter, RelatedDropdownFilter
)

from .models import Server, Ip, Z_server2ip

# ----------------------------------------------------------------------------
# admin.site.register(Server)
# admin.site.register(Ip)
# admin.site.register(Z_server2ip)
# ----------------------------------------------------------------------------


# ----------------------------------------------------------------------------
@admin.register(Server)
class ServerAdmin(admin.ModelAdmin):
    list_display = ['id', 'server', 'is_active', 'date_beg',
                    'date_end', 'date_created', 'date_modified']
    list_filter = ['server']


# ----------------------------------------------------------------------------
@admin.register(Ip)
class IpAdmin(admin.ModelAdmin):
    list_display = ['id', 'ip', 'is_active', 'date_beg',
                    'date_end', 'date_created', 'date_modified']
    list_filter = ['ip']

# ----------------------------------------------------------------------------


@admin.register(Z_server2ip)
class Z_server2ipAdmin(admin.ModelAdmin):
    list_display = ['id', 't2t_server', 't2t_ip', 'is_active',
                    'date_beg', 'date_end', 'date_created', 'date_modified']
    list_filter = ['t2t_server', 't2t_ip']
    # list_filter = (
    #     ('t2t_user', RelatedDropdownFilter),
    #     ('t2t_userid', RelatedDropdownFilter),
    # )
