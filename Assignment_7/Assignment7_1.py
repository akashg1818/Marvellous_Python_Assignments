Square = lambda A : A ** 2
Cube = lambda A : A ** 3


def main():
    value = int(input("Enter the number :"))

    Ans = Square(value)
    ans = Cube(value)
    print("Square :",Ans)
    print("Cube :",ans)

if __name__ == "__main__":
    main()