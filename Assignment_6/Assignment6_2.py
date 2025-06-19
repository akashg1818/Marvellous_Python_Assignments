def SumEven(no):
    sum = 0
    for i in range(2,no+1,2):
        sum = sum + i
    return sum

def main():

    Ans = SumEven(100)
    print("Sum is :",Ans)

if __name__ == "__main__":
    main()