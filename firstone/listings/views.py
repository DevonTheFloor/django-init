from django.http import HttpResponse
from django.shortcuts import render
from listings.models import Band

def hello(request):
    bands = Band.objects.all()
    return render(request, 'listings/hello.html',{'bands': bands})

def about(request):
    return HttpResponse('<h1>À propos</h1> <p>Nous adorons merch !</p>')

def listing(request):
    return HttpResponse('<h1>LISTING</h1>')

def contact(request):
    return HttpResponse('<h1>Formulaire de Contact')
# Create your views here.
