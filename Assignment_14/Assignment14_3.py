class Book:

    def __init__(self,A,B,C):
        self.Name = A
        self.Author = B
        self.__Price = C 
    
    def Display(self):
        print("Name of the book is :"+self.Name)
        print("Author of the book is :"+self.Author)
        print("Price of the book is :",self.__Price)

def main():

    obj1 = Book("C Programming ","Ajay Mittal",200)

    obj1.Display()


if __name__ == "__main__":
    main()

