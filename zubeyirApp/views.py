from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def zubeyir_home(req):
    return HttpResponse('<h1>Zubeyir Gulen</h1>')
