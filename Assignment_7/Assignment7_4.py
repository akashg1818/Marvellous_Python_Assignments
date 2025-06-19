from functools import reduce 

Product = lambda A,B : A * B

def main():
    size = int(input("Enter the number of inputs :" ))

    Data = []

    print("Enter the data :")
    for i in range(size):
        no = int(input())
        Data.append(no)

    print("List :",Data)

    rData = reduce(Product,Data)
    print("Output is :",rData)

if __name__ == "__main__":
    main()