import logging
logger = logging.getLogger(__name__)


class NewsHelper(object):

    def get_news_universal():
        """
        Search news from the mexican newspaper "El Universal"
        """
        import requests
        from bs4 import BeautifulSoup

        url_eluniversal = "https://activo.eluniversal.com.mx/historico/search/index.php?q=vida+agua+permanente"
        res = requests.get(url_eluniversal)

        soup = BeautifulSoup(res.text, 'html.parser')
        head_nota = soup.select('div.HeadNota')

        entries = []
        for note in head_nota:
            print(note.a['href'])
            print(note.a.text)
            print("*" * 20)

            news = {
                "title": note.a.text,
                "link": note.a['href'],
                "summary": "",
            }
            entries.append(news)
        return entries

    def get_news_jornada():
        """
        Search news from the mexican newspaper "La Jornada"
        """
        import feedparser

        feed_url = "https://www.jornada.com.mx/ultimas/search_rss?SearchableText=vida+agua+permanente"
        news_feed = feedparser.parse(feed_url)
        # entry = news_feed.entries[1]
        # print(entry.keys())

        entries = []
        for entry in news_feed.entries:
            news = {
                "title": entry['title'],
                "link": entry['link'],
                "summary": entry['summary'],
            }
            entries.append(news)
        return entries
