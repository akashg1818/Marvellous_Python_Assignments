import os
import sys

def DisplayFile(Filename):

    ret = os.path.exists(Filename)

    if(ret == True):
        print(Filename," is present in current directory")
    else:
        print("File is not present in current directory")

    fobj = open(Filename,"r")
    Data = fobj.read()

    File = sys.argv[1]

    fobjX = open(File,"w")
    fobjX.write(str(Data))

    print("Data gets copied into ",File)
    

    fobj.close()
    fobjX.close()


def main():
    print("Enter the file name :")
    Fname = input()

    DisplayFile(Fname)

if __name__ == "__main__":
    main()