class Arithematic:

    PI = 3.14

    def __init__(self):
        self.value1 = 0
        self.value2 = 0

    def Accept(self,A,B):
        self.value1 = A
        self.value2 = B

    def Addition(self):
        Ans = self.value1 + self.value2
        print("Addition is :",Ans)
    
    def Substraction(self):
        Ans = self.value1 - self.value2
        print("Substraction is :",Ans)

    def Multiplication(self):
        Ans = self.value1 * self.value2
        print("Multiplication is :",Ans)

    def Division(self):
        Ans = self.value1 / self.value2
        print("Division is :",Ans)


def main():

    obj1 = Arithematic()
    obj2 = Arithematic()

    obj1.Accept(12,10)
    obj1.Addition()
    obj1.Substraction()
    obj1.Multiplication()
    obj1.Division()

    obj2.Accept(27,10)
    obj2.Addition()
    obj2.Substraction()
    obj2.Multiplication()
    obj2.Division()

if __name__ == "__main__":
    main()