"""Logged-in page routes."""
from flask import Blueprint, redirect, render_template, url_for, make_response
from flask_login import current_user, login_required, logout_user

# Blueprint Configuration
main_bp = Blueprint(
    "main_bp", __name__, template_folder="templates", static_folder="static"
)

# Instead of using decorator `@app.route('<path>')` for our routes we use `@main_bp.route('<path>')`
# This associates the route with the main_bp blueprint that is configured above and registered in `__init__.py`
# We can also using the decorator @login_required to require login to see these routes

@main_bp.route('/')
@main_bp.route('/home')
def home():
    return "<h1>Welcome to Flashcardz!</h1>"

@main_bp.route('/<email>/mydecks')
@login_required
def my_decks(email):
    return """
        <h1>Hello, {}</h1>
        <h2>Welcome to your account home page (My Decks)!</h2>
    """.format(email)

@main_bp.route('/decks/create')
@login_required
def create_deck():
    return "<h1>Create a Deck here!</h1>"

@main_bp.route('/decks/edit')
@login_required
def edit_deck():
    return "<h1>Edit a Deck here!</h1>"

@main_bp.route('/decks/overview')
def deck_overview():
    return "<h1>View a Deck Overview here!</h1>"

@main_bp.route('/explore-decks')
def explore():
    return "<h1>Explore other decks here!</h1>" 

@main_bp.route("/logout")
@login_required
def logout():
    """User log-out logic."""
    logout_user()
    return redirect(url_for("auth_bp.login"))

@main_bp.errorhandler(404)
def not_found():
    """Page not found."""
    return "<h1>404: Not Found</h1>"