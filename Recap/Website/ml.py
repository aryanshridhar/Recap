from gensim.summarization import summarize

def summarize():
    f = open('file.txt','r')
    raw = f.read()
    f.close()
    sumz=summarize(raw,word_count=100)

    return sumz