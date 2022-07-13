from Deck import Deck

# Create a User
user1 = User('username1', 'password1')

# Create an Empty Deck
deck1 = Deck('D1', 'Test Deck', 'user1')

# Add Deck to User Profile
user1.addOwnedDeck('D1')

# Create a Card in the Deck
deck1.addCard('C1', 'D1', 'What day is it today?', 'Saturday')

print("User Attributes")
print(vars(user1))

print("Deck1 Attributes")
print(vars(deck1))

print("Card Object Contained in Deck1")
print(deck1.cardList)
