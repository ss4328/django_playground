from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home_view(*args, **kwargs):
	return HttpResponse("<h1> Home Page</h1>")


def contact_view(*args, **kwargs):
	return HttpResponse("<h1> Contact Page </h1>")



