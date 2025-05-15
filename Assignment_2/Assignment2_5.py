def CheckPrime(no):
    if (no <= 1):
        print("It is not prime number")
        return

    if(no == 2):
        print("It is prime number")
        return

    for i in range(2,no):
        if(no % i == 0):
            print("It is not prime number")
            return
    
    print("It is prime number")

def main():
    print("Enter the number :")
    value = int(input())

    CheckPrime(value)

if __name__ == "__main__":
    main()