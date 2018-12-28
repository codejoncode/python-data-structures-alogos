import utils
import sorts

bookshelf = utils.load_books(
    'C:/Users/Jonathan/LambdaSchoolProjects/python-data-structures-alogos/sorting/A_Sorted_Tale/books_small.csv')
bookshelf_v1 = bookshelf.copy()
bookshelf_v2 = bookshelf.copy()

long_bookshelf = utils.load_books('C:/Users/Jonathan/LambdaSchoolProjects/python-data-structures-alogos/sorting/A_Sorted_Tale/books_large.csv')

def by_title_ascending(book_a, book_b):
    """
    This function will be used to compare two books and returns 
    true or false based off if book a title_lower is greater than book b title_lower
    comparision done on the books  title_lower key. 
    """
    return book_a['title_lower'] > book_b['title_lower']
# end of by_title_ascending


def by_author_ascending(book_a, book_b):
    """
    This function will be used to compare two books and returns
    true or false based off if book a author_lower is greater than book b
    author_lower keys.  
    """
    return book_a['author_lower'] > book_b['author_lower']
# end of by_author_ascending


def by_total_length(book_a, book_b):
    """
    returns true if the sum of characters in title and author of book a is greater than those same values in book b. 
    else returns false. 
    """
    return len(book_a['author_lower']) + len(book_a['title_lower']) > len(book_b['author_lower']) + len(book_b['title_lower'])


sort_1 = sorts.bubble_sort(bookshelf_v1, by_title_ascending)
sort_2 = sorts.bubble_sort(bookshelf_v1, by_author_ascending)

sorts.quicksort(bookshelf_v2, 0, len(bookshelf_v2)-1, by_author_ascending)

sorts.quicksort(long_bookshelf, 0, len(long_bookshelf)-1, by_total_length)

for book in long_bookshelf:
    print(book['title'],book['author'], len(book['title']) + len(book['author']))
# end of for loop.