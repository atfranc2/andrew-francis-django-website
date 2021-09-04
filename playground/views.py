from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

# Can be called by a certain endpoint by mapping views to a URL


def calculate():
    x = 1
    return x


def say_hello(request):
    x = calculate()
    return render(request, 'hello.html', {'name': 'Andrew'})
