from django.contrib import admin
from events.models import Post, Category, Comment
from django_google_maps import widgets as map_widgets
from django_google_maps import fields as map_fields
class Postmin(admin.ModelAdmin):
	formfield_overrides = {
	map_fields.AddressField: {
	'widget': map_widgets.GoogleMapsAddressWidget(attrs={'data-map-type': 'roadmap'})},
	}

class Catmin(admin.ModelAdmin):
 	pass


	

admin.site.register(Post, Postmin)
admin.site.register(Category, Catmin)

