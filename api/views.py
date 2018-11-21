from .models import (Item, Address,OrderItem)
from rest_framework.generics import (
	ListAPIView,
	RetrieveAPIView,
	RetrieveUpdateAPIView,
	DestroyAPIView,
	CreateAPIView,
)
from .serializers import (UserCreateSerializer, ItemListViewSerializer, ItemDetailViewSerializer, ItemCreateUpdateSerializer, ItemStockUpdateSerializer)
from .serializers import ( AddressListViewSerializer, AddressDetailViewSerializer, AddressCreateUpdateSerializer, AddressDefaultUpdateSerializer)
from .serializers import ( OrderListViewSerializer, OrderDetailViewSerializer, OrderCreateUpdateSerializer, OrderDefaultUpdateSerializer)

class UserCreateAPIView(CreateAPIView):
	serializer_class = UserCreateSerializer


#Item Views


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


# Address Views

class AddressListAPIView(ListAPIView):
	queryset = Address.objects.all()
	serializer_class = AddressListViewSerializer
	# permission_classes = [AllowAny,]
	# filter_backends = [OrderingFilter, SearchFilter,]
	# search_fields = ['name', 'description', 'owner__username']

class AddressDetailAPIView(RetrieveAPIView):
	queryset = Address.objects.all()
	serializer_class = AddressDetailViewSerializer
	lookup_field = 'id'
	lookup_url_kwarg = 'address_id'
	# permission_classes = [AllowAny,]

class AddressCreateUpdateAPIView(RetrieveUpdateAPIView):
	queryset = Address.objects.all()
	serializer_class = AddressCreateUpdateSerializer
	lookup_field = 'id'
	lookup_url_kwarg = 'address_id'
	#permission_classes = [IsAuthenticated,IsOwner]

class AddressCreateAPIView(CreateAPIView):
	queryset = Address.objects.all()
	serializer_class = AddressCreateUpdateSerializer
	
	#permission_classes = [IsAuthenticated,IsOwner]

class AddressDefaultUpdateAPIView(RetrieveUpdateAPIView):
	queryset = Address.objects.all()
	serializer_class = AddressDefaultUpdateSerializer
	lookup_field = 'id'
	lookup_url_kwarg = 'address_id'
	#permission_classes = [IsAuthenticated,IsOwner]


# Order Views
class OrderDetailAPIView(RetrieveAPIView):
	queryset = Order.objects.all()
	serializer_class = OrderDetailViewSerializer
	lookup_field = 'id'
	lookup_url_kwarg = 'order_id'
	# permission_classes = [AllowAny,]

class OrderCreateAPIView(CreateAPIView):
	queryset = Order.objects.all()
	serializer_class = OrderCreateUpdateSerializer
	
	#permission_classes = [IsAuthenticated,IsOwner]

class OrderDefaultUpdateAPIView(RetrieveUpdateAPIView):
	queryset = Order.objects.all()
	serializer_class = OrderDefaultUpdateSerializer
	lookup_field = 'id'
	lookup_url_kwarg = 'order_id'
	#permission_classes = [IsAuthenticated,IsOwner]

# OrderItem Views
class OrderDetailAPIView(RetrieveAPIView):
	queryset = OrderItem.objects.all()
	serializer_class = OrderItemDetailViewSerializer
	lookup_field = 'id'
	lookup_url_kwarg = 'order_id'
	# permission_classes = [AllowAny,]

class OrderCreateAPIView(CreateAPIView):
	queryset = OrderItem.objects.all()
	serializer_class = OrderItemCreateUpdateSerializer
	
	#permission_classes = [IsAuthenticated,IsOwner]


	
