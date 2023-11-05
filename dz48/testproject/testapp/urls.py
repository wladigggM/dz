from django.urls import path
from testapp.views import *

urlpatterns = [
    path('', index),
    path('books/', books),
    path('authors/', authors),
    path('form/', form)
]
