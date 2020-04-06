from flask import Flask

import json
import logging
logger = logging.getLogger(__name__)

app = Flask(__name__)


@app.route("/")
def hello():
    news = {
        'title': 'Titulo de la noticia',
        'summary': 'Contenido de la noticia'
    }
    logger.info(news)
    return json.dumps(news)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
