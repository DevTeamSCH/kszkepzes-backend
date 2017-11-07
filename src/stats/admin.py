from django.contrib import admin
from .models import Profile, KszkEvent


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user_username', 'year_of_join', 'pref_group')

    def user_username(self, obj):
        return obj.user.username

    user_username.admin_order_field = 'user__username'


@admin.register(KszkEvent)
class KszkEventAdmin(admin.ModelAdmin):
    list_display= ('date', 'num_of_pers')
