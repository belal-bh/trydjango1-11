import random
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
# Function based view


def home(request):
    num = None
    rand_list = [
        random.randint(0, 20008),
        random.randint(0, 9333333),
        random.randint(0, 32222222),
    ]
    condition_bool_item = True
    if condition_bool_item:
        num = random.randint(0, 160131)
    context = {
        "num": num,
        "rand_list": rand_list,
    }
    return render(request, "base.html", context)
