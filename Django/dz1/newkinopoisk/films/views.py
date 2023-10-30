from django.http import HttpResponse, Http404
from django.shortcuts import render


# Create your views here.

def newMove(request):
    return HttpResponse('Страница о фильме')


def index(request):
    return HttpResponse('Главная страница')


def movie_pages(request, name_page):
    data = {
        'menu': ['films', 'actors', 'search', 'about']

    }
    if name_page in ['info_movie', 'search_movie']:
        return render(request, f'films/{name_page}.html', data)
    return Http404('<h1>404 Page Not Found</h1>')


def categories(request, id_categories):
    return HttpResponse(f'Categories {id_categories}')


def year_archive(request, year):
    if year <= '2023':
        return HttpResponse(f'year {year}')
    return Http404


class A:
    def __init__(self, a, b):
        self.a = a
        self.__b = b

    @property
    def b(self):
        return self.__b


def f(request):
    data = {
        'movies': [{'id': 1, 'title': 'Movie1', 'description': 'description'},
                   {'id': 2, 'title': 'Movie2', 'description': 'description2'},
                   {'id': 2, 'title': 'Movie2', 'description': 'description2'}],
        'title': 'Учебная страница',
        'menu': ['About', 'page1', 'page2'],
        'num_float': 2.5,
        'num_int': 5,
        'set': {1, 2, 3, 4, 5},
        'dict': {'1': 5, '2': 2},
        'obj': A(5, 6),
    }

    return render(request, 'edu/example.html', data)
