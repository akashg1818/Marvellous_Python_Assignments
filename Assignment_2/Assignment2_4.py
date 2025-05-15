def Factorail(no):
    Ans = 1
    for i in range(1,no+1):
        Ans = Ans * i
    return Ans

def main():
    print("Enter the number :")
    value = int(input())

    Result = Factorail(value)
    print("Factorail of number is :",Result)

if __name__ == "__main__":
    main()