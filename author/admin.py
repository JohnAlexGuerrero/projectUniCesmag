from django.contrib import admin

from author.models import Organization, Participant
# Register your models here.

@admin.register(Organization)
class OrganizationAdmin(admin.ModelAdmin):
    pass

@admin.register(Participant)
class ParticipantAdmin(admin.ModelAdmin):
    pass

