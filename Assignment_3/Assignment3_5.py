import MarvellousNum

def main():
    print("Enter the number of values :")
    size = int(input())

    Data = list()

    print("Enter the elements :")
    for i in range(size):
        no = int(input())
        Data.append(no)
    
    sum = 0
    for i in Data:
        if MarvellousNum.CheckPrime(i):
            sum = sum + i
    
    
    print("List:",Data)
    print("Sum prime numbers is:",sum)
        

if __name__ == "__main__":
    main()
























