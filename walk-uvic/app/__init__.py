from flask import Flask
from flask_sqlalchemy import SQLAlchemy

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
    # for line in nodes.csv, add node to db

    from .views import home
    app.register_blueprint(home)

    return app
