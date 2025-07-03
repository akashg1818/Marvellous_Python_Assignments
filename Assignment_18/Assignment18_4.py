import os
import sys
import hashlib

def CompareFile(Filename1,Filename2):

    ret1 = os.path.exists(Filename1)
    if(ret1 == False):
        print(Filename1,"File is not present in current directory")
    
    ret2 = os.path.exists(Filename2)
    if(ret2 == False):
        print(Filename2,"File is not present in current directory")
    
    obj1 = open(Filename1,"r")
    Data1 = obj1.read()

    obj2 = open(Filename2,"r")
    Data2 = obj2.read()

    if(Data1 == Data2):
        print("Success")
    else:
        print("Failure")   

    obj1.close()
    obj2.close()

def CompareFileX(Filename1,Filename2):

    fobj1 = open(Filename1,"rb")
    fobj2 = open(Filename2,"rb")

    hobj1 = hashlib.md5()

    buffer = fobj1.read(1024)
    while(len(buffer)> 0):
        hobj1.update(buffer)
        buffer = fobj1.read(1024)

    hobj2 = hashlib.md5()

    buffer = fobj2.read(1024)
    while(len(buffer)> 0):
        hobj2.update(buffer)
        buffer = fobj2.read(1024)

    if(hobj1.hexdigest() == hobj2.hexdigest()):
        print("Success")
    else:
        print("Failure")


def main():

    CompareFile(sys.argv[1],sys.argv[2])
    CompareFileX(sys.argv[1],sys.argv[2])

if __name__ == "__main__":
    main()