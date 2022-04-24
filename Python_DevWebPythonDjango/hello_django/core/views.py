from django.shortcuts import render, HttpResponse
# Create your views here.


def hello(request, nome, intidade):
    return HttpResponse('<h1>Hello, {}, {} anos</h1>'.format(nome, intidade))
