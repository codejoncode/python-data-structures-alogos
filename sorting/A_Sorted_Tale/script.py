import utils
import sorts

bookshelf = utils.load_books('C:/Users/Jonathan/LambdaSchoolProjects/python-data-structures-alogos/sorting/A_Sorted_Tale/books_small.csv')

for book in bookshelf:
    print(book['title'])