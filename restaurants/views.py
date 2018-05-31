from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
# Function based view


def home_n(request):   # use Ctrl+Shift+/ for miltiline comment in sublime text 3
    html_var = 'f string ( python-3.6 ) '
    html_ = f"""<!DOCTYPE html>
    <html lang="en"><head>
    <meta charset="utf-8">
    </head>
    <body>
    <h1>Hello world !</h1>
    <p>This is { html_var } comming through</p>
    </body>
    </html>
    """
    return HttpResponse(html_)


def home(request):
    return render(request, "base.html", {"html_var": "context variable"})
