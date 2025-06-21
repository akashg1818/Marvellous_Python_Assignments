from functools import reduce

Compare = lambda i : ((i >= 70) & (i <= 90))

Increase = lambda i : i + 10

Product = lambda A,B : A * B


def main():

    print("How many values you want to enter in the list :")
    value = int(input())

    Data = []
    print("Enter the values :")
    for i in range(value):
        no = int(input())
        Data.append(no)
    print(Data)
    

    fData = list(filter(Compare,Data))
    print("Filtered Data is :",fData)

    mData = list(map(Increase,fData))
    print("mapped data is :",mData)

    result = reduce(Product,mData)
    print("Output is :",result)

if __name__ == "__main__":
    main()