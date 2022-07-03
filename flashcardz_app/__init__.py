import os
import sqlite3
from werkzeug.security import generate_password_hash, check_password_hash
from flask import Flask, redirect, request, render_template, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, UserMixin
import flashcardz_app.models
from flashcardz_app.forms import RegistrationForm, LoginForm

def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),
    )
    
    if test_config is None:
        app.config.from_pyfile('config.py', silent=True)
    else:
        app.config.from_mapping(test_config)

    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass
    
    #set-up loginmanager object
    login_manager = LoginManager()
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(user_id):
        return flashcardz_app.models.User.get_id(user_id)

    @app.route('/')
    def home():
        return "<h1>Welcome to Flashcardz!</h1>"
    
    @app.route('/login')
    def login():
        
        return "<h1>Login Page!</h1>"
    
    @app.route('/register', methods = ['POST', 'GET'])
    def register():
        form = RegistrationForm()
        if form.validate_on_submit():
            user = flashcardz_app.models.User(email=form.email.data, password=form.password1.data)
            user.set_password(form.password1.data)
            #add sqlite insert command
            conn = sqlite3.connect('/Users/jtrull/Documents/cspb3308/Thunderstruck/flashcardz_app/flashcardz.db')
            cur = conn.cursor()
            cur.execute("INSERT INTO users values (?, ?, ?)", (None, user.email, user.password_hash))
            conn.commit()
            cur.close()
            print(user.email+": "+user.password_hash)
            return redirect(url_for('login'))
        return render_template("registration.html", form=form)
    
    @app.route('/mydecks-home')
    def my_decks():
        return "<h1>Welcome to your account home page (My Decks)!</h1>"

    @app.route('/create-deck')
    def create_deck():
        return "<h1>Create a Deck here!</h1>"
    
    @app.route('/edit-deck')
    def edit_deck():
        return "<h1>Edit a Deck here!</h1>"
    
    @app.route('/deck-overview')
    def deck_overview():
        return "<h1>View a Deck Overview here!</h1>"
    
    @app.route('/explore-decks')
    def explore():
        return "<h1>Explore other decks here!</h1>" 
    
    
    return app
