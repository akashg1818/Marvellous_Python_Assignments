import os

def Display(Filename):

    print("Inside the Display function ")

    flag = os.path.exists(Filename)

    if(flag == False):
        print("There is no such file")
    else:
        print("File is present in current directory")
        fobj = open(Filename,"r")
        Data = fobj.read()

        print("Data from file is :",Data)

        fobj.close


def main():

    print("Enter the file name that you want to read :")
    
    FName = input()

    Display(FName)

if __name__ == "__main__":
    main()
