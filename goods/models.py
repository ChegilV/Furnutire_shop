import decimal
from enum import unique
from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.
class Categories(models.Model):
    name = models.CharField(max_length=150, unique=True, verbose_name='name')
    slug = models.SlugField(max_length=200, unique=True, blank=True, null=True, verbose_name='URL')

    class Meta:
        db_table = 'category'
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name



class Products(models.Model):
    name = models.CharField(max_length=150, unique=True, verbose_name='name')
    slug = models.SlugField(max_length=200, unique=True, blank=True, null=True, verbose_name='URL')
    description = models.TextField(blank=True, null=True, verbose_name='description')
    image = models.ImageField(upload_to='goods_images', blank=True, null=True, verbose_name='image')
    price = models.DecimalField(default=0.00, max_digits=7, decimal_places=2, verbose_name='price')
    discount = models.DecimalField(default=0.00, max_digits=7, decimal_places=2, verbose_name='discount %')
    quantity = models.PositiveIntegerField(default=0, verbose_name='quantity')
    caategory = models.ForeignKey(to=Categories, on_delete=models.CASCADE)

    class Meta:
        db_table = 'product'
        verbose_name = 'product'
        verbose_name_plural = 'products'

    def __str__(self):
       return self.name