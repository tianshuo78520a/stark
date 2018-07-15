from flask import Flask
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()

from .models import *
from .views.account import ac
from .views.user import us



def create_app():
    app = Flask(__name__)
    app.config.from_object('settings.BaseConfig')

    app.register_blueprint(ac)
    app.register_blueprint(us)

    db.init_app(app)
    return app

