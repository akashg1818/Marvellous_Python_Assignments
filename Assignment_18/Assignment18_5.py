import os
import sys

def CountStr(Filename,STRING):

    ret = os.path.exists(Filename)

    if(ret == False):
        print(Filename," is not present in current directory")
    

    count = 0
    fobj = open(Filename,"r")
    with fobj:
        lines = fobj.readlines()
        print(len(lines))
        word = lines.split()
        
        if(word == STRING):
            count += 1
    print(count)

    fobj.close()


def main():
    print("Enter the file name :")
    Fname = input()
    print("Enter the string that you want to search in the file :")
    STRING = input()

    CountStr(Fname,STRING)

if __name__ == "__main__":
    main()