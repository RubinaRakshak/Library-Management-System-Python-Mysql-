
class  Library:
    def __init__(self,listofbooks,name):
        self.availablebooks=listofbooks
        self.name=name
        

    def displayAvailablebooks(self):
        print(f"we have following books in our {self.name} library and the books are {self.availablebooks}")
        print(f"the books we have in our {self.name} library are:")
        for book in self.availablebooks:
            print(book)

        #print(f"we have following books in our {self.name} library and the books are {self.availablebooks}")


    def lendbook(self,requestedBook):
        if requestedBook in self.availablebooks:
            print("you have now borrowed it:")
            self.availablebooks.remove(requestedBook)
        else:
            print(f"sorry! someone has borrowed it,{requestedBook} not in the library")

    def addbook(self,returnbook):
        self.availablebooks.append(returnbook)
        print(f"thanks! for returning your borrowed book.{returnbook}")

class Student:
    def requestBook(self):
        print("Enter the name of the book you would like to check out:")
        requestBook=input()
        return requestBook

    def returnBook(self):
        print("Enter the book you would like to return:")
        returnbook=input()
        return returnbook



def main():
    library=Library(["python",".Net","C++","C"],"KIST")
    student=Student()
    done=False
    while done==False:
        print("""=========LIBRARY MENU==========
                  1.DISPLAY ALL AVAILABLE BOOKS
                  2.REQUEST A BOOK
                  3.RETURN A BOOK
                  4.EXIT
                  """)
        choice=int(input("ENTER A CHOICE:"))
        if choice==1:
            library.displayAvailablebooks()
        elif choice==2:
            library.lendbook(student.requestBook())
            
        elif choice==3:
            library.addbook(student.returnBook())
        elif choice==4:
            exit()
main()



       


