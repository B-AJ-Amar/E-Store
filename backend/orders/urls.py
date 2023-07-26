from django.urls import path,include
from .views import *

urlpatterns = [
#    path('', OrderProdView.as_view()),
    path('', OrderView.as_view()),
    

]