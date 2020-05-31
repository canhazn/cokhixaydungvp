from django.contrib import admin

# Register your models here.

from .models import Service
from django_summernote.admin import SummernoteModelAdmin

class ServiceAdmin(SummernoteModelAdmin):
    summernote_fields = ('content',)
    list_display = ('title', 'slug', 'date_created')
    prepopulated_fields = { 'slug': ('title', )}

admin.site.register(Service, ServiceAdmin)