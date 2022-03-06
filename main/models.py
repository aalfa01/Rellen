from django.db import models
from relen.mixins import TranslateMixin

# Create your models here.


class Category(TranslateMixin,models.Model):
	translate_attributes = ['name']
	name_uz = models.CharField(max_length=100)
	name_ru = models.CharField(max_length=100)
	image = models.ImageField(upload_to = "Categories")
	danger = models.CharField(max_length=50, blank=True)
	properties = models.ManyToManyField('Properties')
	def __str__(self):
		return self.name

	

class Image(models.Model):
	image = models.ImageField(upload_to="Posts")
	name = models.CharField(max_length=50)

	def __str__(self):
		return self.name

class Post(TranslateMixin,models.Model):
	translate_attributes = ['subject','comment']
	post = models.ForeignKey(Category, on_delete=models.RESTRICT,null=True,default=None)
	image = models.ManyToManyField(Image)
	subject_uz = models.CharField(max_length=100)
	subject_ru = models.CharField(max_length=100)
	comment_uz = models.TextField()
	comment_ru = models.TextField()
	
	def __str__(self):
		return self.subject


class relen(models.Model):
	image = models.ImageField(upload_to="Relen")
	header = models.CharField(max_length=50)

	def __str__(self):
		return self.header
	

class Ism(models.Model):
	name = models.CharField(max_length=50)
	phone = models.IntegerField()
	message = models.TextField()
	def __str__(self):
		return self.name

class Properties(TranslateMixin, models.Model):
	translate_attributes = ['content']
	name = models.CharField(max_length=50)
	content_uz = models.TextField()
	content_ru = models.TextField()
	relen_product = models.ManyToManyField(relen)
	products = models.ManyToManyField(Post)
	def __str__(self):
		return self.name