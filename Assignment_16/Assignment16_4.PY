def DisplayNumber(Filename):
    
    fobj = open(Filename,"w")
    print("How many numbers you want to write in file :")
    no = int(input())

    for i in range(no):
        Data = int(input())
        fobj.write(str(Data))
        fobj.write("\n")

    fobj = open(Filename,"r")
    print(fobj.read())

def main():
    print("Enter the file name that you want to create :")
    Fname = input()

    DisplayNumber(Fname)

if __name__ == "__main__":
    main()

