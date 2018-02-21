from django.contrib import admin
from import_export.admin import ExportMixin

from . import models
from . import resources


@admin.register(models.Event)
class EventAdmin(ExportMixin, admin.ModelAdmin):
    filter_horizontal = ('visitors', )
    resource_class = resources.EventResource


@admin.register(models.Note)
class NoteAdmin(ExportMixin, admin.ModelAdmin):
    list_display = ('user', 'note', 'event', 'created_by', 'created_at', 'updated_at')
    list_filter = ('user', 'created_by', 'event')
    resource_class = resources.NoteResource
