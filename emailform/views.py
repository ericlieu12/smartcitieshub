from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from .forms import ContactForm
def redirectView(request):
	return HttpResponseRedirect('email/')
def emailView(request):
    if request.method == 'GET':
        form = ContactForm()
    else:
        form = ContactForm(request.POST)
        if form.is_valid():
            category = form.cleaned_data['category']
            body = form.cleaned_data['body']
            title = form.cleaned_data['title']
            address = form.cleaned_data['address']

            try:
                send_mail(category, body, ['el961@myn.edu'], ['admin@example.com'])
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return redirect('success')
    return render(request, "email.html", {'form': form})

def successView(request):
    return HttpResponse('Success! Click the back button, I was too lazy to code this section.')

# Create your views here.
