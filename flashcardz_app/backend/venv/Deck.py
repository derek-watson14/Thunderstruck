class Deck:

    def __init__(self, deckId, deckName, userId):
        self.deckId = deckId
        self.deckName = deckName
        self.ownedBy = userId
        self.attemptNumber = 0
        self.correctAnswers = 0
        self.cardCount = 0
        self.score = 0.0
        self.cardList = []      # List of card objects

    # Add a card to a Deck
    def addCard(self, cardId, deckId, frontText, backText):

        # Create a Card object
        newCard = Card(cardId, deckId, frontText, backText)

        # Append Card object to Deck cardlist attribute
        self.cardList.append(newCard)

class Card:
    def __init__(self, cardId, deckId, frontText, backText):
        self.cardId = cardId
        self.deckId = deckId
        self.frontText = frontText
        self.backText = backText
        self.correct = False

