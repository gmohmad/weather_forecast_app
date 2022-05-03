from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

from app import db
from app import login


class User(UserMixin, db.Model):
    """
    User model
    """

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(15))
    email = db.Column(db.String(20), unique=True)
    password = db.Column(db.String(8))
    comfortable_temperature = db.Column(db.Integer)

    def set_password(self, password):
        """
        Set password for user instanse
        """

        self.password = generate_password_hash(password, method='sha256')

    def check_password(self, password):
        """
        Check password for user instanse
        """

        return check_password_hash(self.password, password)

    def __repr__(self):
        return '<User %r>' % self.username


@login.user_loader
def load_user(id):
    return User.query.get(int(id))
