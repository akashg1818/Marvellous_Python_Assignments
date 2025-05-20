CheckEven = lambda A : A % 2 == 0
Square = lambda A : A ** 2
Sum = lambda A,B : A + B

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
    Result = 0
    for i in value:
        Result = Fun(Result,i)
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

    FData = list(filterX(CheckEven,Data))
    print("Filtered list is :",FData)

    MData = list(mapX(Square,FData))
    print("Mapped list is :",MData)

    RData = reduceX(Sum,MData)
    print("Reduced data is :",RData)

if __name__ == "__main__":
    main()