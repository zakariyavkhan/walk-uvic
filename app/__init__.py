from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import folium
import csv

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config.from_mapping(
        SECRET_KEY='some_key',
        DATABASE='database',
    )

    from models import Node
    db.init_app(app)
    db.create_all()

    from .views import home
    app.register_blueprint(home)

    with open('nodes.csv') as csvfile:
        for line in csv.reader(csvfile, delimiter=','):
            db.session.add(line)
            db.session.commit()
        # db.session.add_all(csv.reader(csvfile, delimiter=','))

    folium.Map(location=[48.463198, -123.311886], 
               zoom_start=17) \
               .save('templates/map.html')

    return app
