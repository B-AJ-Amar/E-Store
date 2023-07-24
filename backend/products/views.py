from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import *
from .models import *

# Create your views here.


class ProductsList(APIView):
    authentication_classes = ()
    permission_classes     = ()
    def get(self,request):
        serializer = ProductSerializer(Product.objects.filter(is_active=True),many=True)
      
        return Response(serializer.data,status=200)
    
    def post(self,request):
        serializer = ProductSerializer(data=request.data,many=True)
        if serializer.is_valid():
            serializer.save()
        
