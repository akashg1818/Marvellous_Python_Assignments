sum = 0

def Factorial(no):
    global sum
    if(no >= 1):
        sum = sum + no
        no = no - 1
        Factorial(no)
    return sum

def main():

    print("Enter the number")
    value = int(input())

    Ret = Factorial(value)
    print("sum is :",Ret)

if __name__ == "__main__":
    main()