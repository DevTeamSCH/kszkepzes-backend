from django.contrib import admin
from import_export.admin import ExportMixin

from . import models
from . import resources


@admin.register(models.Event)
class EventAdmin(ExportMixin, admin.ModelAdmin):
    filter_horizontal = ('visitors', )
    list_filter = ('name', 'date')
    search_fields = ('name', )
    resource_class = resources.EventResource


@admin.register(models.Note)
class NoteAdmin(ExportMixin, admin.ModelAdmin):
    list_display = ('profile', 'note', 'event', 'created_by', 'created_at', 'updated_at')
    list_filter = ('profile', 'created_by', 'event')
    search_fields = ('event__name', 'note')
    resource_class = resources.NoteResource
