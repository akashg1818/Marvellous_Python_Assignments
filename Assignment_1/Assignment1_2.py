def ChkNum(no):
    if(no % 2 == 0):
        print("Even Number")
    else:
        print("Odd number")

def main():
    print("Enter the number :")
    value = int(input())

    ChkNum(value)


if __name__ =="__main__":
    main()