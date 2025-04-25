from django.contrib import admin

from software.models import Objective, App, Requeriment
# Register your models here.

@admin.register(Objective)
class ObjectiveAdmin(admin.ModelAdmin):
    pass

@admin.register(App)
class AppAdmin(admin.ModelAdmin):
    pass


@admin.register(Requeriment)
class RequerimentAdmin(admin.ModelAdmin):
    pass
