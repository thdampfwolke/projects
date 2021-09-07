# ------------------------------------------------------------------
# ../dj_blog/app_blogs/admin.py
# ------------------------------------------------------------------

from django.contrib import admin

from .models import Entry, Post, Tag, Topic

admin.site.register(Entry)
# admin.site.register(Post)
admin.site.register(Tag)
admin.site.register(Topic)


# ------------------------------------------------------------------
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'text', 'topic', 'is_checked',
                    'is_active', 'date_beg', 'date_end', 'date_created', 'date_modified']
    # list_filter = ['in_stock', 'is_active']
    # list_editable = ['price', 'in_stock']
    # prepopulated_fields = {'slug': ('title',)}

# 'id', 'title', 'text', 'topic', 'tag', 'id_checked', 'is_active', 'date_beg', 'date_end', 'date_created', 'date_modified'
