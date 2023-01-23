from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import folium, csv

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY']='dev'
    app.config['SQLALCHEMY_DATABASE_URI']='sqlite://'

    from .models import Node
    with app.app_context():
        db.init_app(app)
        db.create_all()

    with open('app/nodes.csv') as csvfile:
        for line in csv.reader(csvfile, delimiter=','):
            with app.app_context():
                db.session.add(Node(name=line[0], id=line[1]))
                db.session.commit()

    from .views import home
    app.register_blueprint(home)

    folium.Map(location=[48.463198, -123.311886], 
               zoom_start=18) \
               .save('app/templates/map.html')


    return app
