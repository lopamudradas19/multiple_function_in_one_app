from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
def first(request):
    return HttpResponse('This is my first FVB')
def second(request):
    return HttpResponse('This is my second FVB')
def home1(request):
    return render(request,'home1.html')
def home2(request):
    return render(request,'home2.html')