from django.contrib import admin
from import_export.admin import ImportExportModelAdmin

from . import models


@admin.register(models.Event)
class EventAdmin(ImportExportModelAdmin):
    horizontal_filter = ('visitors', )
