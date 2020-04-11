# from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.tokenize.toktok import ToktokTokenizer

import pandas as pd
# import re
import string

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
