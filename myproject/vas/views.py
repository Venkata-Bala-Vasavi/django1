# from django.shortcuts import render
from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
def home(request):
    return HttpResponse("Hello 23b01a12g0")
def firstpage(request):
    return HttpResponse("welcome 23b01a12g0")
def secondpage(request):
    return HttpResponse("Hi 23b01a12g0")
def htmlpage(request):
    template = loader.get_template('external.html')
    return HttpResponse(template.render())

# Create your views here.
