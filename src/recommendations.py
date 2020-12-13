import pickle
import pandas as pd
import nltk
#nltk.download('stopwords')
from nltk.corpus import stopwords
from nltk.tokenize import RegexpTokenizer
import re
from sklearn.metrics.pairwise import cosine_similarity



with open('models/google_model.pickle', 'rb') as data:
    google_model = pickle.load(data)


def _removeNonAscii(s):
    return "".join(i for i in s if  ord(i)<128)

def make_lower_case(text):
    return text.lower()

def remove_stop_words(text):
    text = text.split()
    stops = set(stopwords.words("english"))
    text = [w for w in text if not w in stops]
    text = " ".join(text)
    return text

def remove_html(text):
    html_pattern = re.compile('<.*?>')
    return html_pattern.sub(r'', text)

def remove_punctuation(text):
    tokenizer = RegexpTokenizer(r'\w+')
    text = tokenizer.tokenize(text)
    text = " ".join(text)
    return text



df = pd.read_csv("data/tweets_1.csv")

df['text'] = df['text'].astype(str)
df['cleaned'] = df['text'].apply(_removeNonAscii)

df['cleaned'] = df.cleaned.apply(func = make_lower_case)
df['cleaned'] = df.cleaned.apply(func = remove_stop_words)
df['cleaned'] = df.cleaned.apply(func=remove_punctuation)
df['cleaned'] = df.cleaned.apply(func=remove_html)


# genere average word2dec pour chaque champ
def vectors(x):
    
    
    global word_embeddings
    word_embeddings = []

    
    for line in df['cleaned']:
        avgword2vec = None
        count = 0
        for word in line.split():
            if word in google_model.wv.vocab:
                count += 1
                if avgword2vec is None:
                    avgword2vec = google_model[word]
                else:
                    avgword2vec = avgword2vec + google_model[word]
                
        if avgword2vec is not None:
            avgword2vec = avgword2vec / count
        
            word_embeddings.append(avgword2vec)



def recommendations(text):
    vectors(df)
    cosine_similarities = cosine_similarity(word_embeddings, word_embeddings)
    books = df[['text', 'id']]
    indices = pd.Series(df.index, index = df['text']).drop_duplicates()  
    idx=df[df['text']==text].index.tolist()[0]
    sim_scores = list(enumerate(cosine_similarities[idx]))
    sim_scores = sorted(sim_scores, key = lambda x: x[1], reverse = True)
    sim_scores = sim_scores[1:21]
    book_indices = [i[0] for i in sim_scores]
    recommend = books.iloc[book_indices]
    #print(sim_scores)
    return(recommend)
