# ../app_core_server/models.py

from django.db import models


# ----------------------------------------------------------------------------
class Server(models.Model):
    # id = int
    server = models.CharField(max_length=32, null=False, unique=True)
    model = models.CharField(max_length=32, null=False)
    is_active = models.BooleanField(null=False, default=True)
    date_beg = models.DateField(null=False, default='2000-01-01')
    date_end = models.DateField(null=False, default='2099-12-31')
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Server"
        verbose_name_plural = "Server"
        ordering = ["id", "server"]

    def __str__(self):
        return f"{self.id}, {self.server}, {self.model}"


# ----------------------------------------------------------------------------
class Ip(models.Model):
    # id = int
    ip = models.CharField(max_length=16, null=False, unique=True)
    is_active = models.BooleanField(null=False, default=True)
    date_beg = models.DateField(null=False, default='2000-01-01')
    date_end = models.DateField(null=False, default='2099-12-31')
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Ip"
        verbose_name_plural = "Ip"
        ordering = ["id", "ip"]

    def __str__(self):
        return f"{self.id}, {self.ip}"


# ----------------------------------------------------------------------------
class Z_server2ip(models.Model):
    t2t_server = models.ForeignKey(
        Server, verbose_name="Server",   null=True, blank=False, on_delete=models.CASCADE)
    t2t_ip = models.ForeignKey(
        Ip, verbose_name="Ip", null=True, blank=False, on_delete=models.CASCADE)
    is_active = models.BooleanField(null=False, default=True)
    date_beg = models.DateField(null=False, default='2001-01-01')
    date_end = models.DateField(null=False, default='2099-12-31')
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Z_server2ip"
        verbose_name_plural = "Z_server2ip"
        ordering = ["id", "t2t_server", "t2t_ip"]

    def __str__(self):
        return f"{self.id}, {self.t2t_server}, {self.t2t_ip}"


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
