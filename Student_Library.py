class Library:
    def __init__(self, listOfBooks):
        self.books = listOfBooks

    def displayAllBooks(self):
        print("List of available books are: ")
        for book in self.books:
            print("* ", book)

    def borrowBook(self, nameOfBook):
        if nameOfBook in self.books:
            print(
                f"You have borrowed book of {nameOfBook} , keep it safe and return it in 60 days.\n"
            )
            self.books.remove(nameOfBook)
            return True
        else:
            print(
                f" Sorry the book of {nameOfBook} is not available or someone has borrowed it\n"
            )
            return False

    def returnBook(self, nameOfBook):
        print(f"Thanks for Returning book of {nameOfBook}, Hope you have enjoyed it\n")
        self.books.append(nameOfBook)


class Student:
    def rqbook(self):
        self.book = input("Enter the name of Your Book : ")
        return self.book

    def rtbook(self):
        self.book = input("Enter the name of Your Book : ")
        return self.book


try:
    if __name__ == "__main__":

        CentralLibrary = Library(
            [
                "DevOps",
                "Data Structure & Algorithm Classes",
                "System Design",
                "Java Backend Developer" "Full Stack Development with React & Node JS",
                "Complete Data Science Program",
                "Data Structure & Algorithm-Self Paced",
                "Data Structures & Algorithms in Python.",
            ]
        )

        student = Student()
        while True:

            welcomemsg = """\n\t========Welcome to college Library========\n"""
            menu = """' Select Your Choice : 
            1.To Display the list of Books
            2.To Borrow a book.
            3.To return/add a book.
            4.Exit.
            
            """

            print(welcomemsg)
            print(menu)
            a = int(input("Enter your Choice :"))
            print("\n")
            if a == 1:

                CentralLibrary.displayAllBooks()
            elif a == 2:
                CentralLibrary.borrowBook(student.rqbook())
            elif a == 3:
                CentralLibrary.returnBook(student.rtbook())
            elif a == 4:
                exit()
            elif a > 4:
                print("\nplease choose input in between 1-4 :")
            elif a < 0:
                print("\nplease choose input in between 1-4 :")

except Exception as e:
    print("\nYou have enter invalid input\n")

