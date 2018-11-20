from django.urls import path

#Imports for User login and Item API
from .views import (
    UserCreateAPIView, 
    ItemListAPIView,
    ItemDetailAPIView,
    ItemCreateUpdateAPIView,  
    ItemStockUpdateAPIView,
    ItemCreateAPIView)
#Imports for Address API

from .views import ( 
    AddressListAPIView,
    AddressDetailAPIView, 
    AddressCreateUpdateAPIView,  
    AddressDefaultUpdateAPIView,
    AddressCreateAPIView)

from rest_framework_jwt.views import obtain_jwt_token

urlpatterns = [
    path('login/', obtain_jwt_token, name='login'),
    path('register/', UserCreateAPIView.as_view(), name='register'),
    path('list/', ItemListAPIView.as_view(), name='api-list'),
    path('create/', ItemCreateAPIView.as_view(), name='api-create'),
    path('<int:item_id>/detail/', ItemDetailAPIView.as_view(), name='api-detail'),
    path('<int:item_id>/update/', ItemCreateUpdateAPIView.as_view(), name='api-update'),
    path('<int:item_id>/stock-update/', ItemStockUpdateAPIView.as_view(), name='api-stock-update'),
    #Address Urls
    path('address/list/', AddressListAPIView.as_view(), name='api-address-list'),
    path('address/create/', AddressCreateAPIView.as_view(), name='api-create'),
    path('address/<int:address_id>/detail/', AddressDetailAPIView.as_view(), name='api-address-detail'),
    path('address/<int:address_id>/update/', AddressCreateUpdateAPIView.as_view(), name='api-address-update'),
    path('address/<int:address_id>/default-update/', AddressDefaultUpdateAPIView.as_view(), name='api-address-default-update'),
    # path('api/<int:item_id>/delete/', ItemDeleteAPIView.as_view(), name='api-delete'),
]