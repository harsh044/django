from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title','category','FeatureImages','body')

        widgets = {
            'title' :forms.TextInput(attrs={'class': 'form-control','placeholder':'This is title'}),
            'body' :forms.Textarea(attrs={'class': 'form-control','placeholder':'This is Message-body'}),
            'category' :forms.TextInput(attrs={'class': 'form-control','placeholder':'make your category'}),
        }

# class Commentform(forms.ModelForm):
#     class Meta:
#         model=Comment
#         fields={"name","comment"}
#
#         widgets = {
#             'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Your Name'}),
#             'comment': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Your Comment'}),
#         }