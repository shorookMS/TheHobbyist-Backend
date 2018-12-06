from django.urls import path

#Imports for User login and Item API
from .views import (
	UserCreateAPIView,
	ProfileDetailAPIView, 
	ProfileUpdateAPIView,
	ItemListAPIView,
	ItemDetailAPIView,
	ItemCreateUpdateAPIView,  
	ItemStockUpdateAPIView,
	ItemCreateAPIView
	)
#Imports for Address API

from .views import ( 
	AddressListAPIView, 
	AddressCreateUpdateAPIView,  
	AddressDefaultUpdateAPIView,
	AddressCreateAPIView
	)

#Imports for Order API

from .views import ( 
	OrderListAPIView,
	OrderDetailAPIView, 
	OrderCreateAPIView,
	OrderStatusUpdateAPIView,
	OrderItemDetailAPIView,
	OrderItemCreateAPIView,
	OrderItemDeleteAPIView,
	OrderItemQuantityUpdateAPIView
	)

from rest_framework_jwt.views import obtain_jwt_token

urlpatterns = [
	path('login/', obtain_jwt_token, name='login'),
	path('register/', UserCreateAPIView.as_view(), name='register'),
	path('profile/', ProfileDetailAPIView.as_view(), name='api-profile-detail'),
	path('profile/<int:user_id>/update', ProfileUpdateAPIView.as_view(), name='api-profile-update'),
	# Item Url
	path('item/list/', ItemListAPIView.as_view(), name='api-item-list'),
	path('item/create/', ItemCreateAPIView.as_view(), name='api-item-create'),
	path('item/<int:item_id>/detail/', ItemDetailAPIView.as_view(), name='api-item-detail'),
	path('item/<int:item_id>/update/', ItemCreateUpdateAPIView.as_view(), name='api-item-update'),
	path('item/<int:item_id>/stock-update/', ItemStockUpdateAPIView.as_view(), name='api-item-stock-update'),
	# Address Urls
	path('address/list/', AddressListAPIView.as_view(), name='api-address-list'),
	path('address/create/', AddressCreateAPIView.as_view(), name='api-address-create'),
	path('address/<int:address_id>/update/', AddressCreateUpdateAPIView.as_view(), name='api-address-update'),
	path('address/<int:address_id>/default-update/', AddressDefaultUpdateAPIView.as_view(), name='api-address-default-update'),
	# Order Urls
	path('order/list/', OrderListAPIView.as_view(), name='api-order-list'),
	path('order/create/', OrderCreateAPIView.as_view(), name='api-order-create'),
	path('order/<int:order_id>/status-update/', OrderStatusUpdateAPIView.as_view(), name='api-order-status-update'),
	path('order/<int:order_id>/detail/', OrderDetailAPIView.as_view(), name='api-order-detail'),

	# Order Item Urls
	path('orderitem/create/', OrderItemCreateAPIView.as_view(), name='api-orderitem-create'),
	path('orderitem/<int:orderitem_id>/detail/', OrderItemDetailAPIView.as_view(), name='api-orderitem-detail'),
	path('orderitem/<int:orderitem_id>/delete/', OrderItemDeleteAPIView.as_view(), name='api-orderitem-delete'),
	path('orderitem/<int:orderitem_id>/quantity-update/', OrderItemQuantityUpdateAPIView.as_view(), name='api-orderitem-quantity-update'),


]