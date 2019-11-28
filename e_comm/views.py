from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return render(request , "home.html")

def about(request):
    return HttpResponse("hello world")
def contact(request):
    return HttpResponse("this is contact")
