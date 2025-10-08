from flask import Flask, Blueprint
from flask_restful import Api
from configs.database import db
from flask_migrate import Migrate
import os

api_blueprint = Blueprint('base_api', __name__, url_prefix='/v1')
api = Api(api_blueprint)

# Import controllers so resources are registered
from src.resources.controllers import users

migrate = Migrate()

def create_app():
    app = Flask(__name__)
    basedir = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
    app.config['SQLALCHEMY_DATABASE_URI'] = f"sqlite:///{os.path.join(basedir, 'configs', 'Study.db')}"
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)
    migrate.init_app(app, db)
    app.register_blueprint(api_blueprint)
    return app
