from django.contrib import admin
from import_export.admin import ExportMixin

from . import models
from . import resources


@admin.register(models.Event)
class EventAdmin(ExportMixin, admin.ModelAdmin):
    filter_horizontal = ('visitors', )
    resource_class = resources.EventResource
