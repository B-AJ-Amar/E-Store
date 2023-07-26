from django.db import models
from django.utils import timezone
from products.models import Product

# Create your models here.


class Order(models.Model):
    # id
    user         = models.ForeignKey("main.User", on_delete=models.CASCADE)
    details      = models.ManyToManyField(Product, through="OrderProd")
    created_date = models.DateTimeField(default=timezone.now)
    order_date   = models.DateTimeField(null=True,blank=True)
    is_finished  = models.BooleanField(default=False)
    
    def total_price(self,user):
        total = 0
        for det in OrderProd.objects.filter(user=user,order=self):
            total += det.quantity*det.product.price
        return total
    
class OrderProd(models.Model):
    product      = models.ForeignKey(Product, on_delete=models.CASCADE)
    order        = models.ForeignKey(Order  ,  on_delete=models.CASCADE)
    quantity     = models.IntegerField(default=0)
    date         = models.DateTimeField(default=timezone.now)
    # @property
    def total_price(self):
        return self.quantity*float(self.product.price)
    @property
    def pdoduct_name(self):
        return self.product.username