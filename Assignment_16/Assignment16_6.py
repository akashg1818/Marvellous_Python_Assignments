def Data(Filename1,Filename2):

    fobj1 = open(Filename1, "r")
    Data = fobj1.read()
    
    fobj2 = open(Filename2, "w")
    fobj2.write(Data)



def main():
    print("Enter the name of file from which you wants to copy the data :")
    File1 = input()
    print("Enter the name of file in which you wants to paste the copied the data :")
    File2 = input()

    Data(File1,File2)

if __name__ == "__main__":
    main()