def Addition(data):
    sum = 0

    for value in data:
        sum = sum + value
    return sum


def main():
    print("Enter the number of values :")
    values = int(input())

    Data = list()
    
    print("Enter the number of elements")
    for i in range(values):
        no = int(input())
        Data.append(no)
    
    print("List:",Data)

    Result = Addition(Data)
    print("Addition of elements are :",Result)

if __name__ == "__main__":
    main()
