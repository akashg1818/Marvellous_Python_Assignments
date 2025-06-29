import os

def DisplayFile(Filename):

    print("Inside DisplayFile function ")

    fobj = open(Filename, "w")

    print("Enter the name of 5 students:")
    for i in range(5):
        Data = input()
        fobj.write(Data)
        fobj.write("\n")
    
    fobj = open(Filename, "r")
    print("Entered name of students are :")
    print(fobj.read())

    fobj.close()


def main():
    print("Enter the file name that you want to create:")
    Fname = input()

    DisplayFile(Fname)

if __name__ == "__main__":
    main()