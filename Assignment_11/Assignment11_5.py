sum = 0

def SumDigit(no):
    global sum
    if(no > 0):
        ans = no % 10
        if(ans == 0):
            sum = sum + 1
        no = no // 10
        SumDigit(no)
    return sum

    

def main():

    print("Enter the first number :")
    value = int(input())

    Ret = SumDigit(value)
    print("Total 0 in number :",Ret)

if __name__ == "__main__":
    main()