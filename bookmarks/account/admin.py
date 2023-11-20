from django.contrib import admin

from .models import Profile, Categories


# Register your models here.
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'date_of_birth', 'photo']
    raw_id_fields = ['user']


class CategoriesAdmin(admin.ModelAdmin):
    list_display = ['name']
    search_fields = ['name']


admin.site.register(Profile, ProfileAdmin)
admin.site.register(Categories)
