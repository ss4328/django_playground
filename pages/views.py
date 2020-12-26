from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home_view(request, *args, **kwargs):
	print(request.user)
	# return HttpResponse("<h1> Home Page</h1>")
	return render(request, "home.html", {})

def contact_view(request, *args, **kwargs):
	return render(request, "contact.html", {})

def about_view(request, *args, **kwargs):
	about_context = {
		"name": "About",
		"number": 123,
		"numberList": [123,1234,12345,123456]
	}
	return render(request, "about.html", about_context)

def social_view(request, *args, **kwargs):
	return render(request, "social.html", {})

