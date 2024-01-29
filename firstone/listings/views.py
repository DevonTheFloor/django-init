from django.http import HttpResponse
from django.shortcuts import render

def hello(request):
    return HttpResponse('<h1>Hello Maestro Django!</h1>')

def about(request):
    return HttpResponse('<h1>À propos</h1> <p>Nous adorons merch !</p>')

def listing(request):
    return HttpResponse('<h1>LISTING</h1>')

def contact(request):
    return HttpResponse('<h1>Formulaire de Contact')
# Create your views here.
