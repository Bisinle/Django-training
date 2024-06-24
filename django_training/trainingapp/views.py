from django.shortcuts import render
# ^ import httpresponse
from django.http import HttpResponse

# Create your views here.
def index(request):
    # return HttpResponse("<h1>Hello World, your are index</h1>")
    return render(request,'index.html')


def about(request):
    # return HttpResponse("<h1>About page</h1>")
      return render(request,'about.html')

def courses(request):
    return HttpResponse("<h1>courses page</h1>")
def teachers(request):
    return HttpResponse("<h1>teachers page</h1>")