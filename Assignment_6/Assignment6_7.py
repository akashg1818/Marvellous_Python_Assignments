def DisplayMax(data):
    Ans = 0 
    for value in data:
        if(value >> Ans):
            Ans = value
    return Ans

def main():
    Data = []
    print("Enter 5 numbers :")
    for i in range(5):
        no  = int(input())
        Data.append(no)

    print("Entered numbers are :",Data)

    Result = DisplayMax(Data)
    print("Maximum number is :",Result)


if __name__ == "__main__":
    main()