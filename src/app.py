from flask import Flask
from helpers import NewsHelper

import json
import logging
logger = logging.getLogger(__name__)

app = Flask(__name__)


@app.route("/")
def hello():
    news_eluniversal = NewsHelper.get_news_eluniversal()
    news_jornada = NewsHelper.get_news_jornada()
    news = news_eluniversal + news_jornada
    return json.dumps(news)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
