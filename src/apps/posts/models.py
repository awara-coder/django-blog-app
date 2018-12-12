from django.db import models
import datetime

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length = 150)
    content = models.TextField()
    published = models.DateTimeField(auto_now = False, auto_now_add = True)
    last_modified = models.DateTimeField(auto_now = True, auto_now_add = False)

    def __str__(self):
        return self.title