from django.contrib import admin

from .models import Task, Category


class TaskAdmin(admin.ModelAdmin):
    fields = ["title", "description", "completed"]

admin.site.register(Task, TaskAdmin)
admin.site.register(Category)