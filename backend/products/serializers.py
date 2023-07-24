from rest_framework import serializers
from .models import *


class PhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model=Photo
        fields=['id','photo']
 
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model=Category
        fields="__all__"
               
class ProductSerializer(serializers.ModelSerializer):
    categores = CategorySerializer(many=True)
    photos = PhotoSerializer(source='poduct_p',many=True, read_only=True)
    class Meta:
        model=Product
        fields="__all__"
        fields = ["id","name","stock_quantity","price","categores","photos",]