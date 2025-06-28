import os

def CheckFile(Filename):

    flag = os.path.exists(Filename)

    if(flag == False):
        print("File not exist in current directory")
    else:
        print("File exists in current directory")

def main():
    print("Enter the file name :")

    Fname = input()

    CheckFile(Fname)

if __name__ == "__main__":
    main()