from .models import (Item, Address,OrderItem, Order, Profile)
from rest_framework.generics import (
	ListAPIView,
	RetrieveAPIView,
	RetrieveUpdateAPIView,
	DestroyAPIView,
	CreateAPIView,
)

from .serializers import ( 
  OrderListViewSerializer, 
  OrderDetailViewSerializer, 
  OrderCreateUpdateSerializer, 
  OrderStatusUpdateSerializer
)

from .serializers import ( 
  OrderItemDetailViewSerializer, 
  OrderItemCreateUpdateSerializer,
  OrderItemListViewSerializer 
)

from .serializers import (
	ItemListViewSerializer, 
	ItemDetailViewSerializer, 
	ItemCreateUpdateSerializer, 
	ItemStockUpdateSerializer
)

from .serializers import ( 
	AddressListViewSerializer,  
	AddressCreateUpdateSerializer, 
	AddressDefaultUpdateSerializer
)

from .serializers import (
	UserCreateSerializer,
	UserLoginSerializer,
	ProfileDetailViewSerializer

	)

from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser
from .permissions import IsOwner, IsUser,IsItemUser
# User Views


class UserCreateAPIView(CreateAPIView):
	serializer_class = UserCreateSerializer
	permission_classes = [AllowAny,]

class UserLoginAPIView(APIView):
	serializer_class = UserLoginSerializer
	permission_classes = [AllowAny,]
	def post(self, request):
		my_data = request.data
		serializer = UserLoginSerializer(data=my_data)
		if serializer.is_valid(raise_exception=True):
			valid_data = serializer.data
			return Response(valid_data, status=HTTP_200_OK)
		return Response(serializer.errors, HTTP_400_BAD_REQUEST)


# class UserSignupAPIView(View):

#     def get(self, request, *args, **kwargs):
#         user = self.form_class()
#         profile = self.form_profile()
#         context = {
#             'form': user,
#             'profile_form': profile,
#         }
#         return render(request, self.template_name,context)

#     def post(self, request, *args, **kwargs):
#         user = self.form_class(request.POST)
#         profile = self.form_profile(request.POST, request.FILES)
#         context = {
#             'form': user,
#             'profile_form': profile,
#         }

#         if user.is_valid() and profile.is_valid():
#             user_obj = user.save(commit=False)
#             user_obj.set_password(user_obj.password)
#             user_obj.save()

# @login_required
# @transaction.atomic
# def update_profile(request):
#     user_form = UserSignup(request.POST, instance=request.user)
#     profile_form = ProfileForm(request.POST, instance=request.user.profile)
#     if request.method == 'POST':
#         user_form = UserSignup(request.POST, instance=request.user)
#         profile_form = ProfileForm(request.POST,  request.FILES, instance=request.user.profile)
#         if user_form.is_valid() and profile_form.is_valid():
#             user_obj = user_form.save(commit=False)
#             user_obj.set_password(user_obj.password)
#             user_obj.save()
#             profile_form.save()
#             messages.success(request, 'Your profile was successfully updated!')
#             login(request,user_obj)
#             return redirect('profile', request.user.id)
#         else:
#             messages.error(request, 'Please correct the error below.')
#     else:
#         user_form = UserSignup(instance=request.user)
#         profile_form = ProfileForm(instance=request.user.profile)

#     context = {
#         'user_form': user_form,
#         'profile_form': profile_form
#     }
#     return render(request, 'profile_update.html', context)


# Item Views


class ItemListAPIView(ListAPIView):
	queryset = Item.objects.all()
	serializer_class = ItemListViewSerializer
	permission_classes = [AllowAny,]
	# filter_backends = [OrderingFilter, SearchFilter,]
	# search_fields = ['name', 'description', 'owner__username']

class ItemDetailAPIView(RetrieveAPIView):
	queryset = Item.objects.all()
	serializer_class = ItemDetailViewSerializer
	lookup_field = 'id'
	lookup_url_kwarg = 'item_id'
	permission_classes = [AllowAny,]

class ItemCreateUpdateAPIView(RetrieveUpdateAPIView):
	queryset = Item.objects.all()
	serializer_class = ItemCreateUpdateSerializer
	lookup_field = 'id'
	lookup_url_kwarg = 'item_id'
	permission_classes = [IsAdminUser]

class ItemCreateAPIView(CreateAPIView):
	queryset = Item.objects.all()
	serializer_class = ItemCreateUpdateSerializer
	permission_classes = [IsAdminUser]

class ItemStockUpdateAPIView(RetrieveUpdateAPIView):
	queryset = Item.objects.all()
	serializer_class = ItemStockUpdateSerializer
	lookup_field = 'id'
	lookup_url_kwarg = 'item_id'
	permission_classes = [IsAdminUser]


# Address Views

class AddressListAPIView(ListAPIView):
	queryset = Address.objects.all()
	serializer_class = AddressListViewSerializer
	permission_classes = [IsAuthenticated,IsAdminUser]

class AddressCreateUpdateAPIView(RetrieveUpdateAPIView):
	queryset = Address.objects.all()
	serializer_class = AddressCreateUpdateSerializer
	lookup_field = 'id'
	lookup_url_kwarg = 'address_id'
	permission_classes = [IsAuthenticated,IsOwner]

class AddressCreateAPIView(CreateAPIView):
	queryset = Address.objects.all()
	serializer_class = AddressCreateUpdateSerializer
	permission_classes =[IsAuthenticated,IsOwner]

class AddressDefaultUpdateAPIView(RetrieveUpdateAPIView):
	queryset = Address.objects.all()
	serializer_class = AddressDefaultUpdateSerializer
	lookup_field = 'id'
	lookup_url_kwarg = 'address_id'
	permission_classes =[IsAuthenticated,IsOwner]


# Order Views
class OrderListAPIView(ListAPIView):
	queryset = Order.objects.all()
	serializer_class = OrderListViewSerializer
	permission_classes =[IsAuthenticated,IsOwner]

class OrderDetailAPIView(RetrieveAPIView):
	queryset = Order.objects.all()
	serializer_class = OrderDetailViewSerializer
	lookup_field = 'id'
	lookup_url_kwarg = 'order_id'
	permission_classes = [IsAuthenticated,IsOwner]

class OrderCreateAPIView(CreateAPIView):
	# queryset = Order.objects.all()
	serializer_class = OrderCreateUpdateSerializer
	permission_classes =[IsAuthenticated,IsOwner]

	def post(self, request):
		my_data = request.data
		print(request.user)
		serializer = self.serializer_class(data=my_data)
		if serializer.is_valid():
			valid_data = serializer.data
			new_data = {
				'status': valid_data['status'],
				'profile': Profile.objects.get(id=request.user.id),
				'address': valid_data['address']
			}
			Order.objects.create(**new_data)
			return Response(valid_data, status=HTTP_200_OK)
		return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)

class OrderStatusUpdateAPIView(RetrieveUpdateAPIView):
	queryset = Order.objects.all()
	serializer_class = OrderStatusUpdateSerializer
	lookup_field = 'id'
	lookup_url_kwarg = 'order_id'
	permission_classes =[IsAuthenticated,IsOwner]

# OrderItem Views
class OrderItemDetailAPIView(RetrieveAPIView):
	queryset = OrderItem.objects.all()
	serializer_class = OrderItemDetailViewSerializer
	lookup_field = 'id'
	lookup_url_kwarg = 'orderitem_id'
	permission_classes = [IsAuthenticated,IsItemUser]


class OrderItemCreateAPIView(CreateAPIView):
	queryset = OrderItem.objects.all()
	serializer_class = OrderItemCreateUpdateSerializer
	permission_classes = [IsAuthenticated,IsItemUser]


class OrderItemDeleteAPIView(DestroyAPIView):
	queryset = OrderItem.objects.all()
	serializer_class = OrderItemListViewSerializer
	lookup_field = 'id'
	lookup_url_kwarg = 'orderitem_id'
	permission_classes = [IsAuthenticated,IsItemUser]

# Profile Views 
class ProfileDetailAPIView(RetrieveAPIView):
	queryset = Profile.objects.all()
	serializer_class = ProfileDetailViewSerializer
	lookup_field = 'id'
	lookup_url_kwarg = 'user_id'
	permission_classes =[IsAuthenticated,IsUser]

	
