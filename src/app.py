from flask import Flask
from helpers import NewsHelper

import json
import logging
logger = logging.getLogger(__name__)

app = Flask(__name__)


@app.route("/")
def get_news():
    news_eluniversal = NewsHelper.get_news_eluniversal()
    news_jornada = NewsHelper.get_news_jornada()
    news_sol_de_mexico = NewsHelper.get_news_sol_de_mexico()
    news = news_eluniversal + news_jornada + news_sol_de_mexico
    return json.dumps(news)


@app.errorhandler(404)
def page_not_found(error):
    error_404 = {"error": "page not found"}
    return json.dumps(error_404), 404

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
