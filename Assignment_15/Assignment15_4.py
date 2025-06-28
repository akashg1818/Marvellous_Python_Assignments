import os
import sys

def Display(File1,File2):

    print("Inside the Display function ")

    flag1 = os.path.exists(File1)
    flag2 = os.path.exists(File2)

    if((flag1 == False) or (flag2 == False)):
        print("There is no such file")
    else:
        print("Files are present in current directory")
    fobj = open(File1,"r")
    Data1 = fobj.read()

    Dobj = open(File2,"r")
    Data2 = Dobj.read()

    if(Data1 == Data2):
        print("Success")
    else:
        print("Failure")
    
    fobj.close()
    Dobj.close()


def main():
    Border = "-"*54
    print(Border)
    print("--------------- File Handling ----------------")
    print(Border)

    if(len(sys.argv) == 2):
        if((sys.argv[1] == "--h") or (sys.argv[1] == "--H")):
            print("This application is used to perform compare data of two files")
           
        elif((sys.argv[1] == "--u") or (sys.argv[1] == "--U")):
            print("Use the given script as ")
            print("ScriptName.py  Argument1 Argument2")

        else:
            print("Use the given flags as : ")
            print("--h : Used to display the help")
            print("--u : Used to display the usage")

    elif(len(sys.argv) == 3):
        Display(sys.argv[1],sys.argv[2])

    else:
        print("Invalid number of coomand line arguments")
        print("Use the given flags as : ")
        print("--h : Used to display the help")
        print("--u : Used to display the usage") 

    print(Border)
    print("--------------------- Thank you ---------------")

    print(Border)

if __name__ == "__main__":
    main()
