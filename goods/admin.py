from django.contrib import admin
from goods import models
# Register your models here.

# admin.site.register(models.Categories)
# admin.site.register(models.Products)


@admin.register(models.Categories)
class CategoriesAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
    list_display = ['name',]


@admin.register(models.Products)
class ProductsAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
    list_display = ['name', 'quantity', 'price', 'discount']
    list_editable = ['discount', ]
    search_fields = ['name', 'description']
    list_filter = ['discount', 'quantity', 'caategory']
    fields = [
        'name', 
        'caategory',
        'slug',
        'description',
        'image',
        ('price', 'discount'),
        'quantity',
    ]
