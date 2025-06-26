class Rectangle:

    def __init__(self,A,B):
        self.length = A
        self.width = B

    def DisplayArea(self):
        Ans = 0
        Ans =  self.length * self.width
        print("Area of rectangle is :",Ans)

    def DisplayPerimeter(self):
        Ans = 0
        Ans = 2 *(self.length + self.width)
        print("Perimeter of rectangle is :",Ans)

def main():
    obj1 = Rectangle(10,11)
    obj1.DisplayArea()
    obj1.DisplayPerimeter()

if __name__ == "__main__":
    main()
