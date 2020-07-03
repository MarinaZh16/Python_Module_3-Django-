from django.contrib import admin
from . import models

# Register your models here.


class UserAdmin(admin.ModelAdmin):
    list_display = ['id', 'username', 'token']


admin.site.register(models.User, UserAdmin)
