import sqlite3
import os


def create_db(dbname):
     """
     create_db creates a new database file of a specified name with table structure from ERD

     Parameters:
     -----------
     dbname : str 
          Name of db to be created
     """
     con = sqlite3.connect(dbname)
     cursor = con.cursor()

     create_tables = """
     CREATE TABLE IF NOT EXISTS Users (
          user_id INTEGER PRIMARY KEY,
          email TEXT NOT NULL UNIQUE,
          password TEXT NOT NULL
     );

     CREATE TABLE IF NOT EXISTS Decks (
          deck_id INTEGER PRIMARY KEY,
          deck_name TEXT NOT NULL,
          card_count INTEGER
     );

     CREATE TABLE IF NOT EXISTS Cards (
          card_id INTEGER PRIMARY KEY,
          front_text TEXT,
          back_text TEXT,
          fk_deck_id INTEGER NOT NULL,
          FOREIGN KEY (fk_deck_id) REFERENCES Decks(deck_id)
     );

     CREATE TABLE IF NOT EXISTS CardScores (
          attempts INTEGER,
          correct INTEGER,
          fk_user_id INTEGER NOT NULL,
          fk_card_id INTEGER NOT NULL,
          FOREIGN KEY (fk_user_id) REFERENCES Users(user_id),
          FOREIGN KEY (fk_card_id) REFERENCES Cards(card_id),
          PRIMARY KEY (fk_user_id, fk_card_id)
     );

     CREATE TABLE IF NOT EXISTS OwnedDecks (
          fk_owner_id INTEGER NOT NULL,
          fk_deck_id INTEGER NOT NULL,
          FOREIGN KEY (fk_owner_id) REFERENCES Users(user_id),
          FOREIGN KEY (fk_deck_id) REFERENCES Decks(deck_id),
          PRIMARY KEY (fk_owner_id, fk_deck_id)
     );

     CREATE TABLE IF NOT EXISTS LikedDecks (
          fk_liker_id INTEGER NOT NULL,
          fk_deck_id INTEGER NOT NULL,
          FOREIGN KEY (fk_liker_id) REFERENCES Users(user_id),
          FOREIGN KEY (fk_deck_id) REFERENCES Decks(deck_id)
          PRIMARY KEY (fk_liker_id, fk_deck_id)
     );
     """

     print("Creating database tables...\n")

     cursor.executescript(create_tables)
     con.commit()

     cursor.execute("SELECT name FROM sqlite_schema WHERE type='table';")
     print("Created tables: ", cursor.fetchall())
     con.close()


def delete_db(dbname):
     """
     delete_db deletes a database file of a specified name

     Parameters:
     -----------
     dbname : str 
          Name of db to be deleted
     """
     os.remove(dbname)
     print(f"Database {dbname} deleted")


def fill_db(dbname):
     """
     fill_db fills an existing database file of a specified name with dumy data

     Parameters:
     -----------
     dbname : str 
          Name of db to be deleted
     """
     con = sqlite3.connect(dbname)
     cursor = con.cursor()


     add_data = """
     INSERT INTO Users (email, password)
     VALUES
          ("jack@test.com", "password"),
          ("jane@test.com", "1234asdf");
     
     INSERT INTO Decks (deck_name, card_count)
     VALUES
          ("Jack's Deck", 2),
          ("Jane's Deck", 0);
     
     INSERT INTO Cards (front_text, back_text, fk_deck_id) 
     VALUES
          ( "What is my name?", "Jack", 1 ),
          ( "What is Jane's name?", "Jane", 1 );

     INSERT INTO CardScores (attempts, correct, fk_user_id, fk_card_id) 
     VALUES
          ( 5, 4, 1, 1 ),
          ( 5, 3, 1, 2 ),
          ( 2, 2, 2, 1 ),
          ( 2, 2, 2, 2 );

     INSERT INTO OwnedDecks (fk_owner_id, fk_deck_id) 
     VALUES
          (1, 1),
          (2, 2);

     INSERT INTO LikedDecks (fk_liker_id, fk_deck_id) 
     VALUES
          (2, 1);
     """

     cursor.executescript(add_data)
     con.commit()

     con.close()
