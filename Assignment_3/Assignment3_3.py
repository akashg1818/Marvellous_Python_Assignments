def RetMinimum(data):
    ans = 0
    for value in data:
        ans = value
        break
    
    for value in data:
        if(value < ans):
            ans = value
    return ans


def main():
    print("Enter the number of values :")
    size = int(input())

    Data = list()

    print("Enter the elements :")
    for i in range(size):
        no = int(input())
        Data.append(no)

    print("List:",Data)

    Result = RetMinimum(Data)
    print("Minimum element is:",Result)
        


if __name__ == "__main__":
    main()