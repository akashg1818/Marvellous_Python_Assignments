import os
import sys
import time
import hashlib

def CalculateCheckSum(filename):

    fobj = open(filename,'rb')

    hobj = hashlib.md5()

    buffer = fobj.read(1024)
    while(len(buffer)> 0):
        hobj.update(buffer)
        buffer = fobj.read(1024)
    
    return hobj.hexdigest()

def DisplayResult(Data):
    Result = list(filter(lambda X: len(X) > 1, Data.values()))
    
    Count = 0
    cnt = 0
    Data = []
    for value in Result:
        for subvalue in value:
            Count += 1
            if(Count > 1):
                Data.append(subvalue)
                os.remove(subvalue)
                cnt += 1
        Count = 0

    print("Total deleted file :",cnt)

    return Data

def DirectoryDisplayExtension(Dirname):

    ret = os.path.isabs(Dirname)

    if(ret == False):
        Dirname = os.path.abspath(Dirname)
    
    ret = os.path.exists(Dirname)
    if(ret == False):
        print("There is no such path")
        return 

    ret = os.path.isdir(Dirname)
    if(ret == False):
        print(Dirname,": is path but not directory")
        return

    print("Path of Directory is :"+Dirname)

    
    Data = {}
    
    for Foldername, SubFoldernames, Filenames in os.walk(Dirname):
 
        for fname in Filenames:          
            fname = os.path.join(Foldername,fname)
            #if(fname.endswith(Extention)):  
            checksum = CalculateCheckSum(fname)
            if checksum in Data:
                Data[checksum].append(fname)
            else:
                Data[checksum] = [fname]

    
    Ret = DisplayResult(Data)   
    
    fobj = open("Log.txt","w")

    Border = "-"*54

    fobj.write(Border+"\n")
    fobj.write("This is log file of automation script \n")
    fobj.write("This script is used to clean the directory \n")
    fobj.write(Border+"\n")

    fobj.write("\n\n\n\n\n\n\n")
    fobj.write(str(Ret))

    fobj.write("\n\n\n\n\n\n\n")

    fobj.write(Border+"\n")
    fobj.write(Border+"\n")

    print("Success")

    
def main():

    Border = "-"*54
    print(Border)
    print("--------------- Python Automation ----------------")
    print(Border)


    if(len(sys.argv) == 2):
        if((sys.argv[1] == "--h" or sys.argv[1] == "--H" )):
            print("This script is used to clean the directory")

        elif((sys.argv[1] == "--U" or sys.argv[1] == "--u" )):
            print("Use this script as :")
            print("python filename.py Argument1")
        
        else:
            DirectoryDisplayExtension(sys.argv[1])
            
    else:
        print("Invalid number of command line arguments")
        print("Use the given flags as : ")
        print("--h : Used to display the help")
        print("--u : Used to display the usage") 

    print(Border)
    print("----------- Thank you for using our script -----------")
    print(Border)


if __name__ == "__main__":
    main()