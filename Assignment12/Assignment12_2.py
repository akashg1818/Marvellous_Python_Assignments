class Circle:

    PI = 3.14

    def __init__(self):
        self.Radius = 0.0
        self.Area = 0.0
        self.Circumferance = 0.0

    def Accept(self,A):
        self.Radius = A

    def CalculateArea(self):
        self.Area = Circle.PI * self.Radius*self.Radius
    
    def CalculateCircumferance(self):
        self.Circumferance = 2 * Circle.PI * self.Radius

    def Display(self):
        print("Radius is :",self.Radius)
        print("Area is :",self.Area)
        print("Circumferance is :",self.Circumferance)

def main():

    obj1 = Circle()
    obj2 = Circle()

    obj1.Accept(12)
    obj1.CalculateArea()
    obj1.CalculateCircumferance()
    obj1.Display()

    obj2.Accept(10)
    obj2.CalculateArea()
    obj2.CalculateCircumferance()
    obj2.Display()


if __name__ == "__main__":
    main()