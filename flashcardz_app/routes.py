"""Logged-in page routes."""
from flask import Blueprint, redirect, render_template, url_for, make_response
from flask_login import current_user, login_required, logout_user
import flask_login

from .forms import CreateDecksForm

from .models import User, Deck, db

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
    #step one, obtain id of user to obtain decks
    current_user = User.query.filter_by(email=email).first()
    #step two, get collection of all decks owned by logged in user
    user_decks = Deck.query.filter_by(owner_id=current_user.id).all()
    return render_template('my_decks.html', email=email, user_decks=user_decks)

@main_bp.route('/<email>/decks/create', methods=['GET', 'POST'])
@login_required
def create_deck(email):

    form = CreateDecksForm()
    if form.validate_on_submit():
        current_user = User.query.filter_by(email=email).first()
        new_deck = Deck(name=form.deck_name.data, card_count=form.card_count.data, owner_id=current_user.id)
        db.session.add(new_deck)
        db.session.commit()
        return redirect(url_for('main_bp.my_decks', email=email))

    return render_template('create_deck.html', form=form)

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