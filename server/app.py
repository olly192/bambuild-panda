from flask import Flask
from flask_cors import CORS
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from os import environ, path
from dotenv import load_dotenv

# Get .env file and load config variables
basedir = path.abspath(path.dirname(__file__))
load_dotenv(path.join(basedir, '../.env'))


# Config class
class Config:
    # General Config
    SECRET_KEY = environ.get('SECRET_KEY')
    FLASK_APP = environ.get('FLASK_APP')
    CORS_HEADERS = 'Content-Type'

    # Database
    SQLALCHEMY_DATABASE_URI = environ.get("SQLALCHEMY_DATABASE_URI")
    SQLALCHEMY_ECHO = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False


# Create database
db = SQLAlchemy()


def create_app():
    app = Flask(__name__, instance_relative_config=False)
    # Initialise server and database with config class
    app.config.from_object(Config)
    db.init_app(app)

    with app.app_context():
        # Import views
        from server.views import views as view_routes
        from server.auth import auth as auth_routes
        from server.api import api as api_routes
        # Register views
        app.register_blueprint(view_routes, url_prefix='/')
        app.register_blueprint(auth_routes, url_prefix='/')
        app.register_blueprint(api_routes, url_prefix='/api')

        # Import error pages
        from server.error import error403, error404, error500
        app.register_error_handler(401, error403)
        app.register_error_handler(403, error403)
        app.register_error_handler(404, error404)
        app.register_error_handler(500, error500)

        # Create database tables for data models in models.py
        db.create_all()
        migrate = Migrate(app, db)

        cors = CORS(app)

        # Import user model and initialise login manager
        from server.models import User
        login_manager = LoginManager()
        login_manager.init_app(app)

        @login_manager.user_loader
        def load_user(id):
            return User.query.get(int(id))

        return app


app = create_app()

if __name__ == '__main__':
    app.run()
