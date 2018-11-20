from django.db import models

class Item(models.Model):
	DEPARTMENT_CHOICE = (
		('M', 'Music'),
		('B', 'Books'),
		('S', 'Sports'),
		('A', 'Art')
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
