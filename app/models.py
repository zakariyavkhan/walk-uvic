from . import db

class Node(db.Model):
    name = db.Column(db.String(length=30), primary_key=True)
    id = db.Column(db.Integer(), unique=True, nullable=False)

    def __repr__(self):
        return f'{self.name}'