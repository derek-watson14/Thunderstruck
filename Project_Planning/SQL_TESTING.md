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
            3. Check that the user object contains the correct email and a matching password hash
            4. Check that the user is logged in
        Expected result
            The email and password hash of the successfully returned user matches those input for the test
        Post-conditions
            User is validated with database and successfully signed into their account.
            The account session details are logged in database. 
	    Logged in user can access protected webpages with @login-required decorator
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
            3. Check that the new user's password is a hashed string (is not equal to the original password string)
            4. Check that the hashed string in the DB matches the string from hashing the plain text password
        Expected result
            Test emaail and a hashed password are in the DB; test that hash matches the hash the test password produces
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
    - ###### Verify that user decks are stored in the database
        ```
        Description
            Test that we can view all of the user's decks
        Pre-conditions
            The user is logged-in and has existing decks
        Test steps
            1. Login the user and create 2 new decks
            2. Check that we can retrieve the list of all decks - both pre-existings decks (deck names) and those previously created for this user from the database.
        Expected result
           We view the names of all decks in the database query - both pre-existing decks and those created as part of the test
        Post-conditions
           2 new decks are created with expected columns in the database that are linked to this user's account through the owner_id
        ```
<br>

- **Name**: Deck Overview
- **Description**: Return a single deck and all associated cards and card scores. Deck name can be edited and edit card buttons will appear if user owns this deck
- **Parameters**: user_id, deck_id
- **return values**: deck object (name, id, card count), list containing all associated cards, card score for all cards
- **List of tests for verifying access method**: 
    - ###### Verify that deck name changes are stored in the database
        ```
        Description
            Test that we can view the updated Deck name after it is updated
        Pre-conditions
            The user owns a deck
        Test steps
            1. Change the name of the owned  deck through the Deck Overview "deck name edit" functionality.
            2. Check that we can retrieve the updated name for this deck from the database
        Expected result
            We view the updated deck name in the database query 
        Post-conditions
             The deck name is updated in the Deck table
         ```
- **NOTE:** We list additional tests in the Study Deck access method below. These tests can also be replicated for the Deck Overview access method.
<br>

- **Name**: Study Deck (also includes Cards and CardScores table components)
- **Description**: Return a single deck and all of that deck's cards so they can be reviewed by a user and scored based on an attempt
- **Parameters**: user_id, deck_id
- **return values**: deck object (name, id, card count) and list containing all associated cards
- **List of tests for verifying access method**:
    - ###### Verify that cards can be studied and scored 
        ```
        Description
            Test that all of the cards within a deck can be viewed, studied, and scored by logged in user.
        Preconditions: 
            Use an established user account with a previously created deck with 5 cards
        Test Steps:
            1. Login as user and select deck with 5 established cards
            2. Navigate to Study Deck route
	    3. Check that the card_count = 5 in the database query for that deck and 5 cards are displayed in the UI to study
	    4. Check that the front of each card matches the text added in the database as previously created by user for that decks.id
            5. Check that the back of the card (answer) can be displayed by clicking on the card and user can designate a correct or incorrect score for all cards associated with deck_id
        Expected result
            We view a card_count field of 5 in the database and view cards in UI with correct front and back text for selected decks.id
        Post-conditions
            The Deck exists in the database and has 5 cards associated with it; card_scores is updated with study attempt
        ```

    - ###### Verify the card count and list of cards when the Deck has cards
        ```
        Description
            Verify that the card_count increments by 1 when a new card is created
        Preconditions:
            Use an established user account and existing blank deck
        Test Steps:  
            1. Create a new card with front and back text (Create a new instance of the Card class)
            2. Navigate to Study Deck
            3. Check that the card_count = 1 and can view the updated list of cards associated with the deck in the database query
     	Expected Result
		We view a card_count of 1 can view the the front and back text of the existing card.
        Post-conditions
            The Card Table is updated with the new card.
        ```
<br>

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
    - ###### Verify that user can edit a card
        ```
        Description
            Verify that if a card exists and logged in user clicks "edit" and changes the front text, the card is updated in the database
        Pre-conditions
            There is a logged-in user with an existing deck and 1 card in the deck
        Test steps
            1. Update the front text of the card
            2. Check that the database has the updated front text of the card.
	    3. Check that the card_count for that deck remains the same in the database 
        Expected result
            The database value of the front text of the card is updated.
        Post-conditions
	    The card table is updated and the deck table remains in its original state
        ```
<br>

- **NOTE:** Deck Overview and Study Deck also access the Card table. These methods and their tests are reviewed in the **Decks Table** section above.
<br>


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
    - ###### Verify that the \<*correct*> field is properly updated in the database
        ```
        Description
            Test that when a logged in user clicks correct or incorrect in the app, the db is updated properly
        Pre-conditions
            A valid user is logged-in and has an existing deck with 2 cards
        Test steps
            1. A logged in user selects via the UI that an answer was correct for card #1 and incorrect for card #2.
            2. Check that the correct field is properly updated for those two cards in the database query
        Expected result
            The correct field for card #1 = True. The correct field for card #2 = False.
        Post-conditions
            The cardscores table is updated with the new values 
        ```

- **NOTE:** The cardscore table is also accessed in Deck Overview. This method and its tests are reviewed in the **Decks Table** section above.
<br>
