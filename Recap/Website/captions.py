import requests


class timedtext_url():
    def __init__(self, youtube_url):
        self._youtube_url = youtube_url
        self._timedtext_url_domain = 'https://www.youtube.com/api/timedtext?'
        self._video_id = self.get_videoid()
        self._language = 'lang=en'
        self._format = 'fmt=srv3'

    def get_videoid(self):
        video_id = self._youtube_url[self._youtube_url.index('?') + 1 : ]

        return video_id

    def get_timedtext_url(self):
        return self._timedtext_url_domain + '&'.join([self._video_id, self._language, self._format])





if __name__ == '__main__':

    foo = timedtext_url('https://www.youtube.com/watch?v=vwFCvSQSsVk')
    timedtext_url = foo.get_timedtext_url()

    r = requests.get(timedtext_url)

    file = r.text

    print(file)
    print(timedtext_url)
