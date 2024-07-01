from django.db import models
from django.utils.text import slugify

from django.utils import timezone


class Post(models.Model):
    judul = models.CharField(max_length=225)
    body = models.TextField()
    category = models.CharField(max_length=225)
    waktuPosting = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(default=timezone.now)
    slug = models.SlugField(blank=True, editable=False)
    
    
    def save(self):
        self.slug = slugify(self.judul)
        super(Post, self).save()
    def __str__(self):
        return "{}. {}".format(self.id, self.judul)    
