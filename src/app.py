from flask import Flask, jsonify, request
from helpers import NewsHelper

import logging
logger = logging.getLogger(__name__)

app = Flask(__name__)


@app.route("/api/news", methods=['POST'])
def get_news():

    try:
        keywords = request.json.get('keywords')
        news = NewsHelper().search_news(keywords)
        return jsonify(news)

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
