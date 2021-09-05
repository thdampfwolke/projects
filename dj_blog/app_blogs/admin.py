# ------------------------------------------------------------------
# ../dj_blog/app_blogs/admin.py
# ------------------------------------------------------------------

from django.contrib import admin

from .models import Entry, Post, Tag, Topic

admin.site.register(Entry)
admin.site.register(Post)
admin.site.register(Tag)
admin.site.register(Topic)
