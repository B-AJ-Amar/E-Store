from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import BasicAuthentication
from rest_framework.views import APIView
from collections import OrderedDict

from .serializers import *
from .models import *

# Create your views here.

class OrderView(APIView):
    authentication_classes = (BasicAuthentication,)
    permission_classes     = (IsAuthenticated,)
    def get(self,request):
        orders = Order.objects.filter()
        if orders.exists():
            serializer = OrderSerializer(orders,many=True)
          
            return Response(serializer.data,status=200)
        else:
            return Response(status=404)
    def post(self,request):
        product_id = request.data.get("product_id")
        product_quantity = request.data.get("product_quantity")
        print("product id :>>>",product_id,product_quantity)
        try:
            if not  (product_id and product_quantity):
                return Response(status=400)
            product = Product.objects.get(pk=int(product_id))
            print("product ",product.name)
           
            order = Order.objects.filter(is_finished=False,user=request.user).first()
            print("order ",order.id)
            if not order:
                order = Order.objects.create(user=request.user)
            orderprod = OrderProd.objects.filter(order=order,product=product).first()
            print("orderprod ",orderprod.date)
            if orderprod:
                orderprod.quantity = product_quantity
                orderprod.save()
                print("saved if ",orderprod.date)
            else:
                orderprod = OrderProd.objects.create(order=order,product=product,quantity=product_quantity)
                orderprod.save()
                print("saved else ",orderprod.date)
            
            
            return Response(data={"order_id":orderprod.id,"product_id":product_id,"product_quantity":product_quantity},status=200)
          
        except:
            return Response(status=404)
      
      
class OrderProdView(APIView):
    authentication_classes = (BasicAuthentication,)
    permission_classes     = (IsAuthenticated,)
    def get(self,request):
        orders = OrderProd.objects.all()
        if orders.exists():
            serializer = OrderProdSerializer(orders,many=True)
          
            return Response(serializer.data,status=200)
        else:
            return Response(status=404)
      
    
       
            
           
