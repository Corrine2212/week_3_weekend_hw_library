from models.book import *

book1 = Book("Seven Husbands of Evelyn Hugo", "Taylor Jenkins Reid", "Romance", "Aging and reclusive Hollywood movie icon Evelyn Hugo is finally ready to tell the truth about her glamorous and scandalous life. But when she chooses unknown magazine reporter Monique Grant for the job, no one is more astounded than Monique herself.  Why her? Why now?...")
book2 = Book("I'm Glad My Mom Died", "Jeanette McCurdy", "Memoir", "A heartbreaking and hilarious memoir by iCarly and Sam & Cat star Jennette McCurdy about her struggles as a former child actor_including eating disorders, addiction and a complicated relationship with her overbearing mother...")
book3 = Book("The Song of Achilles", "Madeline Miller", "Historical Fiction", "Greece in the age of heroes. Patroclus, an awkward young prince has been exiled to the court of King Peleus and his perfect son Achilles. By all rights their paths should never cross, but Achilles takes the shamed prince as his friend, and as they grow into young men skilled in the arts of war and medicine their bond blossoms into something deeper.")
books = [book1, book2, book3]

def add_new_book(book_to_add):
    books.append(book_to_add)

def delete_book(book_title):
    book_to_delete = None
    for book in books:
        if book.title == book_title:
            book_to_delete = book
            break

    books.remove(book_to_delete)
