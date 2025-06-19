def CheckEven(no):
    if(no % 2 == 0):
        print(no,"is even number")
    else:
        print(no,"is odd number")

def main(): 
    print("Enter the number :")
    value = int(input())

    CheckEven(value)

if __name__ == "__main__":
    main()