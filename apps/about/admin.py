from django.contrib import admin
from .models import *
from django_summernote.models import Attachment


admin.site.unregister(Attachment)


@admin.register(About)
class AboutAdmin(admin.ModelAdmin):
    list_display = ('name', 'address', 'working_time', 'phone_number')
    list_display_links = ('name',)
    search_fields = ('name',)


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone_number', 'car', 'time')
    list_display_links = ('name',)
    list_filter = ('car',)
    search_fields = ('name',)
    autocomplete_fields = ('car',)
