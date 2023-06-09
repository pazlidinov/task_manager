from django.contrib import admin
from .models import *

# Register your models here.


@admin.register(Direction)
class DirectionAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {"slug": ('name',)}


@admin.register(Group)
class GroupAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {"slug": ('name',)}

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['name', 'family']