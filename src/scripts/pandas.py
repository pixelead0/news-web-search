# from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.tokenize.toktok import ToktokTokenizer

import pandas as pd
# import re
import string

#####
import numpy as np
import os
import re
import operator
import nltk
from nltk.tokenize import word_tokenize
from nltk import pos_tag
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from collections import defaultdict
from nltk.corpus import wordnet as wn
from sklearn.feature_extraction.text import TfidfVectorizer
####

from app.helpers import NewsHelper
# from app import db
# from app.models import News
# from app.models import Keywords
# from app.helpers.db_helper import DbHelper
from app import app

import nltk
nltk.download('stopwords')
nltk.download('punkt')
nltk.download('perluniprops')
nltk.download('nonbreaking_prefixes')

app.app_context().push()

# Setting spanish language
punctuation = string.punctuation + "¿¡|`"
stop_words = set(stopwords.words('spanish'))
toktok = ToktokTokenizer()

keywords = ["vida", "fallecen"]
result = NewsHelper().search_news(keywords)


news = pd.DataFrame.from_dict(result['news'])

news_word_tokenize = []
for i, txt in enumerate(news.content):
    print(i)
    entry = toktok.tokenize(txt.lower())

    # removing punctuation marks.
    entry_filtered = list(
        filter(lambda token: token not in punctuation, entry))

    # deleting stop words
    entry_filtered = list(
        filter(lambda token: token not in stop_words, entry_filtered))
    print(entry)
    print(entry_filtered)
    news_word_tokenize.append(entry_filtered)

news['word_tokenize'] = news_word_tokenize


# Create Vocabulary
vocabulary = set()
for doc in news.word_tokenize:
    vocabulary.update(doc)

vocabulary = list(vocabulary)
# Intializating the tfIdf model
tfidf = TfidfVectorizer(vocabulary=vocabulary)

# Fit the TfIdf model
tfidf.fit(news.content)

# Transform the TfIdf model
tfidf_tran = tfidf.transform(news.content)


def gen_vector_T(tokens):
    """Create a vector for Query/search keywords"""
    Q = np.zeros((len(vocabulary)))
    x = tfidf.transform(tokens)
    print(tokens[0].split(','))
    for token in tokens[0].split(','):
        print(token)
        try:
            ind = vocabulary.index(token)
            Q[ind] = x[0, tfidf.vocabulary_[token]]
        except:
            pass
    return Q


def cosine_sim(a, b):
    """Cosine Similarity function for the calculation"""
    cos_sim = np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b))
    return cos_sim


def cosine_similarity_T(k, query):
    """Cosine Similarity b/w document to query function"""
    preprocessed_query = preprocessed_query = re.sub("\W+", " ", query).strip()
    tokens = word_tokenize(str(preprocessed_query))
    q_df = pd.DataFrame(columns=['q_clean'])
    q_df.loc[0, 'q_clean'] = tokens
    q_df['q_clean'] = wordLemmatizer(q_df.q_clean)
    d_cosines = []

    query_vector = gen_vector_T(q_df['q_clean'])
    for d in tfidf_tran.A:
        d_cosines.append(cosine_sim(query_vector, d))

    out = np.array(d_cosines).argsort()[-k:][::-1]
    print("")
    d_cosines.sort()
    a = pd.DataFrame()
    for i, index in enumerate(out):
        a.loc[i, 'index'] = str(index)
        a.loc[i, 'Subject'] = df_news['Subject'][index]
    for j, simScore in enumerate(d_cosines[-k:][::-1]):
        a.loc[j, 'Score'] = simScore
    return a

cosine_similarity_T(10,’computer science’)