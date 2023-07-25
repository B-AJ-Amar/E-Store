from django.urls import path,include
from .views import *

urlpatterns = [
   
    path('', ProductsListView.as_view()),
    path('<int:id>/', ProductView.as_view()),
    

]