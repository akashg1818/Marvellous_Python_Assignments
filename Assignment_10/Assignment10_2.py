Power = lambda X,Y: X*Y

def main():

    print("Enter first number :")
    value1 = int(input())

    print("ENter second number :")
    value2 = int(input())

    Ret = Power(value1,value2)
    print("Result is :",Ret)


if __name__ == "__main__":
    main()