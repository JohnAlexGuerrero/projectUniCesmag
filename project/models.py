from django.db import models

from django.shortcuts import get_object_or_404
from django.urls import reverse

from django_ckeditor_5.fields import CKEditor5Field

from post.models import Post, ProjectPost

# Create your models here.

class Project(models.Model):
    title = models.CharField(("titulo"), max_length=150, unique=True, null=False)
    description = CKEditor5Field('descrición', config_name='extends')
    version = models.CharField(("version"), max_length=10, null=True, blank=True)

    class Meta:
        verbose_name = ("Project")
        verbose_name_plural = ("Projects")

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("detail", kwargs={"pk": self.pk})

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        
        for post in Post.objects.all():
            obj, obj_created = ProjectPost.objects.get_or_create(
                    title=post.title, 
                    defaults={'project':self, 'title':post.title, 'content': post.content, 'module': post.module}
                )
            
            if obj_created:
                print(obj_created)
            else:
                print(f"{obj} it´s exist...")
            
        return f"saved..."