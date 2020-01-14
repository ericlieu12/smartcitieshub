from django import forms
from django_google_maps import widgets as map_widgets
from django_google_maps import fields as map_fields
MY_CHOICES = (('RESOURCE SHARING', 'RESOURCE SHARING'),
          ('ASSISTANCE REQUIRED', 'ASSISTANCE REQUIRED'),
          ('INFRASTRUCTURE', 'INFRASTRUCTURE'),
          ('TRAFFIC', 'TRAFFIC'),
          ('EVENTS', 'EVENTS'),
          ('FREE FOOD', 'FREE FOOD'),
          ('EMERGENCY', 'EMERGENCY'))
class ContactForm(forms.Form):
    title = forms.CharField(required=True)
    category = forms.CharField(label='Category', widget=forms.CheckboxSelectMultiple(choices=MY_CHOICES))
    body = forms.CharField(required=True)
    address = forms.CharField(max_length=200)
    
