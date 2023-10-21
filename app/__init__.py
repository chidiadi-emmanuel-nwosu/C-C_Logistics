#!/usr/bin/python3
"""init file"""
from datetime import timedelta
from flask import Flask, session
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_migrate import Migrate
from app.config import config


db = SQLAlchemy()
bcrypt = Bcrypt()
login_manager = LoginManager()
login_manager.login_view = 'app_routes.login'
login_manager.login_message_category = 'warning'
migrate = Migrate()

def create_app(config_name):
    """initialises app for either development or production"""
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    db.init_app(app)
    migrate.init_app(app, db)
    bcrypt.init_app(app)
    login_manager.init_app(app)

    @app.before_request
    def handle_session():
        session.permanent = True
        app.permanent_session_lifetime = timedelta(days=1)

    from app.routes import app_routes
    from app.models import user, agent

    @login_manager.user_loader
    def load_user(user_id):
        user_model = user.User.query.get((user_id))
        if user_model is None:
            agent_model = agent.DeliveryAgent.query.get((user_id))
            return agent_model
        return user_model

    app.register_blueprint(app_routes)

    return app

app = create_app('development')
