import numpy as np
import nltk
import string
import pandas as pd
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer
from nltk.stem import WordNetLemmatizer
from nltk.sentiment import SentimentIntensityAnalyzer

stremmer=PorterStemmer()
lemmatizer = WordNetLemmatizer()
sia = SentimentIntensityAnalyzer()

#read the data as text file
text_file = open("C:\\Users\\Ramy Anwar\\Desktop\\Ramy\\data analytics\\data.csv", "r")
data = text_file.readlines()

#lower or upper the data
for i in range(0,len(data)):
    data[i]=data[i].lower()

#remove punctutation
for i in range(0,len(data)):
    data[i] = data[i].translate(str.maketrans('','', string.punctuation))

#remove stop words
stops= set (stopwords.words('english'))

res = []
res1 = []

for i in range(0,len(data)):
    res= res + word_tokenize(data[i])

res= [i for i in res if not i in stops]

print(res)

