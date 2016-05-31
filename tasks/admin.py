from django.contrib import admin
from tasks import models


class TaskAdmin(admin.ModelAdmin):
    date_hierarchy = 'posted_at'
    list_display = (
        'id',
        'title',
        'status',
        'posted_at',
        'price',
    )
    fieldsets = (
        'id',
        'title',
        'message',
        'posted_by',
    )
    search_fields = (
        'id',
        'title',
    )
    fields = (
        'id',
        'title',
        'posted_by',
    )
    admin.site.register(models.Task)
