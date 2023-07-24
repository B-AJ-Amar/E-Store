from django.urls import path,include
from .views import *

urlpatterns = [
   
    path('', ProductsList.as_view()),
    

]