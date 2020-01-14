from django import forms

from events.models import Post, Category, Comment, MY_CHOICES
from django_google_maps import widgets as map_widgets
from django_google_maps import fields as map_fields

class CommentForm(forms.Form):
    name = forms.CharField(
        max_length=60,
        widget=forms.TextInput(attrs={
            "class": "form-control",
            "placeholder": "enter yo name bro"
        })
    )
    body = forms.CharField(widget=forms.Textarea(
        attrs={
            "class": "form-control",
            
        })
    )

    issues = forms.CharField(label='Reason', widget=forms.CheckboxSelectMultiple(choices=MY_CHOICES))
    

    