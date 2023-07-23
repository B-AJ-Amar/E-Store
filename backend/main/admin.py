from django.contrib.auth.admin import UserAdmin
from .models import User
from django.contrib import admin
from django.contrib.auth import get_user_model

from orders.models import *
from products.models import *

User = get_user_model()

class UserAdmin(UserAdmin):
    list_display = ('first_name',"last_name", 'email', 'gender', 'birthday', 'is_active',"is_admin","is_superuser","is_staff")
    list_filter = ( 'email',)
    readonly_fields = ('join_date',)
    
    ordering = ('email',)
    
    filter_horizontal = ()
    filter_vertical = ()
    fieldsets = ()
    

admin.site.register(User, UserAdmin)
admin.site.register(Product)
admin.site.register(Photo)
admin.site.register(Order)
admin.site.register(OrderProd)
admin.site.register(Category)