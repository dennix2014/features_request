from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from flask_bootstrap import Bootstrap


db = SQLAlchemy()
migrate = Migrate()
login = LoginManager()
login.login_view = 'auth.login'
bootstrap = Bootstrap()


def create_app(config_class=Config):
	app = Flask(__name__)
	app.config.from_object(config_class)

	db.init_app(app)
	migrate.init_app(app, db)
	login.init_app(app)
	bootstrap.init_app(app)
	



	from src.auth import bp as auth_bp
	app.register_blueprint(auth_bp, url_prefix='/auth')


	from src.features import bp as features_bp
	app.register_blueprint(features_bp)



	return app
from src import models