class Calculator:

    def __init__(self,A,B):
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
    value1 = int(input("Enter first number :"))
    value2 = int(input("Enter second number :"))

    obj1 = Calculator(value1,value2)
    
    obj1.Addition()
    obj1.Substraction()
    obj1.Multiplication()
    obj1.Division()

if __name__ == "__main__":
    main()