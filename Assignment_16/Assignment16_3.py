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
        print(lines)
        CountLine = len(lines)
        CountWord = 0
        CountChar = 0

        for line in lines:
            words = line.split()
            CountWord += len(words)
            CountChar += len(line)

    print(f"Lines: {CountLine}")
    print(f"Words: {CountWord}")
    print(f"Characters: {CountChar}")

    fobj.close()


def main():
    print("Enter the file name that you want to read:")
    Fname = input()

    DisplayFile(Fname)

if __name__ == "__main__":
    main()