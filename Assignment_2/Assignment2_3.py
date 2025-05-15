def AddFactors(no):
    Ans = 0
    for i in range(1,no+1):
        if(no % i == 0):
           Ans = Ans + i
    return Ans

def main():
    print("Enter the number :")
    value = int(input())

    Result = AddFactors(value)
    print("ADdition of factors is :",Result)

if __name__ == "__main__":
    main()