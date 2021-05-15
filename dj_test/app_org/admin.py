# ../app_org/admin.py


from django.contrib import admin

from .models import Test_liste_01


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