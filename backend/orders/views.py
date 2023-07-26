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
        orders = Order.objects.all()
        if orders.exists():
            serializer = OrderSerializer(orders,many=True)
          
            return Response(serializer.data,status=200)
        else:
            return Response(status=404)
    def post(self,request):
        product_id = request.data.get("product_id")
        product_quantity = request.data.get("product_quantity")
        try:
            if product_quantity<0 or not isinstance(product_quantity, int) or not isinstance(product_id, int) or not (product_id and product_quantity):
                return Response(status=400)
            print("validated done",product_id,product_quantity)
            product = Product.objects.get(id=product_id)
            print("prduct done")
           
            order = Order.objects.filter(is_finished=False,user=request.user).first()
            if not order:
                order = Order.objects.create(user=request.user)
                print("order created ")
            print("order done")
            orderprod = OrderProd.objects.filter(order=order,product=product).first()
            print("orderprod done")
            if orderprod:
                orderprod.quantity = product_quantity
                orderprod.save()
                print("updated done")
            else:
                orderprod = OrderProd.objects.create(order=order,product=product,quantity=product_quantity)
                orderprod.save()
                print("created done")
            return Response(data={"order_id":orderprod.id,"product_id":product_id,"product_quantity":product_quantity},status=200)
        except:
            return Response(status=404)

class OrderDetailsView(APIView):
    authentication_classes = (BasicAuthentication,)
    permission_classes     = (IsAuthenticated,)
    def get(self,request,id):
        # try:
            print("ordest")
            order = order = Order.objects.get(is_finished=False,user=request.user)
            print("ordest", order.id)
            orders = OrderProd.objects.get(order=order,product=Product.objects.get(id=id))
            print("ordest")
            serializer = OrderProd2Serializer(orders)
            return Response(serializer.data,status=200)
            
        # except :
        #     return Response(status=404)
        
    def put(self,request,id):
        product_quantity = request.data.get("product_quantity")
        try:
            if product_quantity<0 or not isinstance(product_quantity, int) or  not (id and product_quantity):
                return Response(status=400)
            product = Product.objects.get(pk=int(id))
           
            order = Order.objects.filter(is_finished=False,user=request.user).first()
            if not order:
                return Response(status=404)
            orderprod = OrderProd.objects.filter(order=order,product=product).first()
            if orderprod:
                orderprod.quantity = product_quantity
                orderprod.save()
            else:
                return Response(status=404)
            return Response(data={"order_id":orderprod.id,"product_id":id,"product_quantity":product_quantity},status=200)
        except:
            return Response(status=404)
        
    def delete(self,request,id):
        # product_id = request.data.get("product_id")
        # product_quantity = request.data.get("product_quantity")
        try:
            print("id : ",id)
            product = Product.objects.get(id=int(id))
            print("droduct : ",product.name)
            order = Order.objects.get(is_finished=False,user=request.user)
            print("order : ",order.id)
            orderprod = OrderProd.objects.filter(order=order,product=product).delete()
            print(order,orderprod,product)
            # orderprod.save()
            return Response(status=202)
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
      
    
       
            
           
