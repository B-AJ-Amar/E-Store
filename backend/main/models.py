from django.db import models
from django.contrib.auth.models import AbstractBaseUser,BaseUserManager,PermissionsMixin
from django.utils import timezone
import os,random,string




class UserManager(BaseUserManager):
    def create_user(self , first_name,last_name,email,gender,birthday, password):
        user = self.model(first_name=first_name,last_name=last_name,email=email,birthday=birthday,gender=gender)
        
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self ,password, first_name=None,last_name=None,email=None,gender=None,birthday=None ):
        user = self.model(first_name=first_name,last_name=last_name,email=email,birthday=birthday,gender=gender)
        user.is_admin         = True
        user.is_staff         = True
        user.is_superuser     = True
        user.verified_badge   = True
        user.set_password(password)
        user.save(using=self._db)
        return user
        



def get_image_upload_path(instance, filename):
    id = instance.id
    return os.path.join('profilephotos', str(id), str(filename))

class User(AbstractBaseUser,PermissionsMixin):
    first_name           = models.CharField(max_length=50,blank=True)
    last_name           = models.CharField(max_length=50,blank=True)
    email                = models.EmailField(unique=True,max_length=320,blank=True)
    photo                = models.ImageField(upload_to= get_image_upload_path,default='user_photos/user_default.png')
    join_date            = models.DateTimeField(default=timezone.now)
    gender               = models.BooleanField(blank=True)
    birthday             = models.DateField(blank=True)
 
    is_active            = models.BooleanField(default=True)
    is_superuser         = models.BooleanField(default=False)
    is_admin             = models.BooleanField(default=False)
    is_staff             = models.BooleanField(default=False)
    is_privite           = models.BooleanField(default=False)
    # last_login
    # password 
    
    objects = UserManager()
    
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS =[  ]
    
    def __str__(self) -> str:
        return f"{self.id} {self.first_name} {self.last_name}"
    
    
"""this table for verify the email. serification link will be accounts/signup/verify/user.KEY"""
class EmailVerification(models.Model):
    user_id = models.ForeignKey("main.User", on_delete=models.CASCADE)
    key     = models.CharField(max_length=50) # a random str 
    
    def create_key(self):     
        self.key = random.choices(list(string.ascii_lowercase+string.digits),k=50)
        
    

    
