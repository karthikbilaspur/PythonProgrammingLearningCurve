import time
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import nltk
import io
import unicodedata
import numpy as np
import re
import string
from numpy import linalg
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.tokenize import PunktSentenceTokenizer
from nltk.tokenize import PunktSentenceTokenizer
from nltk.corpus import webtext
from nltk.stem.porter import PorterStemmer
from nltk.stem.wordnet import WordNetLemmatizer


with open('kindle.txt', encoding ='ISO-8859-2') as f:
	text = f.read()
	
sent_tokenizer = PunktSentenceTokenizer(text)
sents = sent_tokenizer.tokenize(text)

print(word_tokenize(text))
print(sent_tokenize(text))

porter_stemmer = PorterStemmer()

nltk_tokens = nltk.word_tokenize(text)

for w in nltk_tokens:
	print ("Actual: % s Stem: % s" % (w, porter_stemmer.stem(w)))
	

wordnet_lemmatizer = WordNetLemmatizer()
nltk_tokens = nltk.word_tokenize(text)

for w in nltk_tokens:
	print ("Actual: % s Lemma: % s" % (w, wordnet_lemmatizer.lemmatize(w)))
	
text = nltk.word_tokenize(text)
print(nltk.pos_tag(text))

sid = SentimentIntensityAnalyzer() 
tokenizer = nltk.data.load('tokenizers / punkt / english.pickle')

with open('kindle.txt', encoding ='ISO-8859-2') as f:
	for text in f.read().split('\n'):
		print(text)
		scores = sid.polarity_scores(text)
		for key in sorted(scores):
			print('{0}: {1}, '.format(key, scores[key]), end ='')
			
	print()
