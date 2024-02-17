import sqlite3 as db
import csv
import json

# Establish the database and connection
conn = db.connect('BooksBase.db')

# Create a cursor to execute sql commands
click = conn.cursor()


# function for less future typing
def est(sql_command):
    # sql call
    click.execute(sql_command)


# function to execeutemany and commit changes
def dbc(insertion, access):
    # sql needs to click around to insert all data points parsed from csv
    click.executemany(insertion, access)
    # ensure changes are made to the database
    click.commit()



# ACCESS TABLE
# Contains Primary Key (Title) + url + availability

# Fresh start / delete table if present
est('''DROP TABLE IF EXISTS access''')

# create table in database
est('''CREATE TABLE access(
    ID INTEGER PRIMARY KEY,
    url TEXT,
    availability TEXT)''')

# open file and auto-close when done with it
with open(r'dotcomdata/bookdata.csv') as accessfile:

    # hold values parsed through
    access_sheet = csv.DictReader(accessfile)


    data_access = [(i['url'], i['availability'], i['title']) for i in access_sheet]


access_insertion = '''INSERT INTO access(
    id,
    url,
    availability,
    title) VALUES (?, ?, ?, ?)'''

dbc(access_insertion, data_access)



# BOOK TABLE
