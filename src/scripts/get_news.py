from app.helpers import NewsHelper
from app import db
from app.models import News
from app.models import Keywords
from app.helpers.db_helper import DbHelper
from app import app

app.app_context().push()

keywords = ["vida","fallecen"]
result = NewsHelper().search_news(keywords)
result['keywords']
result['news']

for news in result['news']:
    print(type(news))
    kwargs = {"content": news['content'],"reference": news['reference']}
    n = DbHelper().get_or_create(db.session, News, **kwargs)
    for word in result['keywords']:
        keywords_args = {"keyword": word, "keywords": n}
        kw = DbHelper().get_or_create(db.session, Keywords, **keywords_args)



News.query.filter(News.keywords.any(Keywords.keyword == 'ss')).all()
News.query.filter(News.keywords.any(Keywords.keyword.in_(['1','falllecen']))).all()



News.query.filter(News.keywords.contains(Keywords.keyword == 'vida'))
     query.filter(User.addresses.contains(someaddress))



Keywords.query.filter_by(keyword = 'vida')

patients = News.query.filter(Keywords.keywords.contains("vida"))

News.query.filter(News.keywords.contains(Keywords.keyword == 'vida'))
     query.filter(User.addresses.contains(someaddress))


a = db.session.query(Keywords).filter_by(keyword='vida')




db.session.query(News).join(News, Keywords.news_id == News.id).filter(Keywords.keyword == 'vida')
