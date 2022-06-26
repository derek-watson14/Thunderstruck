import sqlite3
import sys
import os

# Creates tables in an SQLite DB
# How to use:
# Run on existing DB: `python create_db.py`
# To delete old DB and remake: `python create_db.py --remake`

DB_NAME = "flashcardz_db.sqlite"

if len(sys.argv) == 2:
     if sys.argv[1] == "--remake":
          answer = input("Permenantly delete existing version of database? (y/n) ")
          if answer.lower() == "y": 
               os.remove(DB_NAME)
               print("> Existing database deleted")
          else:
               print("> Deletion cancelled")


print("Creating database tables...")

con = sqlite3.connect(DB_NAME)

cursor = con.cursor()

create_tables = """
CREATE TABLE IF NOT EXISTS Users (
     user_id INTEGER PRIMARY KEY,
     username TEXT NOT NULL UNIQUE,
     password TEXT NOT NULL UNIQUE,
     email TEXT,
     first_name TEXT,
     last_name TEXT
);

CREATE TABLE IF NOT EXISTS Decks (
     deck_id INTEGER PRIMARY KEY,
     deck_name TEXT NOT NULL,
     card_count INTEGER
);

CREATE TABLE IF NOT EXISTS Cards (
     card_id INTEGER PRIMARY KEY,
     deck_name TEXT NOT NULL,
     card_count INTEGER,
     fk_deck_id INTEGER NOT NULL,
     FOREIGN KEY (fk_deck_id) REFERENCES Decks(deck_id)
);

CREATE TABLE IF NOT EXISTS CardScores (
     card_score_id INTEGER PRIMARY KEY,
     attempts INTEGER,
     correct INTEGER,
     percentage INTEGER,
     fk_user_id INTEGER NOT NULL,
     fk_card_id INTEGER NOT NULL,
     FOREIGN KEY (fk_user_id) REFERENCES Users(user_id),
     FOREIGN KEY (fk_card_id) REFERENCES Cards(card_id)
);

CREATE TABLE IF NOT EXISTS OwnedDecks (
     owned_deck_id INTEGER PRIMARY KEY,
     fk_owner_id INTEGER NOT NULL,
     fk_deck_id INTEGER NOT NULL,
     FOREIGN KEY (fk_owner_id) REFERENCES Users(user_id),
     FOREIGN KEY (fk_deck_id) REFERENCES Decks(deck_id)
);

CREATE TABLE IF NOT EXISTS LikedDecks (
     liked_deck_id INTEGER PRIMARY KEY,
     fk_liker_id INTEGER NOT NULL,
     fk_deck_id INTEGER NOT NULL,
     FOREIGN KEY (fk_liker_id) REFERENCES Users(user_id),
     FOREIGN KEY (fk_deck_id) REFERENCES Decks(deck_id)
)
"""

cursor.executescript(create_tables)
con.commit()

cursor.execute("SELECT name FROM sqlite_schema WHERE type='table';")

print("List of tables in database: ")
print(cursor.fetchall())

con.close()