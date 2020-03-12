from django.shortcuts import render , redirect
from django.http import HttpResponse


def homepage(request):
    if request.method == 'POST':
        yt_video = request.POST.get('hack')
        return redirect(f'http://127.0.0.1:8000/results/{yt_video}')
        
    return render(request , 'Website/index.html')

def results(request ,url): 
    return HttpResponse(f'{url}')