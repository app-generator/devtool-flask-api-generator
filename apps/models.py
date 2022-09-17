from apps import db
class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(64))

class City(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name =  db.Column(db.String(64))
