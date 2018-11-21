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
        'email',
        ''
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
        'detail'
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
        'item',
        'order',
        'quantity'
            ]

class OrderSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    orderitems = OrderItemSerializer()
    class Meta:
        model = Order
        fields = [ 
            'id', 
            'status',
            'date',
            'user',
            ]







# User Serializer 

# class UserCreateSerializer(serializers.ModelSerializer):
#     password = serializers.CharField(write_only=True)
#     user =  serializers.UserSerializer
#     class Meta:
#         model = Profile 
#         fields = ['user','phoneNo', 'bio', 'birth_date', 'img']

#     def create(self, validated_data):
#         username = validated_data['username']
#         password = validated_data['password']
#         new_user = User(username=username)
#         new_user.set_password(password)
#         new_user.save()

#         return validated_data


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

# Make a Profile Serialiser 


# Items Serializers


class ItemListViewSerializer(serializers.ModelSerializer):
    detail = serializers.HyperlinkedIdentityField(
        view_name = "api-detail",
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
        'rating',
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
# Look at this 


class AddressListViewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = [  
        'id',
        'name',
        'area',
        'user',
            ]
        
class AddressCreateUpdateSerializer(serializers.ModelSerializer):
   class Meta:
       model = Address
       fields = [  
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

class OrderItemCreateUpdateSerializer(serializers.ModelSerializer):
    item = ItemSerializer()
    order = OrderSerializer()
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
   


# Order Serializers 

class OrderListViewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = [  
        'id',
        'status',
        'date',
        'user',
            ]
        
            
class OrderDetailViewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = [  
            'id',  
            'status',
            'date',
            'user'
                ]


class OrderCreateUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = [  
            'status',
            'date',
            'user'
                ]

class OrderDefaultUpdateSerializer(serializers.ModelSerializer):
   class Meta:
       model =Order
       fields = [
        'status'
           ]

