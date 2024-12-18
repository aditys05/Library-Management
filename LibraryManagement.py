class Library:
    def __init__(self, listOfBooks):
        self.books = listOfBooks

    def showbooks(self):
        print("\n\tThe books available in library are:\n ")
        for book in self.books:
            print(f"\t\t* {book}")

    def issueBook(self, bookname):
        if bookname in self.books:
            print(f"\nBook is issued! Enjoy reading...{bookname}")
            self.books.remove(bookname)
        else:
            print(
                "\nThis book is Not Available or issued to someone wait untill if available in library ")

    def returnbook(self, bookname):
        if bookname not in self.books:
            self.books.append(bookname)
            print(f"\nThank you for returning the book! ")


class Students:
    def __init__(self, nameuser):
        self.users = nameuser


if __name__ == "__main__":
    username = int(input("Enter your Id number: "))
    user1 = Students(username)

    LibraryShelf = Library(
        ["Bajirao", "Ek purn apurn", "3 hazar taake", "Natsamrat", "Coding with ADITYA"])

welcomMsg = '''
    *** Welcome to the Great Library of ADITYA ***
            Press 1 for list of the books
            Press 2 for getting the book
            Press 3 for returning the book
            Press 4 for exit
            '''

print(welcomMsg)
while (True):

    userinp = int(input("\n\nEnter you choice : "))
    if userinp > 4:
        print("\n\t\t Enter correct choice... ")
    elif userinp == 1:
        LibraryShelf.showbooks()
    elif userinp == 2:
        issuebook = input("Enter the book name: ")
        LibraryShelf.issueBook(issuebook)
    elif userinp == 3:
        rebook = input("Enter book name : ")
        LibraryShelf.returnbook(rebook)
    elif userinp == 4:
        print("\n\n\t***** THANK YOU FOR USING OUR LIBRARY ****\n")
        break
s