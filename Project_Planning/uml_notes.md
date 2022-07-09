User Class
-userID: int
-username: String
-password: String
-ownedDecks: List of deckIDs?
-likedDecks: List of deckIDs?

Deck Class (Deck is a composite of Cards)
-deckID: int
-deckName: String
-ownedBy: int (userID)
-attemptNumber: int
-correctAnswers: int
-cardCount: int
-score: float
-cardList: List of cardIDs in attempt in the order the deck is presented

-addCard()
-updateCorrectAnswers()
-calcScore(int correctAnswers, int cardCount)
-shuffleDeck()
-showNextCard()?
-showPrevCard()?
-makePublic()

Card Class (Card is a component of Deck)
-cardID: int
-deckID: int
-frontText: String
-backText: String
-correct: Boolean

-cardCorrect()

