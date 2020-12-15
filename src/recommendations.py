import string
import pickle
import pandas as pd
import preprocessor as p
from sklearn.metrics.pairwise import linear_kernel

with open('models/vectors.pickle', 'rb') as data:
    vectors = pickle.load(data)
    
with open('models/vectorizer.pickle', 'rb') as data:
    vectorizer = pickle.load(data)
    
df=pd.read_csv("data/tweets_1.csv")

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