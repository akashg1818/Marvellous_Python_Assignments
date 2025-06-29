import os

def DisplayFile(Filename):

    flag = os.path.exists(Filename)

    if(flag == False):
        print("There is no such file")
    else:
        print("File is present in current directory")
        fobj = open(Filename,"r")
        Data = fobj.read()

        print("Data from file is :",Data)

        fobj.close()


def main():
    print("Enter the file name that you want to read:")
    Fname = input()

    DisplayFile(Fname)

if __name__ == "__main__":
    main()