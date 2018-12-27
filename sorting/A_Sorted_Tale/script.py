import utils
import sorts

bookshelf = utils.load_books('C:/Users/Jonathan/LambdaSchoolProjects/python-data-structures-alogos/sorting/A_Sorted_Tale/books_small.csv')

for book in bookshelf:
    print(book['title_lower'])
#end of for loop. 

def by_title_ascending (book_a, book_b):
    """
    This function will be used to compare two books and returns 
    true or false based off if book a is greater than book b 
    comparision done on the books  title_lower key. 
    """
    return book_a['title_lower'] > book_b['title_lower']
#end of by_title_ascending 

sort_1 = sorts.bubble_sort(bookshelf, by_title_ascending)
print(sort_1)