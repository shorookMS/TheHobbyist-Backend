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

class ItemListAPIView(RetrieveAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemListSerializer
    # permission_classes = [AllowAny,]
    # filter_backends = [OrderingFilter, SearchFilter,]
    # search_fields = ['name', 'description', 'owner__username']

class DetailAPIView(RetrieveAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemDetailSerializer
    lookup_field = 'id'
    lookup_url_kwarg = 'item_id'
    # permission_classes = [AllowAny,]

class ItemCreateAPIView(CreateAPIView):
    serializer_class = ItemCreateUpdateSerializer
    # permission_classes = [IsAuthenticated,]

    # def perform_create(self, serializer):
    #     serializer.save(owner=self.request.user)

class ItemUpdateAPIView(RetrieveUpdateAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemCreateUpdateSerializer
    lookup_field = 'id'
    lookup_url_kwarg = 'item_id'
    # permission_classes = [IsAuthenticated,IsOwner]

class ItemDeleteAPIView(DestroyAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemListSerializer
    lookup_field = 'id'
    lookup_url_kwarg = 'item_id'
    # permission_classes = [IsAuthenticated,IsAdminUser]

class OrderAPIView(RetrieveAPIView):
    serializer_class = OrderViewSerializer
