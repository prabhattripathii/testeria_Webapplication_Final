from django.db import models

# Create your models here.
from django.db import models
from django.utils import timezone


class Blog(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    content = models.TextField()
    pub_date = models.DateTimeField(default=timezone.now)
    image = models.ImageField(upload_to='blog_images/', blank=True, null=True)
    articleLink = models.CharField(max_length=100, blank=True, default=None)

    def _str_(self):
        return self.title


class Category(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(unique=True)

    def _str_(self):
        return self.name
