from django.urls import path
from .views import (UserCreateAPIView, ItemListAPIView,
    ItemDetailAPIView,
    ItemUpdateAPIView,
    ItemDeleteAPIView,
    ItemCreateAPIView)

from rest_framework_jwt.views import obtain_jwt_token

urlpatterns = [
    path('login/', obtain_jwt_token, name='login'),
    path('register/', UserCreateAPIView.as_view(), name='register'),
    path('api/list/', ItemListAPIView.as_view(), name='api-list'),
    path('api/create/', ItemCreateAPIView.as_view(), name='api-create'),
    path('api/<int:item_id>/detail/', ItemDetailAPIView.as_view(), name='api-detail'),
    path('api/<int:item_id>/update/', ItemUpdateAPIView.as_view(), name='api-update'),
    path('api/<int:item_id>/delete/', ItemDeleteAPIView.as_view(), name='api-delete'),
]