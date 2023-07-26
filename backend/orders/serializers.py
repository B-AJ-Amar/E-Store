from rest_framework import serializers
from .models import *
from products.models import *

# ! i have problem here i cant serialize quantity and date   
class OrderProdSerializer(serializers.ModelSerializer):
    # product_name = serializers.CharField( source='name')
    product_price= serializers.DecimalField(max_digits=20,decimal_places=2,source='price')
    # total_price = serializers.SerializerMethodField()
    class Meta:
        model=OrderProd
        fields=["id","product_price","quantity","date","total_price"]
        read_only_fields = ('id', "quantity")
        
    def get_total_price(self, instance):
        return instance.total_price()
    

class OrderSerializer(serializers.ModelSerializer):
    
    details = OrderProdSerializer(many=True)
    class Meta:
        model=Order
        fields=["id","details","created_date","order_date"]
        read_only_fields = ('id', )
        