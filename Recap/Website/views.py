from django.shortcuts import render
from django.http import HttpResponse


def homepage(request):
    if request.method == 'POST':
        yt_video = request.POST.get('hack')
        print(yt_video)
        
    return render(request , 'Website/index.html')

def results(request ,url): 
    return HttpResponse(f'{url}')