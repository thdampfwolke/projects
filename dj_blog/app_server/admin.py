# ------------------------------------------------------------------
# ../dj_blog/app_server/admin.py
# ------------------------------------------------------------------

from django.contrib import admin

from .models import Server, Verfahren
from .models import H2H_server2verfahren, T2T_server2verfahren

admin.site.register(Server)
admin.site.register(Verfahren)
admin.site.register(H2H_server2verfahren)
admin.site.register(T2T_server2verfahren)


# # ------------------------------------------------------------------
# @admin.register(Post)
# class PostAdmin(admin.ModelAdmin):
#     list_display = ['id', 'title', 'text', 'topic', 'is_checked',
#                     'is_active', 'date_beg', 'date_end', 'date_created', 'date_modified']
#     # list_filter = ['in_stock', 'is_active']
#     # list_editable = ['price', 'in_stock']
#     # prepopulated_fields = {'slug': ('title',)}
#
# # 'id', 'title', 'text', 'topic', 'tag', 'id_checked', 'is_active', 'date_beg', 'date_end', 'date_created', 'date_modified'
