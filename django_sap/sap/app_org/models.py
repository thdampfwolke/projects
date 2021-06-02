# ../app_org/models.py

from django.db import models


# ----------------------------------------------------------------------------
class Infra_umgebung(models.Model):
    # id = int
    name = models.CharField(max_length=120, unique=True)
    beschreibung = models.TextField(null=True, blank=True)
    check = models.BooleanField(null=False, default=False)
    is_active = models.BooleanField(null=False, default=True)
    date_beg = models.DateField(null=False)
    date_end = models.DateField(null=False, default='2099-12-31')
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Infra_umgebung"
        verbose_name_plural = "Infra_umgebung"
        ordering = ["name"]

    def __str__(self):
        return f"{self.name}"

# ----------------------------------------------------------------------------


class Inventar(models.Model):
    # id = int
    name = models.CharField(max_length=120, unique=True)
    beschreibung = models.TextField(null=True, blank=True)
    check = models.BooleanField(null=False, default=False)
    is_active = models.BooleanField(null=False, default=True)
    date_beg = models.DateField(null=False)
    date_end = models.DateField(null=False, default='2099-12-31')
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
    inventar_art = models.ManyToManyField("Inventar_art", blank=False)

    class Meta:
        verbose_name = "Inventar"
        verbose_name_plural = "Inventar"
        ordering = ["name"]

    def __str__(self):
        return f"{self.name}"

#  -->  t2t: app_org_inventar_inventar_art


class Inventar_art(models.Model):
    # id = int
    name = models.CharField(max_length=120, unique=True)
    beschreibung = models.TextField(null=True, blank=True)
    check = models.BooleanField(null=False, default=False)
    is_active = models.BooleanField(null=False, default=True)
    date_beg = models.DateField(null=False)
    date_end = models.DateField(null=False, default='2099-12-31')
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Inventar_art"
        verbose_name_plural = "Inventar_art"
        ordering = ["name"]

    def __str__(self):
        return f"{self.name}"

# ----------------------------------------------------------------------------


class Itsk_objekte(models.Model):
    # id = int
    name = models.CharField(max_length=120, unique=True)
    beschreibung = models.TextField(null=True, blank=True)
    check = models.BooleanField(null=False, default=False)
    is_active = models.BooleanField(null=False, default=True)
    date_beg = models.DateField(null=False)
    date_end = models.DateField(null=False, default='2099-12-31')
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Itsk_objekte"
        verbose_name_plural = "Itsk_objekte"
        ordering = ["name"]

    def __str__(self):
        return f"{self.name}"

# ----------------------------------------------------------------------------


class Komponente(models.Model):
    # id = int
    name = models.CharField(max_length=120, unique=True)
    beschreibung = models.TextField(null=True, blank=True)
    check = models.BooleanField(null=False, default=False)
    is_active = models.BooleanField(null=False, default=True)
    date_beg = models.DateField(null=False)
    date_end = models.DateField(null=False, default='2099-12-31')
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
    komponente_art = models.ManyToManyField("Komponente_art", blank=False)

    class Meta:
        verbose_name = "Komponente"
        verbose_name_plural = "Komponente"
        ordering = ["name"]

    def __str__(self):
        return f"{self.name}"

#  -->  t2t: app_org_komponente_komponente_art


class Komponente_art(models.Model):
    # id = int
    name = models.CharField(max_length=120, unique=True)
    beschreibung = models.TextField(null=True, blank=True)
    check = models.BooleanField(null=False, default=False)
    is_active = models.BooleanField(null=False, default=True)
    date_beg = models.DateField(null=False)
    date_end = models.DateField(null=False, default='2099-12-31')
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Komponente_art"
        verbose_name_plural = "Komponente_art"
        ordering = ["name"]

    def __str__(self):
        return f"{self.name}"

# ----------------------------------------------------------------------------


class Mitarbeiter(models.Model):
    # id = int
    nachname = models.CharField(max_length=120, null=False)
    vorname = models.CharField(max_length=120, null=False)
    geburtstag = models.DateField(null=True, blank=True)
    bild = models.ImageField(upload_to='pics', null=True, blank=True)
    email = models.EmailField(
        max_length=254, null=True, blank=True, unique=True)
    beschreibung = models.TextField(null=True, blank=True)
    check = models.BooleanField(null=False, default=False)
    is_active = models.BooleanField(null=False, default=True)
    date_beg = models.DateField(null=False)
    date_end = models.DateField(null=False, default='2099-12-31')
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Mitarbeiter"
        verbose_name_plural = "Mitarbeiter"
        ordering = ["nachname", "vorname"]

    def __str__(self):
        return f"{self.nachname}, {self.vorname}"

# ----------------------------------------------------------------------------


class Remedy(models.Model):
    # id = int
    remedy = models.CharField(max_length=120, unique=True)
    beschreibung = models.TextField(null=True, blank=True)
    check = models.BooleanField(null=False, default=False)
    is_active = models.BooleanField(null=False, default=True)
    date_beg = models.DateField(null=False)
    date_end = models.DateField(null=False, default='2099-12-31')
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Remedy"
        verbose_name_plural = "Remedy"
        ordering = ["remedy"]

    def __str__(self):
        return f"{self.remedy}"

# ----------------------------------------------------------------------------


class Rolle(models.Model):
    # id = int
    rolle = models.CharField(max_length=120, unique=True)
    beschreibung = models.TextField(null=True, blank=True)
    check = models.BooleanField(null=False, default=False)
    is_active = models.BooleanField(null=False, default=True)
    date_beg = models.DateField(null=False)
    date_end = models.DateField(null=False, default='2099-12-31')
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Rolle"
        verbose_name_plural = "Rolle"
        ordering = ["rolle"]

    def __str__(self):
        return f"{self.rolle}"

# ----------------------------------------------------------------------------


class Sap_system_landschaft(models.Model):
    # id = int
    name = models.CharField(max_length=120, unique=True)
    beschreibung = models.TextField(null=True, blank=True)
    check = models.BooleanField(null=False, default=False)
    is_active = models.BooleanField(null=False, default=True)
    date_beg = models.DateField(null=False)
    date_end = models.DateField(null=False, default='2099-12-31')
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Sap_system_landschaft"
        verbose_name_plural = "Sap_system_landschaft"
        ordering = ["name"]

    def __str__(self):
        return f"{self.name}"

# ----------------------------------------------------------------------------


class Standort(models.Model):
    # id = int
    standort = models.CharField(max_length=120)
    strasse = models.CharField(max_length=120)
    raum = models.CharField(max_length=120)
    beschreibung = models.TextField(null=True, blank=True)
    check = models.BooleanField(null=False, default=False)
    is_active = models.BooleanField(null=False, default=True)
    date_beg = models.DateField(null=False)
    date_end = models.DateField(null=False, default='2099-12-31')
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Standort"
        verbose_name_plural = "Standort"
        ordering = ["standort", "strasse", "raum"]

    def __str__(self):
        return f"{self.standort}"

# ----------------------------------------------------------------------------


class Verfahren(models.Model):
    # id = int
    verfahren = models.CharField(max_length=120, unique=True)
    email = models.EmailField(
        max_length=254, null=True, blank=True, unique=True)
    beschreibung = models.TextField(null=True, blank=True)
    check = models.BooleanField(null=False, default=False)
    is_active = models.BooleanField(null=False, default=True)
    date_beg = models.DateField(null=False)
    date_end = models.DateField(null=False, default='2099-12-31')
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Verfahren"
        verbose_name_plural = "Verfahren"
        ordering = ["verfahren"]

    def __str__(self):
        return f"{self.verfahren}"


# ----------------------------------------------------------------------------
# open: 26.04.2021
#
# t2t: mitarbeiter - rolle - verfahren - komponente - remedy

class Zt2t_ma2ro2ve2ko2re(models.Model):
    t2t_mitarbeiter = models.ForeignKey(
        Mitarbeiter, verbose_name="Mitarbeiter", null=True, blank=False, on_delete=models.PROTECT)
    t2t_rolle = models.ForeignKey(Rolle, verbose_name="Rolle",
                                  null=True, blank=False, on_delete=models.PROTECT)
    t2t_verfahren = models.ForeignKey(
        Verfahren, verbose_name="Verfahren",     null=True, blank=True,  on_delete=models.PROTECT)
    t2t_komponente = models.ForeignKey(
        Komponente, verbose_name="Komponente",   null=True, blank=True,  on_delete=models.PROTECT)
    t2t_remedy = models.ForeignKey(
        Remedy, verbose_name="Remedy",           null=True, blank=True,  on_delete=models.PROTECT)
    check = models.BooleanField(null=False, default=False)
    is_active = models.BooleanField(null=False, default=True)
    date_beg = models.DateField(null=False)
    date_end = models.DateField(null=False, default='2099-12-31')
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Zt2t_ma2ro2ve2ko2re"
        verbose_name_plural = "Zt2t_ma2ro2ve2ko2re"
        ordering = ["t2t_mitarbeiter"]

    def __str__(self):
        return f"{self.t2t_mitarbeiter}"
        # return f"{self.t2t_mitarbeiter}, {self.t2t_rolle}"
        # return f"{self.t2t_mitarbeiter}, {self.t2t_rolle}, {self.t2t_verfahren}, {self.t2t_komponente}, {self.t2t_remedy}"


# ----------------------------------------------------------------------------
# class Test_02_dyn:
#    id = int
#    nname = str
#    vname = str
#    img = str
#    desc = str
#    phone = int
#    offer = bool

# ----------------------------------------------------------------------------
# class Test_02_dyn_db(models.Model):
#    # id = int
#    nname = models.CharField(max_length=120)
#    vname = models.CharField(max_length=120)
#    img = models.ImageField(upload_to='pics')
#    desc = models.TextField()
#    phone = models.IntegerField()
#    handy = models.IntegerField()
#    offer = models.BooleanField(default=False)

# unique=True
