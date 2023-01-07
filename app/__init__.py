from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import folium
import csv

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY']='dev'
    app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///app.db'

    from .models import Node
    with app.app_context():
        db.init_app(app)
        db.create_all()

    from .views import home
    app.register_blueprint(home)

    with open('app/nodes.csv') as csvfile:
        for line in csv.reader(csvfile, delimiter=','):
            newNode = Node
            newNode.id = line[0]
            newNode.name = line[1]
            with app.app_context():
                db.session.add(newNode)
                db.session.commit()
        # with app.app_context():
        #     db.session.add_all(Node(csv.reader(csvfile, delimiter=',')))

    folium.Map(location=[48.463198, -123.311886], 
               zoom_start=17) \
               .save('templates/map.html')

    return app
