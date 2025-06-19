def CheckPrime(no):
    if(no <= 1 ):
        return False

    if(no == 2):
        return True
    
    for i in range(2,no):
        if(no % i == 0):
            return False

    return True

    

def main():
    value = int(input("Enter the number :"))

    Ans = CheckPrime(value)
    if(Ans == True):
        print(value,"is prime  number")
    else:
        print(value,"is not prime number")
if __name__ == "__main__":
    main()