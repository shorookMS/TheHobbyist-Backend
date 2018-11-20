from django.urls import path
from .views import (UserCreateAPIView, ItemListAPIView,
    ItemDetailAPIView,ItemCreateUpdateAPIView,  ItemStockUpdateAPIView,ItemCreateAPIView)

from rest_framework_jwt.views import obtain_jwt_token

urlpatterns = [
    path('login/', obtain_jwt_token, name='login'),
    path('register/', UserCreateAPIView.as_view(), name='register'),
    path('list/', ItemListAPIView.as_view(), name='api-list'),
    path('create/', ItemCreateAPIView.as_view(), name='api-create'),
    path('<int:item_id>/detail/', ItemDetailAPIView.as_view(), name='api-detail'),
    path('<int:item_id>/update/', ItemCreateUpdateAPIView.as_view(), name='api-update'),
    path('<int:item_id>/stock-update/', ItemStockUpdateAPIView.as_view(), name='api-stock-update'),
    # path('api/<int:item_id>/delete/', ItemDeleteAPIView.as_view(), name='api-delete'),
]