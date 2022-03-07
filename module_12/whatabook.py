# import statements
import mysql.connector
from mysql.connector import errorcode

# database config object
config = {
    "user": "whatabook_user",
    "password": "MySQL8IsGreat!",
    "host": "127.0.0.1",
    "database": "whatabook",
    "raise_on_warnings": True
}

# main menu method
def show_menu():
    print("")
    print("\t\t==============================================")
    print("\t\t\t      MAIN MENU OPTIONS")
    print("\t\t==============================================")
    print("\t\t\t       1. View Books")
    print("\t\t\t       2. View Store Locations")
    print("\t\t\t       3. My Account")
    print("\t\t\t       4. Exit Program")
    print("\t\t==============================================")
    print("\n")

# check user choice and provide for error case
    while True: 
        user_choice = (input('Please type in the corresponding number and press enter: '))
        if user_choice == "1" or user_choice == "2" or user_choice == "3" or user_choice == "4":
            return int (user_choice)
        print("Please enter a valid choice, hint... it is 1, 2, 3, or 4 ")

# show the entire list of books to user 
def show_books(cursor):
    cursor.execute("SELECT book_id, book_name, author, details from book")

    bookList = cursor.fetchall()

    print("\n\n\n\n\n\n\n\n")
    print("\t\t ******************** BOOK LIST ********************")
    print("\n\n")

    for book in bookList:
        print("  Book Name: \t\t" + str(book[1]) + "\n  Author: \t\t" + str(book[2]) + "\n  Details: \t\t" + str(book[3]))
        print("")

# show locations, theres only 1 location in db
def show_locations(cursor):
    cursor.execute("SELECT locale from store")

    locationList = cursor.fetchall()

    print("\n\n")
    print("\t\t ******************** LOCATIONS ********************")
    print("\n\n")


    for location in locationList:
        print("  Locale : " + str(location[0]))
        print("")

# verify that the user has an account and account for typo
def validate_user():
    while True:
        print("\n")
        user_id = input("\t Please enter your user ID : ")
        if user_id == "1" or user_id == "2" or user_id == "3":
            return int (user_id)
        print("\n")
        print("Please enter a valid id, hint... it is 1, 2, or 3 ")

# print account options to user
def show_account_menu():
    print("")
    print("\t\t==============================================")
    print("\t\t\t      ACCOUNT OPTIONS")
    print("\t\t==============================================")
    print("\t\t\t 1. Wishlist")
    print("\t\t\t 2. Add book")
    print("\t\t\t 3. Back to main menu")
    print("\t\t==============================================")
    print("\n")

# let the user choose from menu and account for typo
    while True: 
        user_choice = (input('Please type in the corresponding number and press enter: '))
        if user_choice == "1" or user_choice == "2" or user_choice == "3":
            return int (user_choice)
        print("\n")
        print("Please enter a valid number, hint... it is 1, 2, or 3 ")

# show unique wishlist for user
def show_wishlist(cursor, user_id):
    cursor.execute("SELECT user.user_id, user.first_name, user.last_name, book.book_id, book.book_name, book.author " + 
                    "FROM wishlist " + 
                    "INNER JOIN user ON wishlist.user_id = user.user_id " + 
                    "INNER JOIN book ON wishlist.book_id = book.book_id " + 
                    "WHERE user.user_id = " + str(user_id))

    user_wishlist = cursor.fetchall()

    print("\n\n\n\n\n\n\n\n")
    print("\t\t ******************** YOUR WISHLIST ********************")
    print("\n\n")

    for book in user_wishlist:
        print("  Book Name: \t\t" + str(book[4]) + "\n  Author: \t\t" + str(book[5]))
        print("")

# show remaining books not in wishlist to user
def show_books_to_add(cursor, user_id):
    cursor.execute("SELECT book_id, book_name " +
            "FROM book " +
            "WHERE book_id NOT IN (SELECT book_id FROM wishlist WHERE user_id = " + str(user_id) + ")")

    available_booklist = cursor.fetchall()

    print("\n\n\n\n\n\n\n\n")
    print("\t\t ******************** AVAILABLE BOOKS ********************")
    print("\n\n")

    for book in available_booklist:
        print("  Book ID: \t\t" + str(book[0]) + "\n  Book name: \t\t" + str(book[1]))
        print("")


def add_book_to_wishlist(cursor, user_id, book_id):
    cursor.execute("INSERT INTO wishlist(user_id, book_id) VALUES(" + str(user_id) + "," + str(book_id) + ")")
    db.commit()

try:

    db = mysql.connector.connect(**config) 
    cursor = db.cursor()
    print("\n")
    print("******************** Welcome to the whattabook helper ********************")
    print("\n")

#map out gui for user
    while True:
        choice = show_menu()

        if choice == 1:
            show_books(cursor)
        elif choice == 2:
            show_locations(cursor)
        elif choice == 3:
            user_id = validate_user()
            while True:
                users_menu = show_account_menu()
                if (users_menu == 1):
                    show_wishlist(cursor, user_id)
                elif users_menu == 2:
                    show_books_to_add(cursor, user_id)
                    try:
                        book_id = int(input("\t Enter the book ID that you want to add or press any other key to go back: "))
                    except:
                        print('Please enter a valid number')
                        continue
                    add_book_to_wishlist(cursor,user_id,book_id)
                elif users_menu == 3:
                    break
        elif choice == 4:
            print("")
            print('Thank you for visiting!\n Goodbye!')
            print("")
            break
        
# error handling
except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("Invalid username or password")
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("Invalid database")
    else:
        print(err)
finally:
    db.close()
