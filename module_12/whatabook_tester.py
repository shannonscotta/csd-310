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

def main_menu():
    print("")
    print("\t      WELCOME TO THE MAIN MENU ")
    print("\t      ======================== \n")
    print("\t      1. View Books")
    print("\t      2. View Store Locations")
    print("\t      3. My Account")
    print("\t      4. Exit Program")
    print("\n\n")

    while True: 
        user_choice = (input('Please select the corresponding number to choose an option: '))
        if user_choice == "1" or user_choice == "2" or user_choice == "3" or user_choice == "4":
            return int (user_choice)
        print("Please choose a valid number,hint: choose 1, 2, 3, or 4")

def display_books(cursor):
    cursor.execute("SELECT book_id, book_name, author, details from book")

    bookList = cursor.fetchall()
    print("\t ********** SHOWING ALL BOOKS **********")

    for book in bookList:
        print("  Book Name: " + str(book[1]) + "\n  Author: " + str(book[2]) + "\n  Details: " + str(book[3]))
        print("")
        

def display_locations(cursor):
    cursor.execute("SELECT locale from store")

    locationList = cursor.fetchall()
    print("\t********** SHOWING ALL LOCATIONS **********")

    for location in locationList:
        print("  Locale : " + str(location[0]))
        print("")

def prompt_userID():
    while True:
        user_id = input('\t Please enter your user ID: ')
        if user_id == "1" or user_id == "2" or user_id == "3":
            return int (user_id)
        print("")
        print('\t Please choose a valid number,hint: choose 1,2, or 3')

def display_verified_user_menu():
    print("Welcome to your account")
    print("\t1. Wishlist")
    print("\t2. Add book")
    print("\t3. Back to main menu")

    while True: 
        user_choice = (input('Please select the corresponding number to choose an option: '))
        if user_choice == "1" or user_choice == "2" or user_choice == "3":
            return int (user_choice)
        print("Please choose a valid number,hint: choose 1, 2, or 3")

def display_wishlist(cursor, user_id):
    cursor.execute("SELECT user.user_id, user.first_name, user.last_name, book.book_id, book.book_name, book.author " + 
                    "FROM wishlist " + 
                    "INNER JOIN user ON wishlist.user_id = user.user_id " + 
                    "INNER JOIN book ON wishlist.book_id = book.book_id " + 
                    "WHERE user.user_id = " + str(user_id))

    user_wishlist = cursor.fetchall()

    print("\t********** SHOWING WISHLIST **********")

    for book in user_wishlist:
        print("  Book Name: " + str(book[4]) + "\n  Author: " + str(book[5]))
        print("")

def display_avaliable_books(cursor, user_id):
    cursor.execute("SELECT book_id, book_name " +
            "FROM book " +
            "WHERE book_id NOT IN (SELECT book_id FROM wishlist WHERE user_id = " + str(user_id) + ")")

    available_booklist = cursor.fetchall()

    print("\t********** SHOWING AVAILABLE BOOKS**********")

    for book in available_booklist:
        print("  Book ID: " + str(book[0]) + "\n  Book name: " + str(book[1]))
        print("")

def add_book_to_wishlist(cursor, user_id, book_id):
    cursor.execute("INSERT INTO wishlist(user_id, book_id) VALUES(" + str(user_id) + "," + str(book_id) + ")")
    db.commit()

try:

    db = mysql.connector.connect(**config) 
    cursor = db.cursor()
    
    print("\n\n\n\n\n\n\n\n")
    print("********** Welcome to the whattabook helper **********")

    while True:
        choice = main_menu()

        if choice == 1:
            display_books(cursor)
        elif choice == 2:
            display_locations(cursor)
        elif choice == 3:
            user_id = prompt_userID()
            while True:
                users_menu = display_verified_user_menu()
                if (users_menu == 1):
                    display_wishlist(cursor, user_id)
                elif users_menu == 2:
                    display_avaliable_books(cursor, user_id)
                    try:
                        book_id = int(input("\t Enter the book ID that you want to add or press any other key to cancel: "))
                    except:
                        print('Please enter a valid number')
                        continue
                    add_book_to_wishlist(cursor,user_id,book_id)
                elif users_menu == 3:
                    break
        elif choice == 4:
            print("")
            print("Goodbye!")
            print("")
            break
except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("Invalid username or password")
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("Invalid database")
    else:
        print(err)
finally:
    db.close()



# display_avaliable_books(cursor, 1)
# display_books(cursor)
# display_locations(cursor)
# prompt_userID()