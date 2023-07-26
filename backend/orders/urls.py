from django.urls import path,include
from .views import *

urlpatterns = [
#    path('', OrderProdView.as_view()),
    path('', OrderView.as_view()),
    path('details/<int:id>', OrderDetailsView.as_view()),
    path('details/', OrderProdView.as_view()),
    

]