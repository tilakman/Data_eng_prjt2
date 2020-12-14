import pandas as pd
import string
import re
import pickle
import preprocessor as p
import nltk
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer

from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.feature_extraction.text import TfidfVectorizer

from sklearn.metrics.pairwise import linear_kernel



with open('models/vectors.pickle', 'rb') as data:
    vectors = pickle.load(data)
    
with open('models/vectorizer.pickle', 'rb') as data:
    vectorizer = pickle.load(data)
    
with open('models/df_tweet.pickle', 'rb') as data:
    df = pickle.load(data)

def preprocessing(text):
    text = p.clean(text)
    text = [i for i in text.split() if (i not in string.punctuation)]
    return text

def vectorizing(text,vectorizer):
    text_vector = vectorizer.transform([str(text)])
    return text_vector

def similar_tweets(text_vector, vectors,df):
    cosine_similarities = linear_kernel(text_vector, vectors).flatten()
    related_docs_indices = cosine_similarities.argsort()[:-21:-1]
    tweets = df[['text','id']].loc[related_docs_indices] 
    return tweets

def recommendations(text):
    text_preprocessed = preprocessing(text)
    text_vector = vectorizing(text_preprocessed,vectorizer)
    tweets = similar_tweets(text_vector, vectors,df)
    return tweets