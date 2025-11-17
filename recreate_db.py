import sqlite3
import os

if os.path.isfile("./prod.db"):
    confirmation = input("Are you sure you want to recreate database? (y/n) ")
    if confirmation.lower() != "y":
        print("Exiting...")
        exit()
    print("Okee dokey")
    os.remove("./prod.db")

conn   = sqlite3.connect("prod.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS ROUTINES (
               ID INTEGER PRIMARY KEY,
               NAME TEXT NOT NULL,
               DESCRIPTION TEXT,
               CREATED_AT TIMESTAMP);
""")
conn.commit()

cursor.execute("INSERT INTO ROUTINES (NAME, DESCRIPTION) VALUES (?, ?)", ("First test routine", "This is it, it's really the first one."))
conn.commit()