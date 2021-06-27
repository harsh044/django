from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title','author','category','body')

        widgets = {
            'title' :forms.TextInput(attrs={'class': 'form-control mt-3','placeholder':'This is title'}),
            'author' :forms.TextInput(attrs={'class': 'form-control mt-3','value':'','id':'username','type':'hidden'}),
            'category' :forms.TextInput(attrs={'class': 'form-control mt-3','placeholder':'make your category'}),
            'body' :forms.Textarea(attrs={'class': 'form-control mt-3','placeholder':'This is Message-body'}),
        }

class UpdateForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title','body')

        widgets = {
            'title' :forms.TextInput(attrs={'class': 'form-control','placeholder':'This is title'}),
            'body' :forms.Textarea(attrs={'class': 'form-control','placeholder':'This is Message-body'}),
        }
