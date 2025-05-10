def Division(no):
    if(no % 5 == 0):
        print("True")
    else:
        print("False")


def main():
    value = int(input("Enter the number :"))

    Division(value)

if __name__ == "__main__":
    main()