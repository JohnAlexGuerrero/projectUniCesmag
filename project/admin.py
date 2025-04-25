from django.contrib import admin

from post.models import Post, ProjectPost
from project.models import Project
from component.models import Component

# Register your models here.
@admin.register(ProjectPost)
class ProjectPostAdmin(admin.ModelAdmin):
    pass


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ["title","content"]
    fields = ["title","content","module"]


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    pass

@admin.register(Component)
class ComponentAdmin(admin.ModelAdmin):
    pass
