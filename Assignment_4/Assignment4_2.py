Multiplication = lambda A,B : A * B


def main():
    value1 = int(input("Enter the number :"))
    value2 = int(input("Enter the number :"))

    ret = Multiplication(value1,value2)

    print("Multiplication is :",ret)

if __name__ == "__main__":
    main()