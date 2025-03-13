from django.contrib import admin
from .models import *


@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    list_display = ('order', 'name', 'zoom', 'status')
    list_display_links = ('name',)
    list_editable = ('order', 'zoom', 'status')
    search_fields = ('name',)


@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_display = ('order', 'name', 'brand', 'manufacture_year', 'price', 'is_featured', 'status')
    list_display_links = ('name',)
    list_editable = ('order', 'is_featured', 'status')
    list_filter = ('brand', 'engine_type', 'drive_unit', 'speed_in', 'status')
    search_fields = ('name',)
    autocomplete_fields = ('brand', 'equipments', 'engine_type', 'drive_unit')
    date_hierarchy = 'date'


@admin.register(Car_color)
class Car_colorAdmin(admin.ModelAdmin):
    list_display = ('car', 'order', 'color_1', 'color_2', 'status')
    list_display_links = ('car',)
    list_editable = ('order', 'color_1', 'color_2', 'status')
    list_filter = ('car', 'status')
    search_fields = ('color_1', 'color_2')
    autocomplete_fields = ('car',)


@admin.register(Car_image)
class Car_imageAdmin(admin.ModelAdmin):
    list_display = ('order', 'car', 'image_types_list', 'status')
    list_display_links = ('car',)
    list_editable = ('order', 'status')
    list_filter = ('car', 'status')
    autocomplete_fields = ('car', 'image_types')
