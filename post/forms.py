from django import forms
from django_ckeditor_5.widgets import CKEditor5Widget

from post.models import Post

class PostForm(forms.ModelForm):
    
    class Meta:
        model = Post
        fields = ("title","content")
        
        widgets = {
            "content": CKEditor5Widget(
                attrs={"class": "django_ckeditor_5"}, config_name="extends"
            )
        }
