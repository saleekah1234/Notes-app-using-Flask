from app import db

class Mynotes(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(1000), index=False, unique=True)

    def __repr__(self):
        return '<Mynotes {}>'.format(self.name)   