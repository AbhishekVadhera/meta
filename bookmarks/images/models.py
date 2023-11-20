from django.contrib.auth.models import User
from django.db import models
from django.db.models import CASCADE
from django.utils.text import slugify


# Create your models here.

class Image(models.Model):
    user = models.ForeignKey(User, on_delete=CASCADE, related_name='images_created')
    slug = models.SlugField(max_length=250, blank=True)
    title = models.CharField(max_length=250)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='images/%Y/%m/%d/')
    url = models.URLField(max_length=2000)
    created = models.DateField(auto_now_add=True)
    users_like = models.ManyToManyField(User, related_name='images_liked', blank=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)
