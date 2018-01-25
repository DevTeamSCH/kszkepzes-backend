from django.contrib import admin
from . import models
from solo.admin import SingletonModelAdmin


@admin.register(models.Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user_username', 'join_date')

    def user_username(self, obj):
        return obj.user.username

    user_username.admin_order_field = 'user__username'


# Register your models here.
admin.site.register(models.GroupChoice)
admin.site.register(models.Deadline, SingletonModelAdmin)
