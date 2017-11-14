from django.contrib import admin
from .models import KszkEvent


@admin.register(KszkEvent)
class KszkEventAdmin(admin.ModelAdmin):
    list_display = ('date')
