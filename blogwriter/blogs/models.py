from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

# Create your models here.
class Post(models.Model):
    title=models.CharField(max_length=200)
    author=models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    category = models.CharField(max_length=200)
    body = models.TextField(blank=True, null=True)
    date=models.DateTimeField(auto_now_add=True)
    slug = models.CharField(max_length=200)
    

    def get_absolute_url(self):
        return reverse('Post')