def CheckPrime(no):
    if (no <=1):
        return False
        
    if (no == 2):
        return True

    for i in range(2,no):
        if(no % i == 0):
            return False

    return True

Multiply = lambda A : A * 2

def RetMaximun(data):
    ans = 0
    for value in data:
        if(value > ans):
            ans = value
    return ans


def filterX(Fun,value):
    List = []
    for i in value:
        if( Fun(i) == True ):
            List.append(i)
    return List

def mapX(Fun,value):
    List = []
    for i in value:
        List.append(Fun(i))

    return List

def reduceX(Fun,value):
    Result = Fun(value)

    return Result
        

def main():
    print("Enter the size of list :")
    size = int(input())
    
    Data = []
    print("Enter the number :")
    for i in range(size):
        no = int(input())
        Data.append(no)
    
    print("List:",Data)

    FData = list(filterX(CheckPrime,Data))
    print("Filtered list is :",FData)

    MData = list(mapX(Multiply,FData))
    print("Mapped list is :",MData)

    RData = reduceX(RetMaximun,MData)
    print("Output is :",RData)

if __name__ == "__main__":
    main()