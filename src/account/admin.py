from django.contrib import admin
from solo.admin import SingletonModelAdmin
from import_export.admin import ExportMixin

from . import models
from . import resources


@admin.register(models.Profile)
class ProfileAdmin(ExportMixin, admin.ModelAdmin):
    list_display = ('user_username', 'full_name', 'join_date')
    resource_class = resources.SignUpResource

    def user_username(self, obj):
        return obj.user.username

    user_username.admin_order_field = 'user__username'


# Register your models here.
admin.site.register(models.GroupChoice)
admin.site.register(models.Deadline, SingletonModelAdmin)
