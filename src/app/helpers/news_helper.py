import logging
logger = logging.getLogger(__name__)


class NewsHelper(object):

    def get_news_universal(self, keywords):
        """
        Search news from the mexican newspaper "El Universal"
        """
        import requests
        from bs4 import BeautifulSoup

        url_eluniversal = f"https://activo.eluniversal.com.mx/historico/search/index.php?q={keywords}"
        print(url_eluniversal)
        res = requests.get(url_eluniversal)

        soup = BeautifulSoup(res.text, 'html.parser')
        head_nota = soup.select('div.HeadNota')

        entries = []
        for note in head_nota:
            # print(note.a['href'])
            # print(note.a.text)
            # print("*" * 20)

            news = {
                "content": note.a.text,
                "reference": note.a['href'],
                "ranking": "0.0",
                "keywords": keywords,
            }
            entries.append(news)
        return entries

    def get_news_jornada(self, keywords):
        """
        Search news from the mexican newspaper "La Jornada"
        """
        import feedparser

        feed_url = f"https://www.jornada.com.mx/ultimas/search_rss?SearchableText={keywords}"
        # print(feed_url)
        news_feed = feedparser.parse(feed_url)
        # entry = news_feed.entries[1]

        entries = []
        for entry in news_feed.entries:
            news = {
                "content": entry['title'],
                "reference": entry['link'],
                "ranking": "0.0",
                "keywords": keywords,
            }
            entries.append(news)
        return entries

    def get_news_sol_de_mexico(self, keywords):
        """
        Search news from the mexican newspaper "El Sol de México"
        """
        import requests
        from bs4 import BeautifulSoup
        url_elsoldemexico = f"https://www.elsoldemexico.com.mx/buscar/?q={keywords}"
        print(url_elsoldemexico)
        res = requests.get(url_elsoldemexico)

        soup = BeautifulSoup(res.text, 'html.parser')
        head_nota = soup.select('div.results div.teaser div h4.title')

        entries = []
        for note in head_nota:
            # print(note.a['href'])
            # print(note.a.text)
            # print("*" * 20)

            news = {
                "content": note.a.text,
                "reference": note.a['href'],
                "ranking": "0.0",
                "keywords": keywords,
            }
            entries.append(news)
        return entries

    def search_news(self, keywords):
        keywords_str = '+'.join(str(e) for e in keywords)

        news_eluniversal = self.get_news_universal(keywords_str)
        news_jornada = self.get_news_jornada(keywords_str)
        news_sol_de_mexico = self.get_news_sol_de_mexico(keywords_str)

        result = {}
        result['keywords_str'] = keywords_str
        result['keywords'] = keywords
        result['news'] = news_eluniversal + news_jornada + news_sol_de_mexico

        save_news = self.save_news(result)

        return result

    def save_news(self, result):
        print("+" * 20)
        from app.models import News
        from app.models import Keywords
        from app import db

        for news in result['news']:
            n = News(
                content=news['content'],
                reference=news['reference'],
                ranking=0,
            )

            db.session.add(n)
            db.session.commit()

            for word in result['keywords']:
                print(word, n.id)
                kw = Keywords(keyword=word, keywords=n)
                db.session.add(kw)
                db.session.commit()

        return True
