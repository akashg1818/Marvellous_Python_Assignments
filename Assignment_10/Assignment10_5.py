from functools import reduce

def CheckPrime(no):

    Check = True
    data = []

    if( no == 0 or no == 1):
        Check = False
        
    if(no == 2):
        return Check

    for i in range(2,no):
        if(no % i == 0):
            Check = False
            break

    return Check

    if(Check == True):
        data.append(no)

    return data

Multiply = lambda X : X*2

def CheckMax(no1,no2):

    max = no1
    if(no2 > no1):
        max = no2

    return max



def main():
    print("How many values you want to enter in the list :")
    value = int(input())

    Data = []
    print("Enter the values :")
    for i in range(value):
        no = int(input())
        Data.append(no)
    print(Data)
    

    fData = list(filter(CheckPrime,Data))
    print("Filtered Data is :",fData)

    mData = list(map(Multiply,fData))
    print("mapped data is :",mData)

    result = reduce(CheckMax,mData)
    print("Output is :",result)

if __name__ == "__main__":
    main()