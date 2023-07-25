from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import *
from .models import *

# Create your views here.


class ProductsListView(APIView):
    authentication_classes = ()
    permission_classes     = ()
    def get(self,request):
        serializer = ProductSerializer(Product.objects.filter(is_active=True),many=True)
      
        return Response(serializer.data,status=200)
    
    # def post(self,request):
    #     serializer = ProductSerializer(data=request.data)
    #     print(f"data : {request.data}\nfiiles : {request.FILES}")
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(status=201)
    #     return Response(serializer.errors,status=400)
    
            
class ProductView(APIView):
    authentication_classes = ()
    permission_classes     = ()
    def get(self,request,id):
        print("id :>>>",id)
        try:
            pr = Product.objects.get(id=id,is_active=True)
            serializer = ProductSerializer(pr)
            return Response(serializer.data,status=200)
        except:
            return Response(serializer.data,status=404)
           
