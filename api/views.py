from .models import Item
from rest_framework.generics import (
    ListAPIView,
    RetrieveAPIView,
    RetrieveUpdateAPIView,
    DestroyAPIView,
    CreateAPIView,
)
from .serializers import UserCreateSerializer, ItemListViewSerializer, DetailViewSerializer, OrderViewSerializer

class UserCreateAPIView(CreateAPIView):
    serializer_class = UserCreateSerializer

class ListAPIView(RetrieveAPIView):
    serializer_class = ItemListViewSerializer

class DetailAPIView(RetrieveAPIView):
    serializer_class = DetailViewSerializer

class OrderAPIView(RetrieveAPIView):
    serializer_class = OrderViewSerializer

