import csv
"""
This code will load the current book shelf data from the csv file. 
"""

def load_books(filename):
    bookshelf = []
    with open(filename) as file: 
        shelf = csv.DictReader(file)
        for book in shelf: 
            
            bookshelf.append(book)
    return bookshelf