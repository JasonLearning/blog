from . import db

class Article(db.Model):
    __tablename__ = 'articles'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.Unicode(64), unique=True)
    subtitle = db.Column(db.Unicode(64))
    content = db.Column(db.UnicodeText(), unique=True)
    timestamp = db.Column(db.DateTime())
    viewcount = db.Column(db.Integer())
    image_url = db.Column(db.String())

    def __repr__(self):
        return '<Article "%r">' % self.title


class Comment(db.Model):
    __tablename__ = 'comments'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Unicode(32))
    email = db.Column(db.String(64), unique=True)
    md5 = db.Column(db.String(32), unique=True)
    content = db.Column(db.UnicodeText(), unique=True)

    def __repr__(self):
        return '<Comment by %r>' % self.email


tag_table = db.Table('tag_table',
    db.Column('article_id', db.Integer, db.ForeignKey('articles.id')),
    db.Column('tag_id', db.Integer, db.ForeignKey('tags.id'))
)


class Tag(db.Model):
    __tablename__ = 'tags'
    id = db.Column(db.Integer, primary_key=True)
    tagname = db.Column(db.Unicode(32))
    articles = db.relationship('Article',
                               secondary=tag_table,
                               backref=db.backref('tags', lazy='dynamic'),
                               lazy='dynamic')

    def __repr__(self):
        return '<Tag of %r>' % self.tagname

