# ../app_org/admin.py


from django.contrib import admin
from django_admin_listfilter_dropdown.filters import (
    DropdownFilter, ChoiceDropdownFilter, RelatedDropdownFilter
)
from .models import Infra_umgebung, Inventar, Inventar_art, Itsk_objekte
from .models import Komponente, Komponente_art, Mitarbeiter, Remedy, Rolle
from .models import Sap_system_landschaft, Standort, Verfahren
from .models import Zt2t_ma2ro2ve2ko2re


@admin.register(Infra_umgebung)
class Infra_umgebungAdmin(admin.ModelAdmin):
    list_display = ['name', 'beschreibung', 'is_active', 'check']
    list_filter = ['is_active']

@admin.register(Inventar)
class InventarAdmin(admin.ModelAdmin):
    list_display = ['name', 'beschreibung', 'is_active', 'check']
    list_filter = ['is_active']

@admin.register(Inventar_art)
class Inventar_artAdmin(admin.ModelAdmin):
    list_display = ['name', 'beschreibung', 'is_active', 'check']
    list_filter = ['is_active']

# Itsk_objekte
@admin.register(Itsk_objekte)
class Itsk_objekteAdmin(admin.ModelAdmin):
    list_display = ['name', 'beschreibung', 'is_active', 'check']
    list_filter = ['is_active']

@admin.register(Komponente)
class KomponenteAdmin(admin.ModelAdmin):
    list_display = ['name', 'beschreibung', 'is_active', 'check']
    list_filter = ['is_active']

@admin.register(Komponente_art)
class Komponente_artAdmin(admin.ModelAdmin):
    list_display = ['name', 'beschreibung', 'is_active', 'check']
    list_filter = ['is_active']

@admin.register(Mitarbeiter)
class MitarbeiterAdmin(admin.ModelAdmin):
    list_display = ['nachname', 'vorname', 'geburtstag', 'bild', 'email', 'beschreibung', 'is_active', 'check']
    list_filter = ['is_active']

@admin.register(Remedy)
class RemedyAdmin(admin.ModelAdmin):
    list_display = ['remedy', 'beschreibung', 'is_active', 'check']
    list_filter = ['is_active']

@admin.register(Rolle)
class RolleAdmin(admin.ModelAdmin):
    list_display = ['rolle', 'beschreibung', 'is_active', 'check']
    list_filter = ['is_active']

@admin.register(Sap_system_landschaft)
class Sap_system_landschaftAdmin(admin.ModelAdmin):
    list_display = ['name', 'beschreibung', 'is_active', 'check']
    list_filter = ['is_active']

@admin.register(Standort)
class StandortAdmin(admin.ModelAdmin):
    list_display = ['standort', 'strasse', 'raum', 'beschreibung', 'is_active', 'check']
    list_filter = ['is_active']

@admin.register(Verfahren)
class VerfahrenAdmin(admin.ModelAdmin):
    list_display = ['verfahren', 'email', 'beschreibung', 'is_active', 'check']
    list_filter = ['is_active']

@admin.register(Zt2t_ma2ro2ve2ko2re)
class Zt2t_ma2ro2ve2ko2reAdmin(admin.ModelAdmin):
    list_display = ['t2t_mitarbeiter', 't2t_rolle', 't2t_verfahren', 't2t_komponente', 't2t_remedy', 'is_active', 'check']
    # list_filter = ['t2t_verfahren', 't2t_rolle', 'is_active', 'check']
    list_filter = (
        ('t2t_mitarbeiter', RelatedDropdownFilter),
        ('t2t_rolle', RelatedDropdownFilter),
        ('t2t_verfahren', RelatedDropdownFilter),
        ('t2t_komponente', RelatedDropdownFilter),
        ('t2t_remedy', RelatedDropdownFilter),
        ('is_active', DropdownFilter),
    )


#    list_filter = (
#        # for ordinary fields
#        ('a_charfield', DropdownFilter),
#        # for choice fields
#        ('a_choicefield', ChoiceDropdownFilter),
#        # for related fields
#        ('a_foreignkey_field', RelatedDropdownFilter),
#    )



# Zt2t_ma2ro2ve2ko2re


# @admin.register(Beispiel)
# class BeispielAdmin(admin.ModelAdmin):
#     list_display = ['title', 'author', 'slug', 'price', 'in_stock', 'created', 'updated']
#     list_filter = ['in_stock', 'is_active']
#     list_editable = ['price', 'in_stock']
#     prepopulated_fields = {'slug': ('title',)}
