class Library:

    def __init__(self, list, name):
        self.bookslist = list
        self.name = name
        self.lenddict = {}

    def dispbooks(self):
        print(f"we have following books in our library {self.name}")

        for i in self.bookslist:
            print(i)

    def lendbooks(self, user, book):
        if book not in self.lenddict.keys():
            self.lenddict.update({book:user})
            print("Lender book database has been updated.")

        else:
            print(f"the book is already been issued to {self.lenddict[book]}")

    def addbook(self, book):
        self.bookslist.append(book)
        print("Book has been added.")

    def returnbook(self, book):
        self.lenddict.pop(book)

if __name__ == '__main__':
    ayush = Library(['History', 'Indian Economy', 'geography', 'polity'], "Ayush")

    while(1):
        print(f"Welcome to the {ayush.name} Library. Enter your choice to continue :-")
        print("1. Display books")
        print("2. Lend a book")
        print("3. Add a book")
        print("4. Return a book")

        user_choice = int(input())

        if user_choice == 1:
            ayush.dispbooks()

        elif user_choice == 2:
            book = input("enter the name of the book you want to lend.")
            name = input("enter your name")
            ayush.lendbooks(name, book)

        elif user_choice == 3:
            book = input("enter the name of the book you want to add.")
            ayush.addbook(book)

        elif user_choice == 4:
            book = input("enter the name of the book you want to return.")
            ayush.returnbook(book)

        else:
            print("Not a valid option")

        print("press q to quit, c to continue")
        choice = "blank"

        while(choice != 'q' and choice!= 'c' ):
            choice = input()
            if choice == 'q':
                exit() # exit will stop the execution.

            elif choice == 'c':
                continue

            else:
                continue
