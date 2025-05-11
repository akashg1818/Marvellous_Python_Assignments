def CheckIntiger(no):
    if(no > 0):
        print("Positive number")
    elif(no < 0):
        print("Negative Number")
    else:
        print("Zero")


def main():
    value = int(input("Enter the number :"))

    CheckIntiger(value)

if __name__ == "__main__":
    main()