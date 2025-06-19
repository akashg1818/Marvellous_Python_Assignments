def DisplayFactors(no):
    Ans = 1
    for i in range(1,no+1):
        Ans = Ans * i
    return Ans

def main():
    value = int(input("Enter the number :"))

    Result = DisplayFactors(value)
    print("Factorial is :",Result)

if __name__ == "__main__":
    main()