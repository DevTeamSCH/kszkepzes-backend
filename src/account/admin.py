from django.contrib import admin
from .models import Profile


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user_username', 'join_date', 'pref_group')

    def user_username(self, obj):
        return obj.user.username

    user_username.admin_order_field = 'user__username'
# Register your models here.
