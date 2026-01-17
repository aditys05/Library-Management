class Library:
    def __init__(self, listofbooks):
        self.books = listofbooks

    def show_books(self):
        print("\nThe books available in library are:\n ")
        for book in self.books:
            print(f"* {book}")

    def issue_book(self, bookname):
        if bookname in self.books:
            print(f"\nBook issued Successfully! Enjoy reading :{bookname}")
            self.books.remove(bookname)
        else:
            print("\nThis book is Not Available or issued to someone, please wait untill its available in the library.")

    def return_book(self, bookname):
        if bookname not in self.books:
            self.books.append(bookname)
            print(f"\nThank you for returning the book!")
        else:
            print("This book already exist in the library.")


class Students:
    def __init__(self, nameuser):
        self.users = nameuser


if __name__ == "__main__":
    username = int(input("Enter your Id number: "))
    user1 = Students(username)

    LibraryShelf = Library(
        ["Atomic Habits", "The Sixth Exinction", "Harry Potter", "Natsamrat", "Coding with ADITYA"])

welcom_Msg = """
    *** Welcome to the Great Library of ADITYA ***
            Press 1 for list of the books
            Press 2 for getting the book
            Press 3 for returning the book
            Press 4 for exit
            """

print(welcom_Msg)

while (True):
  try:
    choice = int(input("\nEnter you choice: "))
    
    if choice == 1:
        LibraryShelf.show_books()
    elif choice == 2:
        issue_book = input("Enter the book name you want to issue : ")
        LibraryShelf.issue_book(issue_book)
    elif choice == 3:
        rebook = input("Enter book name you want to return : ")
        LibraryShelf.return_book(rebook)
    elif choice == 4:
        print("\n\n\t***** THANK YOU FOR USING OUR LIBRARY ****\n")
        break
    else:
        print("Please enter the valid option.")
  except ValueError:
    print("Invalid Input.. PLease enter a number.")            