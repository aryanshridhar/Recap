import logging
from gensim.summarization import summarize
import nltk
from nltk.corpus import stopwords
from nltk.cluster.util import cosine_distance
import numpy as np

f = open('file.txt','r')
raw = f.read()
f.close()

sumz=summarize(raw,ratio=.5)

print(sumz)