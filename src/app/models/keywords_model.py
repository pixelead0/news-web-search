from app import db


class Keywords(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    news_id = db.Column(db.Integer, db.ForeignKey('news.id'))
    keyword = db.Column(db.String())

    def to_dict(self):
        data = {
            'id': self.id,
            'news_id': self.news_id,
            'keyword': self.keyword,
        }

    def __repr__(self):
        return f"<Keywords {self.keyword}>"
