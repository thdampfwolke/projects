# ------------------------------------------------------------------
# ../dj_blog/app_server/models.py
# ------------------------------------------------------------------

from django.db import models

# from django.urls import reverse
# from django.utils import timezone
# from django.contrib.auth.models import User
# from django.contrib.auth.models.Group import xxx
# from django.contrib.auth.urls import xxx


# ------------------------------------------------------------------
#
class Server(models.Model):
    # id = int
    name = models.CharField(
        max_length=60, unique=True, null=False, blank=False)

    class Meta:
        verbose_name = 'SERVER'
        verbose_name_plural = 'SERVER'
        ordering = ('id',)

    def __str__(self):
        return f"{self.id, self.name}"


# ------------------------------------------------------------------
#
class Verfahren(models.Model):
    # id = int
    name = models.CharField(
        max_length=60, unique=True, null=False, blank=False)

    class Meta:
        verbose_name = 'VERFAHREN'
        verbose_name_plural = 'VERFAHREN'
        ordering = ('id',)

    def __str__(self):
        return f"{self.id, self.name}"


# ------------------------------------------------------------------
#
class T2T_server2verfahren(models.Model):
    # id = int
    server = models.ForeignKey(Server,    on_delete=models.CASCADE)
    verfahren = models.ForeignKey(Verfahren, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'T2T_SERVER2VERFAHREN'
        verbose_name_plural = 'T2T_SERVER2VERFAHREN'
        ordering = ('id',)

    def __str__(self):
        return f"{self.id, self.server, self.verfahren}"


# ------------------------------------------------------------------
#
class H2H_server2verfahren(models.Model):
    # id = int
    server = models.CharField(
        max_length=60, unique=True, null=False, blank=False)
    verfahren = models.CharField(
        max_length=60, unique=True, null=False, blank=False)

    class Meta:
        verbose_name = 'H2H_SERVER2VERFAHREN'
        verbose_name_plural = 'H2H_SERVER2VERFAHREN'
        ordering = ('id',)

    def __str__(self):
        return f"{self.id, self.server, self.verfahren}"


# # ------------------------------------------------------------------
# class Post(models.Model):
#     # id = int
#     title = models.CharField(
#         max_length=120, unique=True, null=False, blank=False)
#     text = models.TextField(unique=False, null=False, blank=False)
#     topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
#     tag = models.ManyToManyField(Tag)
#     # models.ManyToManyField(Topic)
#     # owner = models.ForeignKey(User, on_delete=models.CASCADE)
#     # group = models.CharField      # ersteller - gruppe
#     is_checked = models.BooleanField(null=False, default=False)
#     is_active = models.BooleanField(null=False, default=True)
#     date_beg = models.DateField(null=False, default='2000-01-01')
#     date_end = models.DateField(null=False, default='2099-12-31')
#     date_created = models.DateTimeField(auto_now_add=True)
#     date_modified = models.DateTimeField(auto_now=True)
#
#     class Meta:
#         verbose_name = 'POST'
#         verbose_name_plural = 'POST'
#         ordering = ('-date_modified',)
#
#     def __str__(self):
#         if len(f"{self.text}") > 50:
#             return f"{self.title, self.text[:50]}..."
#         else:
#             return f"{self.title, self.text}"
