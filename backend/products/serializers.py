from rest_framework import serializers
from .models import *


class PhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model=Photo
        fields=['id','product_id','photo']
 
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model=Category
        fields=['id','name',]
               
class ProductSerializer(serializers.ModelSerializer):
    categories = CategorySerializer(many=True)
    photos = PhotoSerializer(many=True)
    class Meta:
        model=Product
        fields=['id','name','price','categories','photos']