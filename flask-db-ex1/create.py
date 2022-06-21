from appdbexer import db

class Person(db.Model):
    id = db.Column(db.Integer() , primary_key=True)
    first_name = db.Column(db.String(30), nullable=False)
    last_name = db.Column(db.String(30), nullable=False)        


db.create_all()