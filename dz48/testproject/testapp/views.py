from django.shortcuts import render


# Create your views here.

def index(request):
    return render(request, 'testapp/index.html')


def books(request):
    return render(request, 'testapp/book.html')


def authors(request):
    return render(request, 'testapp/author.html')


def form(request):
    return render(request, 'testapp/form.html')
