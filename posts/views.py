from django.shortcuts import render
from django.http import HttpResponse

def index (request):
    #body
    return HttpResponse('Welcome to Django')

def home (request):
    #body
    return HttpResponse('<h3>Welcome to Homepage of blog</h3>')