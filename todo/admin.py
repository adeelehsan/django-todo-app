from django.contrib import admin

from .models import Task


class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'status', 'creation_date', 'completion_date', 'log')
    list_filter = (
        ('user', admin.RelatedOnlyFieldListFilter),
        'status',
    )

    search_fields = ['title']

admin.site.register(Task, TaskAdmin)
