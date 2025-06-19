def Addition(no1,no2):
    ans = 0
    ans = no1 + no2
    return ans

def Difference(no1,no2):
    ans = 0
    ans = no1 - no2
    return ans

def Multiplication(no1,no2):
    ans = 0
    ans = no1 * no2
    return ans

def Division(no1,no2):
    ans = 0
    ans = no1 / no2
    return ans




def main():
    value1 = int(input("Enter first number :"))
    value2 = int(input("Enter Second number :"))

    Ret = Addition(value1,value2)
    print("Addition is :",Ret)

    Ret = Difference(value1,value2)
    print("Differencce is :",Ret)

    Ret = Multiplication(value1,value2)
    print("Product is :",Ret)

    Ret = Division(value1,value2)
    print("Division is :",Ret)

if __name__ == "__main__":
    main()