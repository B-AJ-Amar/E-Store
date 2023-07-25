from rest_framework import serializers
from .models import *
import re
import base64

from django.core.files.base import ContentFile
from rest_framework import serializers


# def convert_to_img(data,uid,filename):
#     if isinstance(data, str) and data.startswith('data:image'):
#         # base64 encoded image - decode
#         format, imgstr = data.split(';base64,')  # format ~= data:image/X,
#         ext = format.split('/')[-1]  # guess file extension
        
#         filename=f'media/product-photos/{uid}/{filename}.{ext}'
#         imgdata = base64.b64decode(imgstr)
#         with open(filename, 'wb') as f:
#             f.write(imgdata)
#         return f'product-photos/{uid}/{filename}.{ext}'

class PhotoSerializer(serializers.ModelSerializer):
    photo  = serializers.CharField(max_length=1000)
    # name  = serializers.CharField(max_length=500)
    class Meta:
        model=Photo
        fields=['photo']
        read_only_fields = ('id', )
        # extra_kwargs = {'photo': {'validators': []},
        #                 # 'name': {'write_only': True}
        #                 }
 
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model=Category
        fields="__all__"
        # read_only_fields = ('name', )
        # extra_kwargs = {'name': {
        #         'validators': []
        #     }}
            
        
        
  
        
               
class ProductSerializer(serializers.ModelSerializer):
    categores = CategorySerializer(many=True, required=False)
    photos = PhotoSerializer(source='poduct_p',many=True)
    
    def create(self, validated_data):
        ctegories = validated_data["categores"]
        photos = validated_data["poduct_p"]
        del validated_data["categores"]
        del validated_data["poduct_p"]
        product = Product.objects.create(**validated_data)
        product.save()
        # add catgories=============================================
        for c in ctegories:    
            keys =  list(c.keys())
            if "id" in keys:
                try:
                    ct = Category.objects.get(id=c["id"])
                    product.categores.add(ct)
                except:pass
            elif "name" in keys:
                try:
                    ct = Category.objects.get(name=c["name"])
                    product.categores.add(ct)
                except:pass 
        # add photos ================================================
        # for p in photos:
        #     keys =  list(p.keys())
        #     if "photo" in keys:
        #         # fn = convert_to_img(p['photo'],str(product.id),"a")
                
        #         cp = Photo.objects.create(photo='../a.png',product=product)
        #         cp.save()
        
    
        return product
    
    
    def validate(self,attr):
        names_pattern = r"\A[A-Za-z\d\s]{3,}\Z"
        if attr['stock_quantity']<0:
            raise serializers.ValidationError('stock_quantity must be >= 0')
        
        if float(attr['price'])<0:
            raise serializers.ValidationError('price must be >= 0')
        
        if not bool(re.match(pattern=names_pattern, string=attr['name'])):
            raise serializers.ValidationError('name must contains only characters digits and spaces')
        
        return attr
        
        
        
        
    class Meta:
        model=Product
        # fields="__all__"
        fields = ["id","name","stock_quantity","price","categores","photos",]
        read_only_fields = ('id', )
        # extra_kwargs = {'categores': {'required': False}}
        extra_kwargs = {'photo': {
                'validators': []
            }}
         
         
         