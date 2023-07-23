from django.db import models
from django.utils import timezone
from products.models import Product

# Create your models here.


class Order(models.Model):
    # id
    user_id      = models.ForeignKey("main.User", on_delete=models.CASCADE)
    details      = models.ManyToManyField(Product, through="OrderProd")
    created_date = models.DateTimeField(default=timezone.now)
    order_date   = models.DateTimeField()
    is_finished  = models.BooleanField(default=False)
    
    
class OrderProd(models.Model):
    product_id  = models.ForeignKey(Product, on_delete=models.CASCADE)
    order_id    = models.ForeignKey(Order  ,  on_delete=models.CASCADE)
    quantity    = models.IntegerField(default=0)