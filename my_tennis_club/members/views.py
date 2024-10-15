"""Create your views here"""

from django.shortcuts import render
from django.http import HttpResponse

def members(request):
    # The name of the view does not have to be the same as the application.
    # I call it members because I think it fits well in this context.
    return HttpResponse("Hello World")