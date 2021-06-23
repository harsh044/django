from django.db import models
from django.urls import reverse
from ckeditor.fields import RichTextField

# Create your models here.
class Post(models.Model):
    title=models.CharField(max_length=200)
    category = models.CharField(max_length=200)
    body = RichTextField(blank=True, null=True)
    date=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('Post')