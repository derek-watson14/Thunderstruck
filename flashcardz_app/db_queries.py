def get_user_from_email(email):
    """
    Returns user info from an email address. Returns null if doesn't exist.
    """
    pass

def get_user_from_id(user_id):
    """
    Returns user info from a user id. Returns null if doesn't exist.
    """
    pass

def get_owned_decks(user_id):
    """
    Returns all decks owned by a particular user.
    """
    pass

def get_liked_decks(user_id):
    """
    Returns all decks liked by a particular user.
    """
    pass

def get_all_deck_cards(deck_id):
    """
    Returns all cards in a certain deck.
    """
    pass

def get_card_score(user_id, card_id):
    """
    Returns attempt/correct data for a particular card a user has tested on before.
    """
    pass

def get_all_card_scores_for_deck(user_id, deck_id):
    """
    Returns all of a users scores on a certain deck.
    """
    pass

def create_deck(deck_name, user_id):
    """
    Posts new deck and owned deck to the database
    """
    pass

def edit_deck_name(user_id, deck_id, new_deck_name):
    """
    Edits the name of the deck if the authenticated user is the owner 
    """
    pass

def like_deck(deck_id, user_id):
    """
    Posts new liked deck to the database
    """
    pass

def delete_deck(user_id, deck_id):
    """
    Deletes deck from Decks, LikedDecks and OwnedDecks
    """
    pass

def unlike_deck(user_id, deck_id):
    """
    Deletes deck from a user's LikedDecks
    """
    pass

def add_card(user_id, deck_id, front_text, back_text):
    """
    Posts new card to an existing deck
    """
    pass

def edit_card(user_id, card_id, front_text, back_text):
    """
    Changes front or back text of a card if a user owns the card
    """

def delete_card(deck_id, front_text, back_text):
    """
    Adds new card to existing deck
    """
    pass