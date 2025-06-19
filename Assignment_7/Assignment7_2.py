Double = lambda A : A * 2

def mapX(Task,value):
    List = []
    for i in value:
        List.append(Task(i))
    return List



def main():
    size = int(input("Enter the number of inputs :" ))

    Data = []

    print("Enter the data :")
    for i in range(size):
        no = int(input())
        Data.append(no)

    print("List :",Data)

    MData = list(mapX(Double,Data))
    print("Mapped output is :",MData)

if __name__ == "__main__":
    main()