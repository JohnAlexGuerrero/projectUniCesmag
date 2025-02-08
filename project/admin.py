from django.contrib import admin

from post.models import Post, ProjectPost

# Register your models here.
@admin.register(ProjectPost)
class ProjectPostAdmin(admin.ModelAdmin):
    pass


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ["title","content"]
    fields = ["title","content","module"]


