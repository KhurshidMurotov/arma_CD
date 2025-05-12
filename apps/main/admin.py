from django.contrib import admin
from .models import Brand, Car, CarColor, CarImage  # Explicit imports


@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    list_display = ('order', 'name', 'zoom', 'status')
    list_display_links = ('name',)
    list_editable = ('order', 'zoom', 'status')
    search_fields = ('name',)
    list_per_page = 50


@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_display = (
        'order', 
        'name', 
        'brand', 
        'manufacture_year', 
        'formatted_price',
        'is_featured', 
        'status'
    )
    list_display_links = ('name',)
    list_editable = ('order', 'is_featured', 'status')
    list_filter = (
        'brand', 
        'engine_type', 
        'drive_unit', 
        'speed_in', 
        'status',
        'is_featured'
    )
    search_fields = ('name', 'brand__name')
    autocomplete_fields = ('brand', 'equipments', 'engine_type', 'drive_unit')
    date_hierarchy = 'date'
    list_select_related = ('brand',)
    list_per_page = 30

    def formatted_price(self, obj):
        return f"${obj.price:,.2f}"
    formatted_price.short_description = 'Price'


@admin.register(CarColor)
class CarColorAdmin(admin.ModelAdmin):
    list_display = (
        'car', 
        'order', 
        'color_1', 
        'color_2', 
        'status'
    )
    list_display_links = ('car',)
    list_editable = ('order', 'color_1', 'color_2', 'status')
    list_filter = ('car__brand', 'status')
    search_fields = ('color_1', 'color_2', 'car__name')
    autocomplete_fields = ('car',)
    list_select_related = ('car', 'car__brand')
    list_per_page = 50


@admin.register(CarImage)
class CarImageAdmin(admin.ModelAdmin):
    list_display = (
        'order', 
        'car', 
        'image_preview',
        'status'
    )
    list_display_links = ('car',)
    list_editable = ('order', 'status')
    list_filter = ('car__brand', 'status', 'image_type')
    autocomplete_fields = ('car', 'image_type')
    list_select_related = ('car', 'image_type')
    list_per_page = 30
    readonly_fields = ('image_preview',)

    def image_preview(self, obj):
        from django.utils.html import format_html
        return format_html(
            '<img src="{}" style="max-height: 50px;" />', 
            obj.image.url
        ) if obj.image else '-'
    image_preview.short_description = 'Preview'