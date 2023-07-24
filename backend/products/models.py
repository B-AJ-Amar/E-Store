from django.db import models
from django.utils import timezone
import os

# # Create your models here.

    
def get_photo_upload_path(instance, filename):
    id = instance.product.id
    return os.path.join('product-photos', str(id), str(filename))

class Photo(models.Model):
    #id
    product           = models.ForeignKey("products.Product",related_name="poduct_p",  on_delete=models.CASCADE)
    photo             = models.ImageField(upload_to= get_photo_upload_path)
    def __str__(self):
        return f"{self.product.name}"
   
class Category(models.Model):
    # id
    name                = models.CharField(max_length=100,unique=True)
    class Meta:
        ordering = ["name"]
    def __str__(self) :
        # return f"{self.name} {self.Product.name}"
        return f"{self.id}-{self.name}"
    
class Product(models.Model):
    name                 = models.CharField(max_length=100, blank=True, null=True)
    description          = models.TextField( blank=True, null=True)
    created_date         = models.DateTimeField(default=timezone.now)
    stock_quantity       = models.IntegerField(default=0)
    price                = models.DecimalField(max_digits=6,decimal_places=2)
    categores            = models.ManyToManyField(Category, related_name='prodcuts', blank=True)
    is_active            = models.BooleanField(default=True)
    def __str__(self) -> str:
        return f"{self.id}-{self.name}"
    


