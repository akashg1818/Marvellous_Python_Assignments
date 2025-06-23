sum = 0

def SumDigit(no):
    global sum
    if(no > 0):
        ans = no % 10
        sum = sum + ans
        no = no // 10
        SumDigit(no)
    return sum

    

def main():

    print("Enter the first number :")
    value = int(input())

    Ret = SumDigit(value)
    print("Sum of digit is :",Ret)

if __name__ == "__main__":
    main()