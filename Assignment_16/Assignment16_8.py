def SpaceRemove(Filename1,Filename2):

    fobj1 = open(Filename1, "r")

    with fobj1 as file:
        lines = file.readlines()

    non_blank_lines = [line for line in lines if line.strip() != ""]

    fobj2 = open(Filename2, "w")
    with fobj2 as file:
        file.writelines(non_blank_lines)


    

def main():

    print("Enter the file that you want to read :")
    Fname1 = input()
    print("Enter the file name that you want to write :")
    Fname2 = input()

    SpaceRemove(Fname1,Fname2)


if __name__ == "__main__":
    main()