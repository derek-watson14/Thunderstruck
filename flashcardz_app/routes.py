"""Logged-in page routes."""
from flask import Blueprint, redirect, render_template, url_for, make_response, Response, request
from flask_login import current_user, login_required, logout_user
import flask_login

from .forms import AddCardForm, CreateDecksForm

from .models import User, Deck, Card, db

# Blueprint Configuration
main_bp = Blueprint(
    "main_bp", __name__, template_folder="templates", static_folder="static"
)

# Instead of using decorator `@app.route('<path>')` for our routes we use `@main_bp.route('<path>')`
# This associates the route with the main_bp blueprint that is configured above and registered in `__init__.py`
# We can also using the decorator @login_required to require login to see these routes

@main_bp.route('/')
def home():
    if current_user.is_authenticated:  
        return redirect(url_for('main_bp.my_decks', email=current_user.email))
    else:
        return redirect(url_for("auth_bp.login"))

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
        new_deck = Deck(name=form.deck_name.data, card_count=0, owner_id=current_user.id)
        db.session.add(new_deck)
        db.session.commit()
        return redirect(url_for('main_bp.my_decks', email=email))

    return render_template('create_deck.html', form=form, title="Create Deck")

@main_bp.route('/<email>/<deck_id>/decks/edit', methods=['GET', 'POST'])
@login_required
def edit_deck(email, deck_id):
    user_cards = Card.query.filter_by(deck_id=deck_id).all()
    deck= Deck.query.filter_by(id=deck_id).first()
    form = AddCardForm()

    #below logic used to calculate score for last attempt
    score_from_last_attempt = 0
    for card in user_cards:
        if(card.last_attempt == True):
            score_from_last_attempt += 1

    percent_score = round((score_from_last_attempt/len(user_cards))*100, 2)
    
    if form.validate_on_submit():
        new_card = Card(
            front=form.front.data, 
            back=form.back.data, 
            deck_id=deck_id, 
            attempts=0,
            correct=0,
            last_attempt=False,
        )
        deck.card_count += 1
        db.session.add(new_card)
        db.session.commit()
        return redirect(url_for('main_bp.edit_deck', email=email, deck_id=deck_id))

    return render_template('edit_deck.html', email=email, user_cards=user_cards, form=form, deck=deck, percent_score=percent_score)

@main_bp.route('/study/<deck_id>/<card_id>')
def study(deck_id, card_id):
    cards = Card.query.filter_by(deck_id=deck_id).order_by(Card.id).all()
    card_id = int(card_id)

    if card_id == -1:
        card_id = cards[0].id
        card = cards[0]
        return render_template('study.html', deck_id=deck_id, card_id=card_id, card=card)
    else:
        index = -1
        for ind, card in enumerate(cards):
            if card.id == card_id:
                index = ind + 1
                break
        
        if index >= len(cards) or index == -1:
            return redirect(url_for('main_bp.edit_deck', email=current_user.email, deck_id=deck_id))
        else:
            return render_template('study.html', deck_id=deck_id, card_id=cards[index].id, card=cards[index])


@main_bp.route("/delete-card?card_id=<card_id>&deck_id=<deck_id>", methods=["GET", "DELETE"])
@login_required
def delete_card(card_id, deck_id):
    Card.query.filter_by(id=card_id).delete()
    db.session.commit()
    return redirect(url_for('main_bp.edit_deck', email=current_user.email, deck_id=deck_id))


@main_bp.route("/record-score", methods=["PUT"])
@login_required
def record_score():
    data = request.json
    
    card = Card.query.filter_by(id=int(data["card_id"])).first()
    
    if(card.attempts == None):  #added to catch situation when attempt first set to None
        card.attempts = 1
    else:
        card.attempts += 1

    if data["correct"] == True:
        if(card.correct == None):  #added to catch situation when correct first set to None
            card.correct = 1
        else:
            card.correct += 1

        card.last_attempt = True
    else:
        card.last_attempt = False

    db.session.commit()

    return "Added"

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