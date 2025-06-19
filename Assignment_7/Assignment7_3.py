Even = lambda A : A % 2 ==  0

def FilterX(Task,value):
    List = []
    for i in value:
        if (Task(i) == True):
            List.append(i)
    return List



def main():
    size = int(input("Enter the number of inputs :" ))

    Data = []

    print("Enter the data :")
    for i in range(size):
        no = int(input())
        Data.append(no)

    print("List :",Data)

    FData = list(FilterX(Even,Data))
    print("Filtered data  is :",FData)

if __name__ == "__main__":
    main()