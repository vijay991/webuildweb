from app import db

class user(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), index=True)

    def __repr__(self):
        return '<User {}>'.format(self.email)
