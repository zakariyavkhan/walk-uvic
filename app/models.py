from . import db

class Node(db.Model):
    id = db.Column(db.Integer(), unique=True, nullable=False)
    name = db.Column(db.String(length=30), primary_key=True)
    # abbr

    def __repr__(self):
        return f'Item {self.name}'