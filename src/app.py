from flask import Flask, jsonify, request
from helpers import NewsHelper

import logging
logger = logging.getLogger(__name__)

app = Flask(__name__)


@app.route("/api/news", methods=['POST'])
def get_news():

    result = {}

    try:
        keywords = request.json.get('keywords')
        keywords_str = '+'.join(str(e) for e in keywords)

        news_eluniversal = NewsHelper().get_news_universal(keywords_str)
        news_jornada = NewsHelper().get_news_jornada(keywords_str)
        news_sol_de_mexico = NewsHelper().get_news_sol_de_mexico(keywords_str)

        result['keywords_str'] = keywords_str
        result['keywords'] = keywords
        result['news'] = news_eluniversal + news_jornada + news_sol_de_mexico
        return jsonify(result)

    except Exception as e:
        error = {"error": f"the page cannot be loaded: -{e}-"}
        return jsonify(error)


@app.errorhandler(404)
@app.errorhandler(405)
def page_not_found(error):
    error_404 = {"error": "the page cannot be loaded"}
    return jsonify(error_404)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
