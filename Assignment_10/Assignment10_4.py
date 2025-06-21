from functools import reduce

CheckEven = lambda i : (i % 2 == 0)

Square = lambda i : i * i

Sum = lambda A,B : A + B


def main():

    print("How many values you want to enter in the list :")
    value = int(input())

    Data = []
    print("Enter the values :")
    for i in range(value):
        no = int(input())
        Data.append(no)
    print(Data)
    

    fData = list(filter(CheckEven,Data))
    print("Filtered Data is :",fData)

    mData = list(map(Square,fData))
    print("mapped data is :",mData)

    result = reduce(Sum,mData)
    print("Output is :",result)

if __name__ == "__main__":
    main()