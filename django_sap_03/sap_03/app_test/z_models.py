# ../app_test/models.py

from django.db import models


# ----------------------------------------------------------------------------
class Infra_umgebung(models.Model):
    # id = int
    name           = models.CharField(max_length=120)
    beschreibung   = models.TextField(null=True, blank=True)
    check          = models.BooleanField(null=False, default=False)
    is_active      = models.BooleanField(null=False, default=True)
    date_beg       = models.DateField(null=False)
    date_end       = models.DateField(null=False, default='2099-12-31')
    date_created   = models.DateTimeField(auto_now_add=True)
    date_modified  = models.DateTimeField(auto_now=True)

# ----------------------------------------------------------------------------
class Inventar_art(models.Model):
    # id = int
    name           = models.CharField(max_length=120)
    beschreibung   = models.TextField(null=True, blank=True)
    check          = models.BooleanField(null=False, default=False)
    is_active      = models.BooleanField(null=False, default=True)
    date_beg       = models.DateField(null=False)
    date_end       = models.DateField(null=False, default='2099-12-31')
    date_created   = models.DateTimeField(auto_now_add=True)
    date_modified  = models.DateTimeField(auto_now=True)

# ----------------------------------------------------------------------------
class Inventar(models.Model):
    # id = int
    name           = models.CharField(max_length=120)
    beschreibung   = models.TextField(null=True, blank=True)
    inventar_art   = models.ForeignKey(Inventar_art, on_delete=models.CASCADE)
    check          = models.BooleanField(null=False, default=False)
    is_active      = models.BooleanField(null=False, default=True)
    date_beg       = models.DateField(null=False)
    date_end       = models.DateField(null=False, default='2099-12-31')
    date_created   = models.DateTimeField(auto_now_add=True)
    date_modified  = models.DateTimeField(auto_now=True)

# ----------------------------------------------------------------------------
class Itsk_objekte(models.Model):
    # id = int
    name           = models.CharField(max_length=120)
    beschreibung   = models.TextField(null=True, blank=True)
    check          = models.BooleanField(null=False, default=False)
    is_active      = models.BooleanField(null=False, default=True)
    date_beg       = models.DateField(null=False)
    date_end       = models.DateField(null=False, default='2099-12-31')
    date_created   = models.DateTimeField(auto_now_add=True)
    date_modified  = models.DateTimeField(auto_now=True)

# ----------------------------------------------------------------------------
class Komponente_art(models.Model):
    # id = int
    komponente_art = models.CharField(max_length=120)
    beschreibung   = models.TextField(null=True, blank=True)
    check          = models.BooleanField(null=False, default=False)
    is_active      = models.BooleanField(null=False, default=True)
    date_beg       = models.DateField(null=False)
    date_end       = models.DateField(null=False, default='2099-12-31')
    date_created   = models.DateTimeField(auto_now_add=True)
    date_modified  = models.DateTimeField(auto_now=True)

# ----------------------------------------------------------------------------
class Komponente(models.Model):
    # id = int
    komponente     = models.CharField(max_length=120)
    beschreibung   = models.TextField(null=True, blank=True)
    komponente_art = models.ForeignKey(Komponente_art, on_delete=models.CASCADE)
    check          = models.BooleanField(null=False, default=False)
    is_active      = models.BooleanField(null=False, default=True)
    date_beg       = models.DateField(null=False)
    date_end       = models.DateField(null=False, default='2099-12-31')
    date_created   = models.DateTimeField(auto_now_add=True)
    date_modified  = models.DateTimeField(auto_now=True)

# ----------------------------------------------------------------------------
class Remedy(models.Model):
    # id = int
    remedy         = models.CharField(max_length=120)
    beschreibung   = models.TextField(null=True, blank=True)
    check          = models.BooleanField(null=False, default=False)
    is_active      = models.BooleanField(null=False, default=True)
    date_beg       = models.DateField(null=False)
    date_end       = models.DateField(null=False, default='2099-12-31')
    date_created   = models.DateTimeField(auto_now_add=True)
    date_modified  = models.DateTimeField(auto_now=True)

# ----------------------------------------------------------------------------
class Rolle(models.Model):
    # id = int
    rolle          = models.CharField(max_length=120)
    beschreibung   = models.TextField(null=True, blank=True)
    check          = models.BooleanField(null=False, default=False)
    is_active      = models.BooleanField(null=False, default=True)
    date_beg       = models.DateField(null=False)
    date_end       = models.DateField(null=False, default='2099-12-31')
    date_created   = models.DateTimeField(auto_now_add=True)
    date_modified  = models.DateTimeField(auto_now=True)

# ----------------------------------------------------------------------------
class Sap_system_landschaft(models.Model):
    # id = int
    name           = models.CharField(max_length=120)
    beschreibung   = models.TextField(null=True, blank=True)
    check          = models.BooleanField(null=False, default=False)
    is_active      = models.BooleanField(null=False, default=True)
    date_beg       = models.DateField(null=False)
    date_end       = models.DateField(null=False, default='2099-12-31')
    date_created   = models.DateTimeField(auto_now_add=True)
    date_modified  = models.DateTimeField(auto_now=True)

# ----------------------------------------------------------------------------
class Staff(models.Model):
    # id = int
    nname          = models.CharField(max_length=120, null=False)
    vname          = models.CharField(max_length=120, null=False)
    geb            = models.DateField(null=True, blank=True)
    pic            = models.ImageField(upload_to='pics', null=True, blank=True)
    email          = models.CharField(max_length=254, null=True, blank=True)
    desc           = models.TextField(null=True, blank=True)
    check          = models.BooleanField(null=False, default=False)
    is_active      = models.BooleanField(null=False, default=True)
    date_beg       = models.DateField(null=False)
    date_end       = models.DateField(null=False, default='2099-12-31')
    date_created   = models.DateTimeField(auto_now_add=True)
    date_modified  = models.DateTimeField(auto_now=True)

# ----------------------------------------------------------------------------
class Standort(models.Model):
    # id = int
    standort       = models.CharField(max_length=120)
    strasse        = models.CharField(max_length=120)
    raum           = models.CharField(max_length=120)
    beschreibung   = models.TextField(null=True, blank=True)
    check          = models.BooleanField(null=False, default=False)
    is_active      = models.BooleanField(null=False, default=True)
    date_beg       = models.DateField(null=False)
    date_end       = models.DateField(null=False, default='2099-12-31')
    date_created   = models.DateTimeField(auto_now_add=True)
    date_modified  = models.DateTimeField(auto_now=True)

# ----------------------------------------------------------------------------
class Verfahren(models.Model):
    # id = int
    verfahren      = models.CharField(max_length=120)
    beschreibung   = models.TextField(null=True, blank=True)
    check          = models.BooleanField(null=False, default=False)
    is_active      = models.BooleanField(null=False, default=True)
    date_beg       = models.DateField(null=False)
    date_end       = models.DateField(null=False, default='2099-12-31')
    date_created   = models.DateTimeField(auto_now_add=True)
    date_modified  = models.DateTimeField(auto_now=True)
