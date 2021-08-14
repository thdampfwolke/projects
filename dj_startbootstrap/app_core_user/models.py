# ../app_core_user/models.py

from django.db import models


# ----------------------------------------------------------------------------
class User(models.Model):
    # id = int
    nname = models.CharField(max_length=32, null=False)
    vname = models.CharField(max_length=32, null=False)
    geb = models.DateField(null=True, blank=True)
    email = models.EmailField(
        max_length=64, null=True, blank=True, unique=True)
    is_active = models.BooleanField(null=False, default=True)
    date_beg = models.DateField(null=False, default='2000-01-01')
    date_end = models.DateField(null=False, default='2099-12-31')
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "User"
        verbose_name_plural = "User"
        ordering = ["id", "nname", "vname"]

    def __str__(self):
        return f"{self.id}, {self.nname}, {self.vname}"


# ----------------------------------------------------------------------------
class UserId(models.Model):
    # id = int
    uid = models.CharField(max_length=32, null=False)
    is_active = models.BooleanField(null=False, default=True)
    date_beg = models.DateField(null=False, default='2000-01-01')
    date_end = models.DateField(null=False, default='2099-12-31')
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "UserId"
        verbose_name_plural = "UserId"
        ordering = ["id", "uid"]

    def __str__(self):
        return f"{self.id}, {self.uid}"


# ----------------------------------------------------------------------------
class Z_user2userid(models.Model):
    t2t_user = models.ForeignKey(
        User,   verbose_name="User",   null=True, blank=False, on_delete=models.CASCADE)
    t2t_userid = models.ForeignKey(
        UserId, verbose_name="UserId", null=True, blank=False, on_delete=models.CASCADE)
    is_active = models.BooleanField(null=False, default=True)
    date_beg = models.DateField(null=False, default='2001-01-01')
    date_end = models.DateField(null=False, default='2099-12-31')
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Z_user2userid"
        verbose_name_plural = "Z_user2userid"
        ordering = ["id", "t2t_user", "t2t_userid"]

    def __str__(self):
        return f"{self.id}, {self.t2t_user}, {self.t2t_userid}"


# # ----------------------------------------------------------------------------
# # open: 26.04.2021
# #
# # t2t: mitarbeiter - rolle - verfahren - komponente - remedy
#
# class Zt2t_ma2ro2ve2ko2re(models.Model):
#     t2t_mitarbeiter = models.ForeignKey(Mitarbeiter, verbose_name="Mitarbeiter", null=True, blank=False, on_delete=models.PROTECT)
#     t2t_rolle       = models.ForeignKey(Rolle, verbose_name="Rolle",             null=True, blank=False, on_delete=models.PROTECT)
#     t2t_verfahren   = models.ForeignKey(Verfahren, verbose_name="Verfahren",     null=True, blank=True,  on_delete=models.PROTECT)
#     t2t_komponente  = models.ForeignKey(Komponente, verbose_name="Komponente",   null=True, blank=True,  on_delete=models.PROTECT)
#     t2t_remedy      = models.ForeignKey(Remedy, verbose_name="Remedy",           null=True, blank=True,  on_delete=models.PROTECT)
#     check = models.BooleanField(null=False, default=False)
#     is_active = models.BooleanField(null=False, default=True)
#     date_beg = models.DateField(null=False)
#     date_end = models.DateField(null=False, default='2099-12-31')
#     date_created = models.DateTimeField(auto_now_add=True)
#     date_modified = models.DateTimeField(auto_now=True)
#
#     class Meta:
#         verbose_name = "Zt2t_ma2ro2ve2ko2re"
#         verbose_name_plural = "Zt2t_ma2ro2ve2ko2re"
#         ordering = ["t2t_mitarbeiter"]
#
#     def __str__(self):
#         return f"{self.t2t_mitarbeiter}"
#         #return f"{self.t2t_mitarbeiter}, {self.t2t_rolle}"
#         #return f"{self.t2t_mitarbeiter}, {self.t2t_rolle}, {self.t2t_verfahren}, {self.t2t_komponente}, {self.t2t_remedy}"
