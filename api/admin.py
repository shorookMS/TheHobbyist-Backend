from django.contrib import admin

from .models import (Item, Address,Order,OrderItem, Profile)

admin.site.register(Item)
admin.site.register(Address)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(Profile)

