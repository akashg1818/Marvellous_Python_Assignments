def RetFrequency(data,No):
    count = 0

    for value in data:
        if(value == No):
            count += 1
    return count


def main():
    print("Enter the number of values :")
    size = int(input())

    Data = list()

    print("Enter the elements :")
    for i in range(size):
        no = int(input())
        Data.append(no)
    
    value = int(input("Enter the element : "))
    print("List:",Data)

    Result = RetFrequency(Data,value)
    print("Frequency of the element is:",Result)
        


if __name__ == "__main__":
    main()