from django.contrib.auth.models import User
from rest_framework import serializers
from .models import (Item, Address )

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

class AddressListViewSerializer(serializers.ModelSerializer):
    detail = serializers.HyperlinkedIdentityField(
        view_name = "api-address-detail",
        lookup_field = "id",
        lookup_url_kwarg = "address_id"
        )

    class Meta:
        model = Address
        fields = [  
        'id',
        'name',
        'governorate',
        'area',
        'user',
        'detail'

            ]

class AddressDetailViewSerializer(serializers.ModelSerializer):

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
