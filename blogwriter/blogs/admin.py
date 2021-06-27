from django.contrib import admin
from .models import Post

# Register your models here.
class PostAdmin(admin.ModelAdmin):
    list_display = ('id','title','author','category','date')

admin.site.register(Post,PostAdmin)