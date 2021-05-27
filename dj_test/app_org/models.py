# ../app_xxx/models.py

import uuid
from django.db import models
#from django.contrib.auth.models import User


# ----------------------------------------------------------------------------
# open: 26.04.2021
#
# t2t: mitarbeiter - rolle - verfahren - komponente - remedy


class Server_uuid(models.Model):
    uuid = models.UUIDField(editable=False, default=uuid.uuid4, unique=True)
    is_active = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "server_uuid"
        verbose_name_plural = "server_uuid"
        ordering = ["uuid"]

    def __str__(self):
        return f"{self.uuid}"


class Server_hostname(models.Model):
    name = models.CharField(max_length=25, unique=True)
    is_active = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "server_hostname"
        verbose_name_plural = "server_hostname"
        ordering = ["name"]

    def __str__(self):
        return f"{self.name}"


class Zt2t_server(models.Model):
    t2t_uuid = models.ForeignKey(
        Server_uuid, verbose_name="uuid", null=True, blank=False, on_delete=models.PROTECT)
    t2t_name = models.ForeignKey(Server_hostname, verbose_name="Server_hostname",
                                 null=True, blank=False, on_delete=models.PROTECT)
    check = models.BooleanField(null=False, default=False)
    is_active = models.BooleanField(null=False, default=True)
    date_beg = models.DateField(null=False)
    date_end = models.DateField(null=False, default='2099-12-31')
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Zt2t_server"
        verbose_name_plural = "Zt2t_server"
        ordering = ["t2t_uuid"]

    def __str__(self):
        return f"{self.t2t_uuid}"


class Test_liste_01(models.Model):
    ROLE_CHOICES = (
        (1, 'Customer'),
        (2, 'Supplier'),
        (3, 'Admin'),
        (4, 'SuperAdmin'),
    )
    #user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=25, unique=True)
    birthdate = models.DateField(null=True, blank=True)
    role = models.PositiveSmallIntegerField(
        choices=ROLE_CHOICES, null=True, blank=True)
    is_active = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # @property
    # def email(self):
    #    return "%s"%(self.user.email)

    # def __str__(self):
    #    return self.user.username
