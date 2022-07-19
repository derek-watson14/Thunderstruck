
class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.ownedDecks = []    # List of deckIds
        self.likedDecks = []    # List of deckIds

    # Add Deck to a User
    # Need to add restriction that we can't
    # add the owned deck until the deck is created
    def addOwnedDeck(self, deckId):

        # Append deckIds to User list of ownedDecks
        self.ownedDecks.append(deckId)

