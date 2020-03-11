from youtube_transcript_api import YouTubeTranscriptApi
from get_http_timed_text import timedtext_url

def get_timedtext(youtube_url):
    obj = timedtext_url(youtube_url)
    timedtext = YouTubeTranscriptApi.get_transcript(obj.get_videoid()[2:]) # get rid of fist two letters

    final_str = ' '.join(x['text'].replace('\n', ' ') for x in timedtext)

    return final_str


if __name__ == '__main__':
    try:
        obj = timedtext_url(input('type youtube url: '))
    except ValueError:
        print('Enter the url please !')
    else:
        try:
            timedtext = YouTubeTranscriptApi.get_transcript(obj.get_videoid()[2:]) # get rid of fist two letters
        except:
            print('Subtitles are disabled for this video')
        else:
            final_str = ' '.join(x['text'].replace('\n', ' ') for x in timedtext)

            with open('file.txt' , 'w') as f:
                f.write(str(final_str))
