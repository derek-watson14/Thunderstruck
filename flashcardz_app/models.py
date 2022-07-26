from . import db
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

# Defining many-to-many relationships with helper table
# For more information visit:
# https://flask-sqlalchemy.palletsprojects.com/en/2.x/models/
scores = db.Table('cardscores', 
    db.Column('attempts', db.Integer, nullable=False),
    db.Column('correct', db.Integer, nullable=False),
    db.Column('last_attempt_correct', db.Boolean, nullable=False),
    db.Column('user_id', db.Integer, db.ForeignKey('users.id'), primary_key=True),
    db.Column('card_id', db.Integer, db.ForeignKey('cards.id'), primary_key=True)
)

class User(UserMixin, db.Model):
    """User account model."""

    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(40), nullable=False, unique=False)
    password = db.Column(db.String(200), primary_key=False, unique=False, nullable=False)
    owned_decks = db.relationship('Deck', backref='users', lazy=True)
    scores = db.relationship('Card', secondary=scores, lazy=True, backref=db.backref('users', lazy=True))

    def set_password(self, password):
        self.password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)

    # Defines how entry will be represented in a print statement
    def __repr__(self):
        return "<User email={}>".format(self.email)

class Deck(db.Model):
    """Deck model."""

    __tablename__ = "decks"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(40), nullable=False, unique=False)
    card_count = db.Column(db.Integer, primary_key=False, nullable=False)
    cards = db.relationship('Card', backref='deck', lazy=True)
    owner_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)

    # Defines how entry will be represented in a print statement
    def __repr__(self):
        return "<Deck name={}>".format(self.name)

class Card(db.Model):
    """Card model."""

    __tablename__ = "cards"
    id = db.Column(db.Integer, primary_key=True)
    front = db.Column(db.String(560), nullable=False, unique=False)
    back = db.Column(db.String(560), nullable=False, unique=False)
    deck_id = db.Column(db.Integer, db.ForeignKey('decks.id'), nullable=False)

    # Defines how entry will be represented in a print statement
    def __repr__(self):
        # Show only first n chars of string in print statement
        CHARS = 20
        front_partial = self.front[:CHARS] + "..." if len(self.front) > CHARS else self.front
        back_partial = self.back[:CHARS] + "..." if len(self.front) > CHARS else self.back
        # return "<Card front={} back={}>".format(front_partial, back_partial)
        return "<Card front={} back={}>".format(front_partial, back_partial)

