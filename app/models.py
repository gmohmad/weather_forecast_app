from app import db


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(15))
    email = db.Column(db.String(20), unique=True)
    password = db.Column(db.String(8))
    comfortable_temperature = db.Column(db.Integer)

    def __repr__(self):
        return '<User %r>' % self.username
