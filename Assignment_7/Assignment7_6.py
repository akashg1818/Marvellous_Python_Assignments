
def FilterX(value):
    List = []
    for i in value:
        if (i <= 1):
            return False

        if (i == 2):
            List.append(i)
            return True

        for j in range(2,i):
            if( i %  j == 0):
                return False

        return True
        

    return List



def main():
    size = int(input("Enter the number of inputs :" ))

    Data = []

    print("Enter the data :")
    for i in range(size):
        no = int(input())
        Data.append(no)

    print("List :",Data)

    FData = list(FilterX(Data))
    print("Filtered data  is :",FData)

if __name__ == "__main__":
    main()