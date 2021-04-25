# ../app_org/admin.py

from django.contrib import admin
from app_org.models import Zmitarbeiter, Zrolle, Zverfahren, Zt2t_ma_ro_ve


@admin.register(Zmitarbeiter)
class ZmitarbeiterAdmin(admin.ModelAdmin):
    list_display = ("nachname", "vorname", "email", "geburtstag")
    list_filter = ("is_active", )
    search_fields = ("last_name__startswith", )
    # list_display = ("last_name", "first_name", "show_average")
    # fields = ("first_name", "last_name", "courses")
    # search_fields = ("last_name__startswith", )


@admin.register(Zrolle)
class ZrolleAdmin(admin.ModelAdmin):
    list_display = ("rolle", "beschreibung")
    list_filter = ("is_active", )


@admin.register(Zverfahren)
class ZverfahrenAdmin(admin.ModelAdmin):
    list_display = ("verfahren", "beschreibung")
    list_filter = ("is_active", )


@admin.register(Zt2t_ma_ro_ve)
class Zt2t_ma_ro_veAdmin(admin.ModelAdmin):
    list_display = ("t2t_mitarbeiter", "t2t_rolle", "t2t_verfahren")
    list_filter = ("is_active", )

# app_org_zmitarbeiter_rollen
# id  zmitarbeiter_id     zrolle_id
# 1   1                   1
# 2   1                   3
