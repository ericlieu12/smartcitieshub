from django.db import models
from django.utils import timezone
from multiselectfield import MultiSelectField
from django_google_maps import fields as map_fields

MY_CHOICES = (('IN PROGESS', 'IN PROGRESS'),
          ('SOLUTION', 'SOLUTION'),
          ('PROBLEM SOLVED', 'PROBLEM SOLVED'),
          ('SUGGESTION', 'SUGGESTION'),
          ('OFFER', 'OFFER'))

class CustomDateTimeField(models.DateTimeField):
    def value_to_string(self, obj):
        val = self.value_from_object(obj)
        if val:
            val.replace(microsecond=0)
            return val.isoformat()
        return ''
class Category(models.Model):
    name = models.CharField(max_length=20)
 
class Post(models.Model):
	title = models.CharField(max_length=255)
	body = models.TextField()
	categories = models.ManyToManyField('Category', related_name='posts')
	created = CustomDateTimeField(auto_now_add=True)
	lastedit = models.DateTimeField(auto_now=True)
	address = map_fields.AddressField(max_length=200,default='')
	geolocation = map_fields.GeoLocationField(max_length=100, default='')

class Comment(models.Model):
	op = models.CharField(max_length=20)
	comment = models.TextField()
	created = models.DateTimeField(auto_now_add=True)
	category = models.CharField(max_length=20)
	
	post = models.ForeignKey('Post',on_delete=models.CASCADE)
	