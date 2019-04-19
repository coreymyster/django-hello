from django.shortcuts import render
from django.http import HttpResponse

# If there is an http response then "Hello World!" will
# be diaplyed on the screen
def myView(request):
    return HttpResponse('Hello World!')
