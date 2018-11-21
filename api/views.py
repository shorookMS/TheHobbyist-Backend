from .models import (Item, Address)
from rest_framework.generics import (
	ListAPIView,
	RetrieveAPIView,
	RetrieveUpdateAPIView,
	DestroyAPIView,
	CreateAPIView,
)
from .serializers import (
	ItemListViewSerializer, 
	ItemDetailViewSerializer, 
	ItemCreateUpdateSerializer, 
	ItemStockUpdateSerializer
)

from .serializers import ( 
	AddressListViewSerializer, 
	AddressDetailViewSerializer, 
	AddressCreateUpdateSerializer, 
	AddressDefaultUpdateSerializer
)

from .serializers import (
	UserCreateSerializer,
	UserLoginSerializer

	)

from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST
from rest_framework.views import APIView

# User Views

class UserCreateAPIView(CreateAPIView):
	serializer_class = UserCreateSerializer

class UserLoginAPIView(APIView):
    serializer_class = UserLoginSerializer

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
            
       

# class Login(View):
#     form_class = UserLogin

#     def get(self, request, *args, **kwargs):
#         form = self.form_class()
#         return render(request, self.template_name, {'form': form})

#     def post(self, request, *args, **kwargs):
#         form = self.form_class(request.POST)
#         if form.is_valid():

#             username = form.cleaned_data['username']
#             password = form.cleaned_data['password']

#             auth_user = authenticate(username=username, password=password)
#             if auth_user is not None:
#                 login(request, auth_user)
#                 messages.success(request, "Welcome Back!")
#                 return redirect('dashboard')
#             messages.warning(request, "Wrong email/password combination. Please try again.")
#             return redirect("login")
#         messages.warning(request, form.errors)
#         return redirect("login")

# class Logout(View):
#     def get(self, request, *args, **kwargs):
#         logout(request)
#         messages.success(request, "You have successfully logged out.")
#         return redirect("login")

# def profile(request, user_id):
#     user = User.objects.get(id=user_id)
#     events = Event.objects.filter(user=user)

#     my_follows = []
#     for follow in Follower.objects.filter(follower = request.user):
#         my_follows.append(follow.following.id)  

#     context = {
#         'events':events,
#         'user':user,
#         'my_follows': my_follows
#     }
#     return render(request, 'profile.html', context)

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
	serializer_class = AddressListViewSerializer

	def get_queryset(self, *args, **kwargs):
		if self.request.user.is_anonymous:
			return Address.objects.all()
		return Address.objects.filter(user=self.request.user)


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
