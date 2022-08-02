"""Logged-in page routes."""
from flask import Blueprint, redirect, render_template, url_for, make_response
from flask_login import current_user, login_required, logout_user
import flask_login

from .forms import AddCardForm, CreateDecksForm, AddAnswerForm

from .models import User, Deck, Card, db

# Blueprint Configuration
main_bp = Blueprint(
    "main_bp", __name__, template_folder="templates", static_folder="static"
)

# Instead of using decorator `@app.route('<path>')` for our routes we use `@main_bp.route('<path>')`
# This associates the route with the main_bp blueprint that is configured above and registered in `__init__.py`
# We can also using the decorator @login_required to require login to see these routes

# @main_bp.route('/')
# @main_bp.route('/home')
# def home():
#     return "<h1>Welcome to Flashcardz!</h1>"

@main_bp.route('/<email>/mydecks')
@login_required
def my_decks(email):
    #step one, obtain id of user to obtain decks
    current_user = User.query.filter_by(email=email).first()
    #step two, get collection of all decks owned by logged in user
    user_decks = Deck.query.filter_by(owner_id=current_user.id).all()
    return render_template('my_decks.html', email=email, user_decks=user_decks, title="My Decks")

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

    return render_template('create_deck.html', form=form, title="Create Deck")

@main_bp.route('/<email>/<deck_id>/decks/edit', methods=['GET', 'POST'])
@login_required
def edit_deck(email, deck_id):
    user_cards = Card.query.filter_by(deck_id=deck_id).all()
    form = AddCardForm()
    if form.validate_on_submit():
        new_card = Card(front=form.front.data, back=form.back.data, deck_id=deck_id)
        db.session.add(new_card)
        db.session.commit()
        user_cards = Card.query.filter_by(deck_id=deck_id).all()
        return render_template('my_cards.html', email=email, user_cards=user_cards, form=form, title="Edit Deck")

    
    return render_template('my_cards.html', email=email, user_cards=user_cards, form=form)

@main_bp.route('/<email>/<deck_id>/decks/overview')
def deck_overview(email, deck_id):
    cards = Card.query.filter_by(deck_id=deck_id).all()
    deck = Deck.query.filter_by(id=deck_id).one()
    deck_name = deck.name
    return render_template('deck_overview.html', email=email, deck_id=deck_id, deck_name=deck_name, cards=cards)

@main_bp.route('/<email>/<deck_id>/<card_id>/study')
def study(email, deck_id, card_id=0, methods=['GET', 'POST']):
    
    card_id = int(card_id)
    cards = Card.query.filter_by(deck_id=deck_id).all() #returns list of all cards
    print(cards)
    print(cards[card_id].id)
    print(cards[0].id)
    current_card = cards[card_id]  #start with first card in list
    deck = Deck.query.filter_by(id=deck_id).one()
    deck_name = deck.name
    working_card = Card.query.filter_by(id=current_card.id).one() #get card to update below correct answer


    form = AddAnswerForm()
    if form.validate_on_submit():
        if (form.yes.data):
            working_card.correct = True
        else:
            working_card.correct = False
        
        db.session.commit()
        return render_template('study.html', form=form, title="Study Deck", email=email, deck_id=deck_id, deck_name=deck_name, current_card=current_card, card_id=current_card.id)
    
    return render_template('study.html', form=form, title="Study Deck", email=email, deck_id=deck_id, deck_name=deck_name, current_card=current_card, card_id=current_card.id)

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