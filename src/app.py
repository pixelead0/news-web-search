from flask import Flask
from flask import jsonify
from helpers import NewsHelper

import logging
logger = logging.getLogger(__name__)

app = Flask(__name__)


@app.route("/api/news", methods=['POST'])
def get_news():
    news_eluniversal = NewsHelper.get_news_universal()
    news_jornada = NewsHelper.get_news_jornada()
    news_sol_de_mexico = NewsHelper.get_news_sol_de_mexico()
    news = news_eluniversal + news_jornada + news_sol_de_mexico
    return jsonify(news)


@app.errorhandler(404)
@app.errorhandler(405)
def page_not_found(error):
    error_404 = {"error": "the page cannot be loaded"}
    return jsonify(error_404)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
