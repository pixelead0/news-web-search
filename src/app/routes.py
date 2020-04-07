from flask import Flask, jsonify, request

from app import app
from app.helpers import NewsHelper

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
