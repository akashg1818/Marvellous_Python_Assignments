import os
import sys

def Display(Filename):

    print("Inside the Display function ")

    flag = os.path.exists(Filename)

    if(flag == False):
        print("There is no such file")
    else:
        print("File is present in current directory")
    fobj = open(Filename,"r")
    Data = fobj.read()

    Dobj = open("Demo.txt","w")
    Dobj.write(Data)

    Dobj.close()


def main():
    Border = "-"*54
    print(Border)
    print("--------------- File Handling ----------------")
    print(Border)

    if(len(sys.argv) == 2):
        if((sys.argv[1] == "--h") or (sys.argv[1] == "--H")):
            print("This application is used to perform file handling")
           
        elif((sys.argv[1] == "--u") or (sys.argv[1] == "--U")):
            print("Use the given script as ")
            print("ScriptName.py  Argument1 ")

        else:
            Display(sys.argv[1])
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
