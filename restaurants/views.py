import random
from django.http import HttpResponse
from django.shortcuts import render
from django.views import View

# Create your views here.
# Function based view


def home(request):
    context = {
    }
    return render(request, "home.html", context)


def about(request):
    context = {
    }
    return render(request, "about.html", context)


def contact(request):
    context = {
    }
    return render(request, "contact.html", context)


# Class based view
class ContactView(View):
    def get(self, request, *args, **kwargs):
        print(kwargs)
        context = {}
        return render(request, "contact.html", context)
