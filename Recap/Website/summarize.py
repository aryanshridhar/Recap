from youtube_transcript_api import YouTubeTranscriptApi

a = YouTubeTranscriptApi.get_transcript('KdmPHEnPJPs&t=1s')

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
    

with open('file.txt' , 'w') as f:
    f.write(str(final))
