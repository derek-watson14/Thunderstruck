import os
import psycopg2
import sqlite3
import werkzeug
from werkzeug.security import generate_password_hash, check_password_hash
from flask import Flask, redirect, request, render_template, url_for, flash
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

# Create globally accessible instances of important libaries
login_manager = LoginManager()
db = SQLAlchemy()

def create_app():

    # Initialize the core application
    app = Flask(__name__, instance_relative_config=False)
    app.config.from_object("config.Config")
    
    # Initialize library plugins
    db.init_app(app)
    login_manager.init_app(app)

    # Import routes and create app
    with app.app_context():
        # Import routes from routes.py
        from . import auth, routes

        # Register Blueprints
        # Flask apps can be organized via a built-in concept called Blueprints, which are essentially the Flask equivalent of Python modules
        # Blueprints keep related logic and assets grouped and separated from one another
        # In this case main_bp (routes.py) contains pages users see when logged, and auth.bp (auth.py) contain login and auth routes
        app.register_blueprint(routes.main_bp)
        app.register_blueprint(auth.auth_bp)
        
        # Create database tables for our data models
        db.create_all()
    
        return app
 