import os

def DisplayFile(Filename):

    flag = os.path.exists(Filename)

    if(flag == False):
        print("There is no such file")
    else:
        print("File is present in current directory")

    fobj = open(Filename,"r")

    with fobj as file:
        lines = file.readlines()
        print("lines are :",lines)
        
        for line in lines:
            CountWord = 0
            words = line.split()
            CountWord += len(words)
            if(CountWord >= 5):
                print(line)

    fobj.close()


def main():
    print("Enter the file name that you want to read:")
    Fname = input()

    DisplayFile(Fname)

if __name__ == "__main__":
    main()