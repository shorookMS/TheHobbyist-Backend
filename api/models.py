

from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save




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
	image = models.ImageField(null=True, blank=True)
	rating = models.CharField(max_length=120)
	category = models.CharField(max_length=1, choices=DEPARTMENT_CHOICE)
	available = models.BooleanField(default=True)
	

	def __str__(self):
		return self.name

class Profile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	phoneNo = models.CharField(max_length=9,null=True)
	bio = models.TextField(max_length=500)
	img = models.ImageField(null=True)
	birth_date = models.DateField(null=True)

	def __str__(self):
		return self.user.username

class Address(models.Model):
	GOVERNORATE_CHOICE = (
		('A', 'Al Asimah Governorate'),
		('H', 'Hawalli Governorate'),
		('F', 'Farwaniya Governorate'),
		('M', 'Mubarak Al-Kabeer Governorate'),
		('AH', 'Ahmadi Governorate'),
		('J', 'Jahra Governorate'),
		)

	user = models.ForeignKey(Profile, default=1,  related_name='addresses', on_delete=models.CASCADE)
	name = models.CharField(max_length=120)
	governorate = models.CharField(max_length=2, choices=GOVERNORATE_CHOICE)
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
	STATUS_CHOICE=(
		('O', 'Ordered'),
		('P', 'Packed'),
		('D', 'Delivered')
		)

	user= models.ForeignKey(Profile, default=1, related_name='orders',  on_delete=models.CASCADE)
	date = models.DateField(auto_now_add=True)
	status = models.CharField( default=0,max_length=2, choices=STATUS_CHOICE)
	address = models.ForeignKey(Address, default=1, on_delete=models.CASCADE)

class OrderItem(models.Model):
	item= models.ForeignKey(Item, default=1, on_delete=models.CASCADE)
	order=models.ForeignKey(Order, default=1, related_name='orderItems', on_delete=models.CASCADE)
	quantity=models.PositiveIntegerField(default=0)	



@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
	if created:
		Profile.objects.create(user=instance)

# @receiver(post_save, sender=User)
# def save_user_profile(sender, instance, **kwargs):
# 	instance.profile.save()



