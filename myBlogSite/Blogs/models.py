from django.db import models
from django.urls import reverse
from ckeditor.fields import RichTextField

# Create your models here.
class Post(models.Model):
    title=models.CharField(max_length=200)
    # author=models.ForeignKey(User,on_delete=models.CASCADE)
    # author=models.ForeignKey(settings.AUTH_USER_MODEL,on_delete = models.CASCADE)
    category = models.CharField(max_length=200)
    FeatureImages =models.ImageField(null=True, blank=True,upload_to="images/")
    body = RichTextField(blank=True, null=True)
    date=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('Post')

# class Comment(models.Model):
#     post=models.ForeignKey(Post,related_name="comments",on_delete=models.CASCADE,null=True)
#     name=models.CharField(max_length=200)
#     comment=models.TextField()
#     date=models.DateTimeField(auto_now_add=True)
#
#     def __str__(self):
#         return '%s - %s ' % (self.post.title,self.name)

    # def get_absolute_url(self):
    #     return reverse('PostDetail',kwargs={'pk': self.pk})