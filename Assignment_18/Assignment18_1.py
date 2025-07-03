import os

def FileExist(Filename):

    ret = os.path.exists(Filename)

    if(ret == True):
        print("File is present in current directory")
    else:
        print("File is not present in current directory")


def main():
    print("Enter the file name :")
    Fname = input()

    FileExist(Fname)

if __name__ == "__main__":
    main()