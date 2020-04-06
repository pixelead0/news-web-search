import logging
logger = logging.getLogger(__name__)


class NewsHelper(object):

    def get_news_eluniversal():
        import requests
        from bs4 import BeautifulSoup
        url_eluniversal = "https://activo.eluniversal.com.mx/historico/search/index.php?q=vida+agua+permanente"
        res = requests.get(url_eluniversal)

        soup = BeautifulSoup(res.text, 'html.parser')
        head_nota = soup.select('div.HeadNota')

        entries = []
        for note in head_nota:
            logger.info(note.a['href'])
            logger.info(note.a.text)
            logger.info("*" * 20)

            news = {
                "title": note.a.text,
                "link": note.a['href'],
                "summary": "",
            }
            entries.append(news)
        return entries
