from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    if request.method == 'POST':
        return HttpResponse("You must have POSTed something")
    else: # GET request
        return HttpResponse(request.method)
    # return HttpResponse("Hello, world! This is the about view.")
