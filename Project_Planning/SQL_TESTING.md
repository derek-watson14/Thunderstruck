# Milestone 5: SQL Design

### List of tables:
- users
- decks
- cards
- cardscores

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
- **Description**: Log a user in by getting data from an HTML form and verifying their password
- **Parameters**: email, password
- **return values**: user object containing all data for that user
- **List of tests for verifying access method**: 
    - ###### Verify that login is not possible when an email is not stored in the user table
        ```
        Description
            Test that you cannot login with an email not stored in the DB
        Pre-conditions
            The email used for the test is not in the DB
        Test steps
            1. Log in with an email known to not be in the DB
            2. Check that NULL is returned
            3. Check that the user is NOT logged in
        Expected result
            An error message is displayed on the screen and the user is NOT logged in
        Post-conditions
            The user remains on the login page but a message is desplayed indicating the specified user was not found.
        ```
    - ###### Verify that login returns the correct user and logs them in
        ```
        Description
            Test that when logging in, the correct user is returned from the database
        Pre-conditions
            Email and password are valid at submission and correct to a known user
        Test steps
            1. Log in with user information that is known to exist in the db
            2. Check that a user object is returned
            3. Check that that user object contains the correct email and a massing password hash
            4. Check that the user is logged in
        Expected result
            The email and password hash of the successfully returned user match those input for the test
        Post-conditions
            User is validated with database and successfully signed into their account.
            The account session details are logged in database. 
        ```

<br>

- **Name**: Register
- **Description**: Register a new user in the database by getting input from an HTML form
- **Parameters**: email, password1, password2 (must match password1)
- **return values**: If user already exists, redirect. Else return created user object
- **List of tests for verifying access method**: 
    - ###### Verify user profile is stored with an email and hashed password
        ```
        Description
            Test that the user's data has been correctly stored
        Pre-conditions
            Email and password are valid at submission
        Test steps
            1. Register a new user with a known test email and password
            2. Check that we can retrieve that new user's email from the database
            3. Check that the new user's password is a hashed string (need to know what the expected hashed value is)
            4. Check that the hashed string in the DB matches the string from hashing the plain text password
        Expected result
            Test emaail and a hashed password are in the DB, that hash should match the hash the test password produces
        Post-conditions
            User is created with the expected credentials within the database
        ```
<br>

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
- **Name**: My Decks
- **Description**: Return all decks created by a user to populate the users account page
- **Parameters**: user_id
- **return values**: list of decks owned by the user
- **List of tests for verifying access method**: 
    - ###### [ USE CASE NAME ]
        ```
        Description
            [ TO DO ]
        Pre-conditions
            [ TO DO ]
        Test steps
            1. [ TO DO ]
            2. [ TO DO ]
        Expected result
            [ TO DO ]
        Post-conditions
            [ TO DO ]
        ```
<br>

- **Name**: Deck Overview
- **Description**: Return a single deck and all associated cards and card scores. Deck name can be edited and edit card buttons will appear if user owns this deck
- **Parameters**: user_id, deck_id
- **return values**: deck object (name, id, card count), list containing all associated cards, card score for all cards
- **List of tests for verifying access method**: 
    - ###### [ USE CASE NAME ]
        ```
        Description
            [ TO DO ]
        Pre-conditions
            [ TO DO ]
        Test steps
            1. [ TO DO ]
            2. [ TO DO ]
        Expected result
            [ TO DO ]
        Post-conditions
            [ TO DO ]
        ```
<br>

- **Name**: Study Deck
- **Description**: Return a single deck and all of that deck's cards so they can be reviewed by a user
- **Parameters**: user_id, deck_id
- **return values**: deck object (name, id, card count) and list containing all associated cards
- **List of tests for verifying access method**:
    - ###### [ USE CASE NAME ]
        ```
        Description
            [ TO DO ]
        Pre-conditions
            [ TO DO ]
        Test steps
            1. [ TO DO ]
            2. [ TO DO ]
        Expected result
            [ TO DO ]
        Post-conditions
            [ TO DO ]
        ```
<br>


#### Deck Tests:
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

#### Card Data Access Methods:
- **Name**: Edit/Create Card
- **Description**: Edit or create a card, if the logged in user owns the deck. If card_id is passed edit a card, if not create a card
- **Parameters**: user_id, deck_id, optional: card_id
- **return values**: none
- **List of tests for verifying access method**:
    - ###### [ USE CASE NAME ]
        ```
        Description
            [ TO DO ]
        Pre-conditions
            [ TO DO ]
        Test steps
            1. [ TO DO ]
            2. [ TO DO ]
        Expected result
            [ TO DO ]
        Post-conditions
            [ TO DO ]
        ```
<br>

- **NOTE:** Other methods that access data from the cards table include Deck Overview, Edit Deck and Study Deck. These methods and their tests are reviewed in the **Decks Table** section above.
<br>

#### Card Tests:
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
- **Name**: Indicate Correct/Incorrect Button
- **Description**: When using the study deck function, after flipping a card a user can indicate if their answer was correct or incorrect. The data is sent to the server
- **Parameters**: user_id, card_id, correct (boolean)
- **return values**: deck object (name, id, card count) and list containing all associated card object
- **List of tests for verifying access method**:
    - ###### [ USE CASE NAME ]
        ```
        Description
            [ TO DO ]
        Pre-conditions
            [ TO DO ]
        Test steps
            1. [ TO DO ]
            2. [ TO DO ]
        Expected result
            [ TO DO ]
        Post-conditions
            [ TO DO ]
        ```
<br>


- **NOTE:** Deck overview also accesses the cardscore table. This method and it's tests are reviewed in the **Decks Table** section above.
<br>

#### Cardscore Tests: