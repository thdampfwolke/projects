# ../app_org/admin.py


from django.contrib import admin

from .models import Test_liste_01, Server_uuid, Server_hostname, Zt2t_server


@admin.register(Zt2t_server)
class Zt2t_serverAdmin(admin.ModelAdmin):
    list_display = ['t2t_uuid', 't2t_name', 'is_active']
    list_filter = ['is_active']


@admin.register(Server_hostname)
class Server_hostnameAdmin(admin.ModelAdmin):
    list_display = ['name', 'is_active']
    list_filter = ['is_active']


@admin.register(Server_uuid)
class Server_uuidAdmin(admin.ModelAdmin):
    list_display = ['uuid', 'is_active']
    list_filter = ['is_active']


@admin.register(Test_liste_01)
class Test_liste_01Admin(admin.ModelAdmin):
    list_display = ['name', 'role', 'is_active']
    list_filter = ['is_active', 'role']


"""
class Test_liste_01(models.Model):
    ROLE_CHOICES = (
        (1, 'Customer'),
        (2, 'Supplier'),
        (3, 'Admin'),
        (4, 'SuperAdmin'),
    )
    #user = models.OneToOneField(User, on_delete=models.CASCADE)
    name       = models.CharField(max_length=25, unique=True)
    birthdate  = models.DateField(null=True, blank=True)
    role       = models.PositiveSmallIntegerField(choices=ROLE_CHOICES, null=True, blank=True)
    is_active  = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

"""
