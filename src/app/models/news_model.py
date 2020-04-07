from app import db


class News(db.Model):
    __tablename__ = 'news'

    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String())
    reference = db.Column(db.String())
    ranking = db.Column(db.Integer())
    keywords = db.Column(db.String())

    def __repr__(self):
        return f"<News {self.content}>"
