from django.contrib import admin
from .models import Product, Category, ItemCategory, ItemProduct


class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'category',
        'price',
        'description',
        'image',
        'inStock',
    )

admin.site.register(ItemProduct, ProductAdmin)

class CategoryAdmin(admin.ModelAdmin):
     list_display = (
        'slug',
        'name',
    )


admin.site.register(ItemCategory, CategoryAdmin)



