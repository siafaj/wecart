from django.contrib import admin

from store.models import Product

# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    list_display = ('product_name', 'price', 'stock', 'is_available', 'created_date', 'updated_date')
    prepopulated_fields = {'slug': ('product_name',)}
    list_filter = ('is_available', 'category')
    search_fields = ('product_name', 'description')

admin.site.register(Product, ProductAdmin)
