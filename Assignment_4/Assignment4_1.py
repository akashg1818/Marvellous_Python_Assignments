Power = lambda A : A ** 2


def main():
    value = int(input("Enter the number :"))

    ret = Power(value)

    print("Power of two is :",ret)



if __name__ == "__main__":
    main()