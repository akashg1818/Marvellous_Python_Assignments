import os

def DisplayFile(Filename):

    ret = os.path.exists(Filename)

    if(ret == True):
        print("File is present in current directory")
    else:
        print("File is not present in current directory")

    fobj = open(Filename,"r")
    Data = fobj.read()

    print("Data inside file :\n",Data)
    

    fobj.close()


def main():
    print("Enter the file name :")
    Fname = input()

    DisplayFile(Fname)

if __name__ == "__main__":
    main()