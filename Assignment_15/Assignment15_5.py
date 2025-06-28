import os
import sys

def Search(Filename,STR):

    print("Inside the Display function ")

    flag = os.path.exists(Filename)

    if(flag == False):
        print("There is no such file")
    else:
        print("File is present in current directory")
    
    Count = 0
    fobj = open(Filename,"r")
    with fobj as file:
        for line in file:
            if STR in line:
                Count += 1
    print("Frequency of stirng "+STR+" in file is :",Count)
    
    fobj.close()

def main():
    print("Enter the file name that you want to read :")
    Fname = input()

    print("Enter the string that you want to search in the file :")
    Str = input()

    Search(Fname,Str)
    

if __name__ == "__main__":
    main()
