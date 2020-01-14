from django.contrib import admin
from django.urls import path

from .views import emailView, successView, redirectView

urlpatterns = [
	path('', redirectView),
    path('email/', emailView, name='email'),
    path('success/', successView, name='success'),
]