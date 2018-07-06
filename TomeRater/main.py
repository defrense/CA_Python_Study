from TomeRater import *
from populate import *
#running this script in -i interactive mode to use advanced featrues


def standard_user():
    print('A default Tome_Rater collection has been created\nPlease choose from below functions:\n')
    print('------------------------------------------------------------')
    print('a. Print Book Catalog     b. Print User List\nc. Print Most Read Book    d. Print Highest Rated Book ')
    print('------------------------------------------------------------')
    choice = input('\n  :').lower()

    if choice == 'a':
        Tome_Rater.print_catalog()
    elif choice == 'b':
        Tome_Rater.print_users()
    elif choice == 'c':
        print(Tome_Rater.most_read_book())
    elif choice == 'd':
        print(Tome_Rater.highest_rated_book())

def advanced_user():
    print('A default Tome_Rater collection has been created\n------------------------------------------------------------\n')
    print('Please manually call below available methods[e.g. Tome_Rater.print_catalog()]')
    print('\n\
            create_book(title, isbn, price)\n\
            create_novel(title, author, isbn, price)\n\
            create_non_fiction(title, subject, level, isbn, price)\n\
            add_book_to_user(book, email, rating)\n\
            add_user(name, email, user_books)\n\
            print_catalog()   print_users()   most_positive_user()\n\
            get_n_most_read_books(n)   get_n_most_expensive_books(n)\n')


print('\n\n\n\n\
=================================\nWELCOME TO TOME RATER APP\n=================================\n')
print('\n(A) Standard User                              (B)Advanced User\n\n\n\n')
user_mode = input('\nChoose Login type: ').lower()
if user_mode == 'a':
    standard_user()
elif user_mode == 'b':
    advanced_user()
else:
    print ('Invalid Choice!')
