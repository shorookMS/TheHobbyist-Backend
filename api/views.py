from .models import Item
from rest_framework.generics import (
	ListAPIView,
	RetrieveAPIView,
	RetrieveUpdateAPIView,
	DestroyAPIView,
	CreateAPIView,
)
from .serializers import (UserCreateSerializer, ItemListViewSerializer, ItemDetailViewSerializer, ItemCreateUpdateSerializer, ItemStockUpdateSerializer)

class UserCreateAPIView(CreateAPIView):
	serializer_class = UserCreateSerializer

class ItemListAPIView(ListAPIView):
	queryset = Item.objects.all()
	serializer_class = ItemListViewSerializer
	# permission_classes = [AllowAny,]
	# filter_backends = [OrderingFilter, SearchFilter,]
	# search_fields = ['name', 'description', 'owner__username']

class ItemDetailAPIView(RetrieveAPIView):
	queryset = Item.objects.all()
	serializer_class = ItemDetailViewSerializer
	lookup_field = 'id'
	lookup_url_kwarg = 'item_id'
	# permission_classes = [AllowAny,]

class ItemCreateUpdateAPIView(RetrieveUpdateAPIView):
	queryset = Item.objects.all()
	serializer_class = ItemCreateUpdateSerializer
	lookup_field = 'id'
	lookup_url_kwarg = 'item_id'
	#permission_classes = [IsAuthenticated,IsOwner]

class ItemCreateAPIView(CreateAPIView):
	queryset = Item.objects.all()
	serializer_class = ItemCreateUpdateSerializer
	
	#permission_classes = [IsAuthenticated,IsOwner]

class ItemStockUpdateAPIView(RetrieveUpdateAPIView):
	queryset = Item.objects.all()
	serializer_class = ItemStockUpdateSerializer
	lookup_field = 'id'
	lookup_url_kwarg = 'item_id'
	#permission_classes = [IsAuthenticated,IsOwner]