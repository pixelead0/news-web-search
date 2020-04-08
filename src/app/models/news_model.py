from app import db


class News(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String())
    reference = db.Column(db.String())
    ranking = db.Column(db.Numeric(10, 2), default=0.0)
    keywords = db.relationship('Keywords', backref='keywords', lazy='dynamic')

    def to_dict(self):
        data = {
            'id': self.id,
            'content': self.content,
            'reference': self.reference,
            'ranking': self.ranking,
            'keywords': self.keywords,
        }

    def __repr__(self):
        return f"<News {self.content}>"
