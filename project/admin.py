from django.contrib import admin

from project.models import Project

# Register your models here.

class ProjectAdmin(admin.ModelAdmin):
    list_display = ("project_name", "description",)
    prepopulated_fields = {"slug": ("project_name",)}

admin.site.register(Project, ProjectAdmin)