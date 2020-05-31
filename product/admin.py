from django.contrib import admin

# Register your models here.

from .models import Product
from django_summernote.admin import SummernoteModelAdmin

class ProductAdmin(SummernoteModelAdmin):
    summernote_fields = ('content',)
    list_display = ('title', 'slug', 'date_created')
    prepopulated_fields = { 'slug': ('title', )}

admin.site.register(Product, ProductAdmin)