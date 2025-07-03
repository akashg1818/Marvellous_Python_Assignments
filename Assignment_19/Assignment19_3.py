import os
import sys
import time
from pathlib import Path
import shutil


def CreateDirectory(Dirname):

    ret = os.path.isdir(Dirname)
    if(ret == False):
        os.mkdir(Dirname)
        print("Directory Created")
    else:
        print("Directory already exist")

def DirectoryCopy(Dir1,Dir2):

    for fname in os.listdir(Dir1):

        s = os.path.join(Dir1, fname)
        d = os.path.join(Dir2, fname)

        if os.path.isdir(s):
            shutil.copytree(s, d, dirs_exist_ok=True)
        else:
            shutil.copy2(s, d)
    return Dir2



def DirectoryTravel(Dirname1,Dirname2):

    ret = os.path.isabs(Dirname1)

    if(ret == False):
        Dirname1 = os.path.abspath(Dirname1)
    
    ret = os.path.exists(Dirname1)
    if(ret == False):
        print("There is no such path")
        return 

    ret = os.path.isdir(Dirname1)
    if(ret == False):
        print(Dirname1,": is path but not directory")
        return

    print("Path of Directory is :"+Dirname1)
   
    for Foldername, SubFoldernames, Filenames in os.walk(Dirname1):

        print("Folder name :"+Foldername)

        for subf in SubFoldernames:
            print("Sub folder name is :",subf)

        for fname in Filenames:
            print("Filenmae is :",fname)

    CreateDirectory(Dirname1)

    Ret = DirectoryCopy(Dirname1,Dirname2)

    print("Path of second Directory is :"+Ret)
   
    for Foldername, SubFoldernames, Filenames in os.walk(Ret):

        print("Folder name :"+Foldername)

        for subf in SubFoldernames:
            print("Sub folder name is :",subf)

        for fname in Filenames:
            print("Filenmae is :",fname)



    
def main():

    Border = "-"*54
    print(Border)
    print("--------------- Python Automtion ----------------")
    print(Border)


    if(len(sys.argv) == 2):
        if((sys.argv[1] == "--h" or sys.argv[1] == "--H" )):
            print("This is automation script")
            print("This script is used to change the extension of file")

        elif((sys.argv[1] == "--U" or sys.argv[1] == "--u" )):
            print("Use this script as :")
            print("python filename.py Argument1 Argument2")
        
        else:
            print("Use the given flags as : ")
            print("--h : Used to display the help")
            print("--u : Used to display the usage")

    elif(len(sys.argv) == 3):

        DirectoryTravel(sys.argv[1],sys.argv[2])


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