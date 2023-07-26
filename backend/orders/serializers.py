from rest_framework import serializers
from .models import *
from products.models import *


class OrderProdSerializer(serializers.ModelSerializer):
   
    product_name = serializers.CharField( source='product.name')
    product_price = serializers.CharField( source='product.price')
    class Meta:
        model=OrderProd
        fields=["id","order","quantity","date","product","product_name","product_price"]
        read_only_fields = ('id', "quantity")
        
    # def get_total_price(self, instance):
    #     return instance.total_price()

class OrderSerializer(serializers.ModelSerializer):
    
    details = OrderProdSerializer(many=True,read_only=True, source='orderprod_set')
    # orderprod = serializers.PrimaryKeyRelatedField(queryset=OrderProd.objects.all())
    class Meta:
        model=Order
        fields=["id","details","created_date","order_date"]
        read_only_fields = ('id', )
        