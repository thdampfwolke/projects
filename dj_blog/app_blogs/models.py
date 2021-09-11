# ------------------------------------------------------------------
# ../dj_blog/app_blogs/models.py
# ------------------------------------------------------------------

from django.db import models

# from django.urls import reverse
# from django.utils import timezone
# from django.contrib.auth.models import User
# from django.contrib.auth.models.Group import xxx
# from django.contrib.auth.urls import xxx


# ------------------------------------------------------------------
# BLOG      BLOG
# posts		Beitraege
# tags		Stichworte      n:n     Netz, Server, TA, . . .
# topics	Themen		    1:n     Stoerung, Wartung, . . .
# title		Titel


# ------------------------------------------------------------------
class Topic(models.Model):
    # id = int
    topic = models.CharField(
        max_length=60, unique=True, null=False, blank=False)
    # owner = models.ForeignKey(User, on_delete=models.CASCADE)
    # group = models.CharField      # ersteller - gruppe
    is_checked = models.BooleanField(null=False, default=False)
    is_active = models.BooleanField(null=False, default=True)
    date_beg = models.DateField(null=False, default='2000-01-01')
    date_end = models.DateField(null=False, default='2099-12-31')
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'TOPIC'
        verbose_name_plural = 'TOPIC'
        ordering = ('-date_modified',)

    def __str__(self):
        return self.topic


# ------------------------------------------------------------------
class Tag(models.Model):
    # id = int
    tag = models.CharField(max_length=60, unique=True, null=False, blank=False)
    # owner = models.ForeignKey(User, on_delete=models.CASCADE)
    # group = models.CharField      # ersteller - gruppe
    is_checked = models.BooleanField(null=False, default=False)
    is_active = models.BooleanField(null=False, default=True)
    date_beg = models.DateField(null=False, default='2000-01-01')
    date_end = models.DateField(null=False, default='2099-12-31')
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'TAG'
        verbose_name_plural = 'TAG'
        ordering = ('tag',)

    def __str__(self):
        return self.tag


# ------------------------------------------------------------------
class Post(models.Model):
    # id = int
    title = models.CharField(
        max_length=120, unique=True, null=False, blank=False)
    text = models.TextField(unique=False, null=False, blank=False)
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    tag = models.ManyToManyField(Tag)
    # models.ManyToManyField(Topic)
    # owner = models.ForeignKey(User, on_delete=models.CASCADE)
    # group = models.CharField      # ersteller - gruppe
    is_checked = models.BooleanField(null=False, default=False)
    is_active = models.BooleanField(null=False, default=True)
    date_beg = models.DateField(null=False, default='2000-01-01')
    date_end = models.DateField(null=False, default='2099-12-31')
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'POST'
        verbose_name_plural = 'POST'
        ordering = ('-date_modified',)

    def __str__(self):
        if len(f"{self.text}") > 50:
            return f"{self.title, self.text[:50]}..."
        else:
            return f"{self.title, self.text}"

# Post: id, title. text, topic, tag, is_checked, is_active, date_beg, date_end, date_created, date_modified

# ------------------------------------------------------------------
class Entry(models.Model):
    # id = int
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    text = models.TextField(unique=False, null=False, blank=False)
    # owner = models.ForeignKey(User, on_delete=models.CASCADE)
    # group = models.CharField      # ersteller - gruppe
    is_checked = models.BooleanField(null=False, default=False)
    is_active = models.BooleanField(null=False, default=True)
    date_beg = models.DateField(null=False, default='2000-01-01')
    date_end = models.DateField(null=False, default='2099-12-31')
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'ENTRY'
        verbose_name_plural = 'ENTRY'
        ordering = ('-date_modified',)

    def __str__(self):
        if len(f"{self.text}") > 50:
            return f"{self.text[:50]}..."
        else:
            return f"{self.text}"


# ==================================================================
# old:

# class Topic(models.Model):
#     """A topic the user is learning about."""
#     text = models.CharField(max_length=200)
#     date_added = models.DateTimeField(auto_now_add=True)
#     owner = models.ForeignKey(User, on_delete=models.CASCADE)
#
#     def __str__(self):
#         """Return a string representation of the model."""
#         return self.text
#
#
# class Entry(models.Model):
#     """Something specific learned about a topic."""
#     topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
#     text = models.TextField()
#     date_added = models.DateTimeField(auto_now_add=True)
#
#     class Meta:
#         verbose_name_plural = 'entries'
#
#     def __str__(self):
#         """Return a string representation of the model."""
#         if len(f"{self.text}") > 50:
#             return f"{self.text[:50]}..."
#         else:
#             return f"{self.text}"
#
# class Question(models.Model):
#     # ...
#     def was_published_recently(self):
#         return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
# ----------------------------------------------------------------
# from django.db import models
# from django.urls import reverse
#
# class Post(models.Model):
#     title = models.CharField(max_length=155)
#     content = models.TextField()
#     slug = models.SlugField(max_length=255)
#     image = models.ImageField(upload_to="images/", default="images/default.png")
#
#     def get_absolute_url(self):
#         return reverse("blog:single", args=[self.slug])
#
#     def __str__(self):
#         return self.title

# ../store/models.py

# from django.contrib.auth.models import User
# from django.db import models
# #from django.urls import reverse
#
#
# class ProductManager(models.Manager):
#     def get_queryset(self):
#         return super(ProductManager, self).get_queryset().filter(is_active=True)
#
#
# class Category(models.Model):
#     name = models.CharField(max_length=255, db_index=True)
#     slug = models.SlugField(max_length=255, unique=True)
#
#     class Meta:
#         verbose_name_plural = 'categories'
#
#     #def get_absolute_url(self):
#     #    return reverse('store:category_list', args=[self.slug])
#
#     def __str__(self):
#         return self.name
#
#
# class Product(models.Model):
#     category = models.ForeignKey(Category, related_name='product', on_delete=models.CASCADE)
#     created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='product_creator')
#     title = models.CharField(max_length=255)
#     author = models.CharField(max_length=255, default='admin')
#     description = models.TextField(blank=True)
#     image = models.ImageField(upload_to='images/')
#     slug = models.SlugField(max_length=255)
#     price = models.DecimalField(max_digits=4, decimal_places=2)
#     in_stock = models.BooleanField(default=True)
#     is_active = models.BooleanField(default=True)
#     created = models.DateTimeField(auto_now_add=True)
#     updated = models.DateTimeField(auto_now=True)
#     objects = models.Manager()
#     products = ProductManager()
#
#     class Meta:
#         verbose_name_plural = 'Products'
#         ordering = ('-created',)
#
#     #def get_absolute_url(self):
#     #    return reverse('store:product_detail', args=[self.slug])
#
#     def __str__(self):
#         return self.title
#
