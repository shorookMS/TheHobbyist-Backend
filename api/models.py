from django.db import models
from django.contrib.auth.models import User

class Item(models.Model):
	DEPARTMENT_CHOICE = (
		('M', 'Music'),
		('B', 'Books'),
		('S', 'Sports'),
		('A', 'Art'),
		('T', 'Tech'),
		)
	name = models.CharField(max_length=120)
	description = models.TextField()
	price = models.DecimalField(max_digits=6, decimal_places=3)
	stock = models.PositiveIntegerField()
	image = models.CharField(max_length=120)
	rating = models.CharField(max_length=120)
	category = models.CharField(max_length=1, choices=DEPARTMENT_CHOICE)
	available = models.BooleanField(default=True)
	

	def __str__(self):
		return self.name

class Address(models.Model):
	GOVERNORATE_CHOICE = (
		('A', 'Al Asimah Governorate'),
		('H', 'Hawalli Governorate'),
		('F', 'Farwaniya Governorate'),
		('M', 'Mubarak Al-Kabeer Governorate'),
		('AH', 'Ahmadi Governorate'),
		('J', 'Jahra Governorate'),
		)
	user= models.ForeignKey(User, default=1,  related_name='user', on_delete=models.CASCADE)
	name = models.CharField(max_length=120)
	governorate = models.CharField(max_length=1, choices=GOVERNORATE_CHOICE)
	area = models.CharField(max_length=40)
	block = models.PositiveIntegerField()
	street = models.CharField(max_length=120)
	house_building = models.CharField(max_length=40)
	floor = models.PositiveIntegerField()
	appartment = models.CharField(max_length=10)
	extra_directions = models.TextField()
	default = models.BooleanField(default=False)


	def __str__(self):
		return self.name

class Order(models.Model):
	status=(
		('0', 'Ordered'),
		('P', 'Packed'),
		('D', 'Delivered')
		)

	user= models.ForeignKey(User, default=1, related_name='user',  on_delete=models.CASCADE)
	date = models.DateField(auto_now_add=True)
	address = models.ForeignKey(Address, default=1, on_delete=models.CASCADE)

class OrderItem(models.Model):
	item= models.ForeignKey(Item, default=1, on_delete=models.CASCADE)
	order=models.ForeignKey(Order, default=1, related_name='item', on_delete=models.CASCADE)
	quantity=models.PositiveIntegerField()	
