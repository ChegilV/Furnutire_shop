from django.db import models
from traitlets import default

from users.models import User
from goods.models import Products

class CartQueryset(models.QuerySet):
    
    def total_price(self):
        return sum(cart.product_price() for cart in self)

    def total_quantity(self):
        if self:
            return sum(cart.quantity for cart in self)
        return 0
    


class Cart(models.Model):
    user = models.ForeignKey(to=User, on_delete=models.CASCADE, blank=True, null=True, verbose_name='User')
    product = models.ForeignKey(to=Products, on_delete=models.CASCADE, verbose_name='Product')
    quantity = models.PositiveSmallIntegerField(default=0, verbose_name='quantity')
    session_key = models.CharField(max_length=32, null=True, blank=True)
    created_timestamp = models.DateTimeField(auto_now_add=True, verbose_name='Updated Data')

    class Meta:
        db_table = 'cart'
        verbose_name = 'Cart'
        verbose_name_plural = 'Carts'

    objects = CartQueryset().as_manager()

    def product_price(self):
        return round(self.product.sale_price() * self.quantity ,2)
    
    def __str__(self):
        return f'Cart {self.user.username} | Product {self.product.name} |Quanitity {self.quantity}'