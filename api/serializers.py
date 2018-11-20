from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Item 

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
