# Milestone 5: SQL Design

### List of tables:
- users
- decks
- cards
- cardscores

### Data Access Method Template
- **Name**:
- **Description**:
- **Parameters**:
- **return values**:
- **List of tests for verifying each access method**: 

-----

## User Table
- Table name: **users**
- Table Description: **Contains login information for all registered users**
- Fields
    - **id** = integer to serve as the primary key
    - **email** = string to hold the user's email address.
    - **password** = string to hold the user's hashed password.

#### User Data Access Methods:
- **Name**: Login
- **Description**: Verify a user exists, compare password hashes, return user object
- **Parameters**: email, password
- **return values**: user object containing all data for that user
- **List of tests for verifying each access method**: 

#### Tests:
1. Verify user profile is stored with an email and hashed  password
-Preconditions: Email and password are valid
-Steps:
    1.  Register a new user with the email: cool@test.edu and password = coolpassword (Create a new instance of the Users class)
    2.  Test that we can retrieve that new user's email from the database
    3.  Test that the new user's password is a hashed string (need to know what the expected hashed value is)


2. Verify that you cannot store a user account with a blank password (This is a edge-case check rather than a test we would run every time I think)
-Steps:
    1. Register a new user with an email: blank@test.edu and do not fill out the password field. 
    2. Test that we cannot retrieve the new user's email from the database.

-----

## Deck Table
- Table name: **decks**
- Table Description: **Contains all user created decks**
- Fields
    - **id**: integer to serve as the primary key
    - **name**: string that represents the name of this specific deck
    - **card_count**: integer that represents the number of cards the user has created in this deck
    - **owner_id**: Foreign Key that represents the corresponding id in the user table. This field links the deck to the user.

#### Deck Data Access Methods:

#### Tests:
1. Verify that the new blank deck is populated in the Decks table and the card_count is zero.
-Preconditions: Use an established user account
-Steps:
    1. Login as a user and create a new Deck called "Test Deck 1." (Create a new instance of the Deck class)
    2. Test that the name field = "Test Deck 1"
    3. Test that the card_count = 0.
    4. Test that we can retrieve the correct corresponding user email from the users table

2. Verify that the card_count is 0 when the Deck is first created

3. Verify that the card_count increments by 1 when a new card is created
-Steps:
    1. Login as a user and access "Test Deck 1"
    2. Create a new card with front and back text (Create a new instance of the Card class)
    3. Test that the card_count = 1 in the database


-----

## Card Table
- Table name: **cards**
- Table Description: **Contains all cards from all decks**
- Fields
    - **id**: integer to serve as the primary key
    - **front**: string that represents the flash card front text
    - **back**: string that represents the flash card back text
    - **deck_id**: Foreign Key that represents the corresponding id in the deck table. This field links the card to the deck.

#### Deck Data Access Methods:

#### Tests:
1. Verify that the new card is populated in the Cards table
-Preconditions: Using an established user account and already created a Deck
-Steps:
1. Login as a user and create a new card. (Create a new instance of the Card class)
2. Test that we can retrieve the card front and back text from the database
3. Test that we can retrieve the correct Deck name from the Deck table (from the database)


-----

## Cardscore Table
- Table name: **cardscores**
- Table Description: **Keeps track of an individual User's score on each card.  Contains 1 row for each User/Card combination.**
- Fields
    - **card_id**: card associated with this score, foreign key
    - **user_id**: user associated with this score, foreign key
    - **attempts**: string that represents the flash card front text
    - **correct**: string that represents the flash card back text
    - **last_attempt correct**: Foreign Key that represents the corresponding id in the deck table. This field links the card to the deck.


#### Cardscore Data Access Methods:

#### Tests: