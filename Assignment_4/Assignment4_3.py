# CheckValue = lambda A : 70 <= A <= 90
# Increase = lambda A : A + 10
# reduce = lambda A,B : A * B
from functools import reduce


def main():
    print("Enter the size of list :")
    size = int(input())
    
    Data = []
    print("Enter the number :")
    for i in range(size):
        no = int(input())
        Data.append(no)
    
    print("List:",Data)

    FData = list(filter(lambda A : 70 <= A <= 90,Data))
    print("Filtered list is :",FData)

    MData = list(map(lambda A : A + 10,FData))
    print("Mapped list is :",MData)

    RData = reduce(lambda A,B : A * B,MData)
    print("Reduced data is :",RData)

if __name__ == "__main__":
    main()