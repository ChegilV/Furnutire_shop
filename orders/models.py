from django.db import models
from traitlets import default
from users.models import User
from goods.models import Products
# Create your models here.
class OrderitemQueryset(models.QuerySet):
    def totla_price(self):
        return sum(cart.products_price() for cart in self)
    
    def total_quantity(self):
        if self:
            return sum(cart.quantity for cart in self)
    

class Order(models.Model):
    user = models.ForeignKey(to=User, on_delete=models.SET_DEFAULT, verbose_name='User', blank=True, null=True, default=None)
    created_timestamp = models.DateTimeField(auto_now_add=True, verbose_name='Data of creation')
    phone_number = models.CharField(default=False, verbose_name='Number of phone')
    requires_delivery = models.BooleanField(default=False, verbose_name='Need a delivery')
    delivery_address = models.TextField(null=True, blank=True, verbose_name='address of delivery')
    payment_on_get = models.BooleanField(default=False, verbose_name= 'Payment')
    is_paid = models.BooleanField(default=False, verbose_name='Payed')
    status = models.CharField(max_length=50, default='in processing', verbose_name='Status of order')

    class Meta:
        db_table = 'order'
        verbose_name = 'Order'
        verbose_name_plural = 'Orders'

        def __str__(self):
            return f'Order № {self.pk} | Customer {self.user.first_name} {self.user.last_name}'
        


class OrderItem(models.Model):
    order = models.ForeignKey(to=Order, on_delete=models.CASCADE, verbose_name='Order')
    product = models.ForeignKey(to=Products, on_delete=models.SET_DEFAULT, verbose_name='Product', null=True, default=None)
    name = models.CharField(max_length=150, verbose_name='Name')
    price = models.DecimalField(max_digits=7, decimal_places=2, verbose_name='Price')
    quantity = models.PositiveBigIntegerField(default=0, verbose_name='Quantity')
    created_timestamp = models.DateTimeField(auto_now_add=True, verbose_name='Data of sell')

    class Meta:
        db_table = 'order_item'
        verbose_name = 'Sold product'
        verbose_name_plural = 'Sold products'

    objects = OrderitemQueryset.as_manager()

    def products_price(self):
        return round(self.product.sale_price() * self.quantity, 2)

    def __str__(self):
        return f'Product {self.name} | Order № {self.order.pk}' 