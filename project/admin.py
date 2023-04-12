from django.contrib import admin

from project.models import Project

# Register your models here.

class ProjectAdmin(admin.ModelAdmin):
    list_display = ("project_name", "status", "created_on", "updated_on",)
    search_fields = ("project_name", "description")
    prepopulated_fields = {"slug": ("project_name",)}
    list_filter = ("status", "created_on")

admin.site.register(Project, ProjectAdmin)