import sqlite3 as db
import csv
import json

# Establish the database and connection
conn = db.connect('BooksBase.db')

# Create a cursor to execute sql commands
click = conn.cursor()


# function for less future typing
def est('''sql_command'''):
    # sql call
    click.execute('''sql_command''')


# function to execeutemany and commit changes
def dbc(insertion, data):
    # sql needs to click around to insert all data points parsed from csv
    click.executemany(insertion, data)
    # ensure changes are made to the database
    click.commit()



# ACCESS TABLE
# Contains Primary Key (id) + url + availability

# Fresh start / delete table if present
est('''DROP TABLE IF EXISTS access''')

# create table in database
est('''CREATE TABLE access(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    url TEXT,
    availability TEXT)''')

# open file to read and auto-close when done with it
with open(r'dotcomdata/bookdata.csv', 'r') as af:

# read through the csv
    access_sheet = csv.DictReader(af)

# hold all instances of iterating through 'url' and 'availbility'
    data_access = [(i['url'], i['availability']) for i in access_sheet]

# put values into the table
access_insertion = '''INSERT INTO access(
    url TEXT NOT NULL,
    availability TEXT NOT NULL) 
    VALUES (?, ?)'''

# sql, click through inserting all data as detailed into table and commit changes
dbc(access_insertion, data_access)



# BOOK TABLE
# CONTAINS title, product type, category, description, FOREIGN KEY (id)

# Fresh start / delete table if exists
est('''DROP TABLE IF EXISTS book''')

# create book table for database
est('''CREATE TABLE book(
    title TEXT NOT NULL, 
    product_type, 
    category, 
    description, 
    FOREIGN KEY (id)
        REFERENCES access (id)
)''')

with open (r'dotcomdata/bookdata.csv', 'r') as bf:

    book_sheet = csv.DictReader(bf)

# iterating through the csv and holding all instances as identified in i[]
    data_book = [(i['title'],
                i['product_type'],
                i['category'],
                i['description']) for i in book_sheet]

# insert data taken from csv and input into table for database
book_insertion = '''INSERT INTO book(
    title, 
    product type, 
    category,
    description)
    VALUES (?, ?, ?, ?)'''

# finish book table / commit changes
dbc(book_insertion, data_book)



# MONEY TABLE
# PRICE, TAX, AND PRICE INCL_EXCL TAX

# Fresh Start / Money Table:
est('''DROP TABLE IF EXISTS money''')

# Establish clean money table
est('''CREATE TABLE money(
    price_exl_tax,
    price_incl_tax,
    tax,
    price,
    FOREIGN KEY (id)
        REFERENCES access (id)
)''')



