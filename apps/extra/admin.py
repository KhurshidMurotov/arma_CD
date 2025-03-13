from django.contrib import admin
from .models import *


@admin.register(Engine_type)
class Engine_typeAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug_name')
    list_display_links = ('name',)
    search_fields = ('name',)


@admin.register(Drive_unit)
class Drive_unitAdmin(admin.ModelAdmin):
    list_display = ('order', 'name')
    list_display_links = ('name',)
    list_editable = ('order',)
    search_fields = ('name',)


@admin.register(Equipment)
class EquipmentAdmin(admin.ModelAdmin):
    list_display = ('order', 'name', 'status')
    list_display_links = ('name',)
    list_editable = ('order', 'status')
    list_filter = ('status',)
    search_fields = ('name',)


@admin.register(Image_type)
class Image_typeAdmin(admin.ModelAdmin):
    list_display = ('order', 'name', 'slug_name')
    list_display_links = ('name',)
    list_editable = ('order',)
    search_fields = ('name',)
