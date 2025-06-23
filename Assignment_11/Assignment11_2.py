fact = 1

def Factorial(no):
    global fact
    if(no == 0):
        return 0
        
    if(no >= 1):
        fact = fact * no
        no = no - 1
        Factorial(no)
    return fact

def main():

    print("Enter the number")
    value = int(input())

    Ret = Factorial(value)
    print("Factorial is :",Ret)

if __name__ == "__main__":
    main()