# Initial List of Tests

Website Page Transitions
- After you log-in, does it bring you to the "My Decks" Homepage?
- Does hitting "Edit Deck" on the My Decks Homepage bring you to the Edit Deck page?
- Does hitting "Create Deck" on the My Decks Homepage bring you to the Create Deck page?

Registration/Login Credentials
- Does the login page recognize old credentials (users who have regististered previously?)?
- If the user's credentials are not in the SQL database, is the user prompted to Register?
- Does the logout button on the Homepage actually log you out?
- Are the username's constraints that the username is not null and unique working properly?
- Are the password's constraint that it is not null working properly?
- Is the hash of hte password stored in the SQL database?

Working with the Decks
- Does the "shuffle" flashcard button actually change the order of the cards?
- Does "Next" bring you to a different card?
- Does "Previous" bring you to the last card?
- Can you view the deck that you created?
- Can you view decks that you did not create?
- Can you view only other user's public decks?

Reviewing Incorrect Answers Only
- When you review the deck a seond time, does it show only the subset of cards you got incorrect the first time?
- When you review the deck a thrird time, does it show only the subset of cards you got incorrect the second time?

Creating and Editing Decks
- Is the full inputted flash card question and answer inputted by the user displayed?
- Does every question have an answer, and vice-versa?
- If you edit a card after you already created it, does is the new text correctly displayed?

Calculations
- Does the user's number of "correct answers" information that is displayed  truely represent the correct number of correct answers.
- Does the user's score reflect the number of correct answers as a percentage of all cards in the deck?
- Does the attempt field accurately represent the number of times the user has gone through that deck?
- These tests above apply to both the first attempt through a deck and the repeat attempts when you review incorrect answers only

Website Header and Body Text
- Does the webpage render the correct website banner text?

User Inputs
- Is the full inputted flash card question and answer inputted by the user displayed?
- Does every question have an answer, and vice-versa?
-

