import pandas as pd
import string
import re
import pickle

import nltk
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
import preprocessor as p


from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.feature_extraction.text import TfidfVectorizer

from sklearn.metrics.pairwise import linear_kernel

df = pd.read_csv("data/tweets_1.csv")
df_clean = df.drop(columns=["Unnamed: 0","date","link","retweet","author"])


def preprocess_tweet(row):
    text = row['text']
    text = p.clean(text)
    return text

df_clean['text'] = df_clean.apply(preprocess_tweet, axis=1)
df_clean['Cleaned'] = df_clean['text'].apply(lambda x:''.join([i for i in x if i not in string.punctuation]))
df_clean['Cleaned'] = ["".join(word) for word in df_clean['Cleaned'].values]

vectorizer = TfidfVectorizer()
vectors = vectorizer.fit_transform(df_clean.Cleaned)

with open('models/vectors.pickle', 'wb') as output:
    pickle.dump(vectors, output)
    
with open('models/vectorizer.pickle', 'wb') as output:
    pickle.dump(vectorizer, output)