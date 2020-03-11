from django.shortcuts import render
from django.http import HttpResponse


def homepage(request):
    return render(request , 'Webiste/index.html')

def results(request ,url): 
    return HttpResponse(f'{url}')