from rest_framework_simplejwt.views import TokenObtainPairView
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import *


class LogInView(TokenObtainPairView):
    def post(self, request, *args, **kwargs):
        
        print(request.data)
        user = User.objects.filter(email=request.data['email']).first()
        if user and not user.is_active:
            request.data['email']=""
            
        response = super().post(request, *args, **kwargs)

        # response.data['custom_data'] = ' custom data!'

        return response

class SignUpView(APIView):
    authentication_classes = ()
    permission_classes     = ()

    def post(self,request):
        serializer = SignUpSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=201)
        return Response(serializer.errors,status=400)
    
    
    