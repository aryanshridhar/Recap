from django.shortcuts import render , redirect
from django.http import HttpResponse
from youtube_transcript_api import YouTubeTranscriptApi
from gensim.summarization import summarize
import re

def summarize1(percent=20):
    f = open('file.txt','r')
    raw = f.read()
    f.close()
    if '.' in str(percent):
        percent = float(percent)
    else:
        percent = int(percent)
    sumz=summarize(raw,ratio=percent/100)

    return sumz

def id_video(url):
    result = re.match('^[^v]+v=(.{11}).*', url)
    return result.group(1)

def geturl(video):
    a = YouTubeTranscriptApi.get_transcript(video)
    list1 = []

    for key in range(0,len(a),3):
        try:
            i1 = a[key].get('text')
            i2 = a[key+1].get('text')
            i3 = a[key+2].get('text')
        except IndexError:
            pass

        final = i1 + i2 + i3
        list1.append(final)
        
    final_str = '\n'.join(list1)

    with open('file.txt' , 'w') as f:
        f.write(str(final_str))


def homepage(request):
    if request.method == 'POST':
        yt_video = request.POST.get('hack')
        try:
            vid_id = id_video(yt_video)
        except:
            return render(request , 'Website/404wrong.html')
        return redirect(f'http://127.0.0.1:8000/results/{vid_id}')
        
    return render(request , 'Website/index.html')

def results(request ,url):
    words = 20
    if request.method == 'POST':
        words = request.POST.get('word')
    geturl(url)
    summarized = summarize1(percent=words)
    context = {'summary' : summarized.replace('\n','').title() , 'url': 'https://www.youtube.com/embed/'+url}
    return render(request , 'Website/result.html' , context)

def view_404(request , *args , **kwargs):
    return render(request , 'Website/404.html')