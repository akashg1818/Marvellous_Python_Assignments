import os
import sys
import time

def DirectoryDisplayExtension(Dirname,Extention):

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


    Data = []
    TotalCount = 0
    ActualCount = 0
    for Foldername, SubFoldernames, Filenames in os.walk(Dirname):
 
        for fname in Filenames:
            TotalCount += 1  
            #fname = os.path.join(Foldername,fname)
            if(fname.endswith(Extention)):  
                ActualCount +=1
                Data.append(fname)

    timestamp = time.ctime()

    Filename = "Automation%s.Log"%(timestamp)
    Filename = Filename.replace(" ","_")
    Filename = Filename.replace(":","_")

    fobj = open(Filename,"w")

    Border = "-"*54

    fobj.write(Border+"\n")
    fobj.write("This is log file of automation script \n")
    fobj.write("This script is used to display the files with given Extension from directory \n")
    fobj.write(Border+"\n")

    fobj.write("\n\n\n\n\n\n\n")
    fobj.write("Total files in the directory are :")
    fobj.write(str(TotalCount))
    fobj.write("\n")
    fobj.write("File with given extension are :")
    fobj.write(str(ActualCount))
    fobj.write("\n")
    fobj.write("File with that extension are :")
    fobj.write(str(Data))

    fobj.write("\n\n\n\n\n\n\n")

    fobj.write(Border+"\n")
    fobj.write("This is is created at \n"+timestamp+"\n")
    fobj.write(Border+"\n")

    print("Success")
    print("Please check file "+Filename+" in current directory")

    
def main():

    Border = "-"*54
    print(Border)
    print("--------------- Python Automation ----------------")
    print(Border)


    if(len(sys.argv) == 2):
        if((sys.argv[1] == "--h" or sys.argv[1] == "--H" )):
            print("This script is used to display file with given extension from provided directory")

        elif((sys.argv[1] == "--U" or sys.argv[1] == "--u" )):
            print("Use this script as :")
            print("python filename.py Argument1 Argument2")
        
        else:
            print("Use the given flags as : ")
            print("--h : Used to display the help")
            print("--u : Used to display the usage")

    elif(len(sys.argv) == 3):

        DirectoryDisplayExtension(sys.argv[1],sys.argv[2])

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