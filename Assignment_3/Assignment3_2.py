def RetMaximun(data):
    ans = 0
    for value in data:
        if(value > ans):
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

    Result = RetMaximun(Data)
    print("Maximum element is:",Result)
        


if __name__ == "__main__":
    main()