import os

from flask import Flask

def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)

    if test_config is None:
        app.config.from_pyfile('config.py', silent=True)
    else:
        app.config.from_mapping(test_config)

    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    @app.route('/')
    def home():
        return "<h1>Welcome to Flashcardz!</h1>"
    
    @app.route('/login')
    def login():
        return "<h1>Login Page!</h1>"
    
    @app.route('/create-new-account')
    def create_account():
        return "<h1>Create a new account!</h1>"
    
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
