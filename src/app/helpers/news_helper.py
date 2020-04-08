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

    def get_news_from_db(self, keywords):
        from app.models import News
        from app.models import Keywords

        keywords_str = '+'.join(str(e) for e in keywords)

        result = News.query.filter(
            News.keywords.any(Keywords.keyword.in_(keywords))
        ).all()

        entries = []
        for entry in result:
            news = {
                "content": entry.content,
                "reference": entry.reference,
                "ranking": entry.ranking,
                "keywords": keywords_str,
            }
            entries.append(news)
        return entries

    def search_news(self, keywords):
        keywords_str = '+'.join(str(e) for e in keywords)

        result = {}
        result['keywords_str'] = keywords_str
        result['keywords'] = keywords

        news_from_db = self.get_news_from_db(keywords)
        if news_from_db:
            result['news'] = news_from_db
        else:
            news_eluniversal = self.get_news_universal(keywords_str)
            news_jornada = self.get_news_jornada(keywords_str)
            news_sol_de_mexico = self.get_news_sol_de_mexico(keywords_str)
            result['news'] = news_eluniversal + \
                news_jornada + news_sol_de_mexico
            save_news = self.save_news(result)

        return result

    def save_news(self, result):
        from app.models import News
        from app.models import Keywords
        from app.helpers.db_helper import DbHelper
        from app import db

        db_helper = DbHelper()

        for news in result['news']:
            news_args = {
                "content": news['content'],
                "reference": news['reference']
            }

            n = DbHelper().get_or_create(db.session, News, **news_args)

            for word in result['keywords']:
                print(word, n.id)
                keywords_args = {"keyword": word, "keywords": n}
                kw = DbHelper().get_or_create(db.session, Keywords, **keywords_args)
        return True
