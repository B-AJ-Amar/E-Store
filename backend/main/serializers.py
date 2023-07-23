from rest_framework import serializers
from .models import *
import re
from django.utils import timezone



class SignUpSerializer(serializers.ModelSerializer):
    
    def validate(self, attr):
        
        # Use the regular expression pattern to check if the input contains at least one digit, one character, and one symbol
        password_pattern = r"(?=.*\d)(?=.*[a-zA-Z])(?=.*[^a-zA-Z\d]).+)"
        names_pattern = r"\A[A-Za-z\s]{3,}\Z"
        email_pattern = r"(@gmail|@yahoo|@hotmail|@univ|@icloud)"

        
        attr['email']  = str(attr['email']).strip().lower()
        if not bool(re.search(email_pattern, attr['email'])):
            raise serializers.ValidationError('wrong email')
        
        attr['first_name']  = str(attr['first_name']).strip().lower()
        if not bool(re.match(pattern=names_pattern, string=attr['first_name'])):
            raise serializers.ValidationError('wrong first name')
        
        attr['last_name']  = str(attr['last_name']).strip().lower()
        if not bool(re.match(names_pattern, attr['last_name'])):
            raise serializers.ValidationError('wrong last name')
        
        
        bd_year = str(attr['birthday']).split("-")[0]
        if timezone.now().year-int(bd_year)<18 :
            raise serializers.ValidationError('under 18 years old')
        
        
        # PASSWORD :=================================================
        if len( attr['password'])<8:
            raise serializers.ValidationError('wrong first name')
        
        if not bool(re.match(pattern=password_pattern, string=attr['password'])):
            raise serializers.ValidationError("password must contains at least one digit, one character, and one symbol.")
       
        
        return attr
    
    def create(self, validated_data):
        password = validated_data.pop('password')
        user = User(**validated_data)
        user.set_password(password)
        user.is_active = False
        user.save()
        ev = EmailVerification.objects.create(user_id=user)
        ev.create_key()
        ev.save()
        return user
    
    class Meta:
        model=User
        fields= ("id","first_name","last_name","gender","birthday","email","password")
        read_only_fields = ('id', )
        extra_kwargs = {
            'password': {'write_only': True}
        }