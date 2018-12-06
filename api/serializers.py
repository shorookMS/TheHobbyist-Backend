from django.contrib.auth.models import User
from rest_framework import serializers

from .models import (Item, Address,Order,OrderItem, Profile )

# Serializers
class UserSerializer(serializers.ModelSerializer):
	class Meta:
		model = User
		fields = [  
		'username',
		'first_name',
		'last_name',
		'email'
			]
# Remove later
class ProfileSerializer(serializers.ModelSerializer):
	user = UserSerializer()
	class Meta:
		model = Profile
		fields = [  
		'user',
		'phoneNo',
		'bio',
		'img',
		'birth_date'
			]

class ItemSerializer(serializers.ModelSerializer):
	class Meta:
		model = Item
		fields = [  
		'id',
		'name',
		'price',
		'image',
		'rating',
		'description',
		'price',
		'stock',
		'image',
		'rating',
		'category',
		'available'

			]

class AddressSerializer(serializers.ModelSerializer):
	class Meta:
		model = Address
		fields = [
		'id',  
		'name',
		'governorate',
		'area',
		'block',
		'street',
		'house_building',
		'floor',
		'appartment',
		'extra_directions',
		'default',
			]

class OrderItemSerializer(serializers.ModelSerializer):
	class Meta:
		model = OrderItem
		fields = [
		'id',  
		'item',
		'order',
		'quantity'
			]

class OrderSerializer(serializers.ModelSerializer):
	# user = UserSerializer()
	address = AddressSerializer()
	orderItems = OrderItemSerializer(many=True, read_only=True)
	class Meta:
		model = Order
		fields = [ 
			'id', 
			'status',
			'date',
			'profile',
			'orderItems',
			'address'
			]
	def create(self, validated_data):
		orderItems_data = validated_data.pop('orderItems')
		order = Order.objects.create(**validated_data)
		for orderItem_data in orderitems_data:
			OrderItem.objects.create(order=order, **orderItem_data)
		return order


# User Serializer 

class ProfileUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile 
        fields = ['phoneNo', 'bio', 'birth_date', 'img']


class UserCreateSerializer(serializers.ModelSerializer):
	password = serializers.CharField(write_only=True)
	class Meta:
		model = User
		fields = ['username', 'password']

	def create(self, validated_data):
		username = validated_data['username']
		password = validated_data['password']
		new_user = User(username=username)
		new_user.set_password(password)
		new_user.save()
		return validated_data


class UserLoginSerializer(serializers.Serializer):
	username = serializers.CharField()
	password = serializers.CharField(write_only=True)
	token = serializers.CharField(allow_blank=True, read_only=True)

	def validate(self, data):
		my_username = data.get('username')
		my_password = data.get('password')

		try:
			user_obj = User.objects.get(username=my_username)
			jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
			jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER

			payload = jwt_payload_handler(user_obj)
			token = jwt_encode_handler(payload)

			data["token"] = token
		except:
			raise serializers.ValidationError("This username does not exist")

		if not user_obj.check_password(my_password):
			raise serializers.ValidationError("Incorrect username/password combination! Noob..")
		return data

# Profile Serialiser 

class ProfileDetailViewSerializer(serializers.ModelSerializer):
	addresses = AddressSerializer(many=True, read_only=True)
	orders = OrderSerializer(many=True, read_only=True)

	user = UserSerializer()
	class Meta:
		model = Profile
		fields = [  
		'user',
		'phoneNo',
		'bio',
		'img',
		'birth_date',
		'addresses',
		'orders'
			]


# Items Serializers


class ItemListViewSerializer(serializers.ModelSerializer):
	detail = serializers.HyperlinkedIdentityField(
		view_name = "api-item-detail",
		lookup_field = "id",
		lookup_url_kwarg = "item_id"
		)

	class Meta:
		model = Item
		fields = [  
		'id',
		'name',
		'price',
		'image',
		'stock',
		'rating',
		'category',
		'detail'
			]

class ItemDetailViewSerializer(serializers.ModelSerializer):

	class Meta:
		model = Item
		fields = [  
		'id',
		'name',
		'description',
		'price',
		'stock',
		'image',
		'rating',
		'category',
		'available'
		]
 
class ItemCreateUpdateSerializer(serializers.ModelSerializer):
	class Meta:
		model = Item
		fields = [
		'name',
		'description',
		'price',
		'stock',
		'image',
		'category',
		'available'
		]

 
class ItemStockUpdateSerializer(serializers.ModelSerializer):
   class Meta:
	    model = Item
	    fields = [
		 'stock',
		 ]


# Address Serializers 

#Check 
class AddressListViewSerializer(serializers.ModelSerializer):
	# user = ProfileSerializer()
	class Meta:
		model = Address
		fields = [  
		'id',
		'profile',
		'name',
		'governorate',
		'area',
		'block',
		'street',
		'house_building',
		'floor',
		'appartment',
		'extra_directions',
		'default',
		
			]
		
class AddressCreateUpdateSerializer(serializers.ModelSerializer):
   class Meta:
	   model = Address
	   fields = [  
		'profile',
		'name',
		'governorate',
		'area',
		'block',
		'street',
		'house_building',
		'floor',
		'appartment',
		'extra_directions',
		'default',
			]

 
class AddressDefaultUpdateSerializer(serializers.ModelSerializer):
	class Meta:
		model = Address
		fields = [
		  'default',
		]

# OrderItem Serializers
class OrderItemListViewSerializer(serializers.ModelSerializer):
	class Meta:
		model = OrderItem
		fields = [  
		'item',
		'order',
		'quantity'
			]     

class OrderItemCreateUpdateSerializer(serializers.ModelSerializer):
	# item = ItemSerializer()
	# order = OrderSerializer()
	class Meta:
		model = OrderItem
		fields = [  
		'item',
		'order',
		'quantity'
			]       

class OrderItemDetailViewSerializer(serializers.ModelSerializer):
	item = ItemSerializer()
	order = OrderSerializer()
	class Meta:
		model = OrderItem
		fields = [  
		'item',
		'order',
		'quantity'
			] 

class OrderItemQuantityUpdateSerializer(serializers.ModelSerializer):
   class Meta:
	   model =OrderItem
	   fields = [
		'quantity'
		   ]
   


# Order Serializers 

class OrderListViewSerializer(serializers.ModelSerializer):
	class Meta:
		model = Order
		fields = [  
		'id',
		'status',
		'date',
		'profile',
			]
		
			
class OrderDetailViewSerializer(serializers.ModelSerializer):
	orderItems =  OrderItemSerializer()
	class Meta:
		model = Order
		fields = [  
			'id',  
			'status',
			'date',
			'orderItems'
				]


class OrderCreateUpdateSerializer(serializers.ModelSerializer):
	class Meta:
		model = Order
		fields = [
			'id',
			'status',  
			'date',
			'address'
				]
	
class OrderStatusUpdateSerializer(serializers.ModelSerializer):
	# address= AddressSerializer()
	class Meta:
		model =Order
		fields = [
			'status',
			'address'
			]

