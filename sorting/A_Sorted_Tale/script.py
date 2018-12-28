import utils
import sorts

bookshelf = utils.load_books('C:/Users/Jonathan/LambdaSchoolProjects/python-data-structures-alogos/sorting/A_Sorted_Tale/books_small.csv')
bookshelf_v1 = bookshelf.copy()

def by_title_ascending (book_a, book_b):
    """
    This function will be used to compare two books and returns 
    true or false based off if book a title_lower is greater than book b title_lower
    comparision done on the books  title_lower key. 
    """
    return book_a['title_lower'] > book_b['title_lower']
#end of by_title_ascending 
def by_author_ascending (book_a, book_b):
    """
    This function will be used to compare two books and returns
    true or false based off if book a author_lower is greater than book b
    author_lower keys.  
    """
    return book_a['author_lower'] > book_b['author_lower']
#end of by_author_ascending

sort_1 = sorts.bubble_sort(bookshelf_v1, by_title_ascending)
sort_2 = sorts.bubble_sort(bookshelf_v1, by_author_ascending)

for book in sort_2:
    print(book['author'])
#end of for loop. 
