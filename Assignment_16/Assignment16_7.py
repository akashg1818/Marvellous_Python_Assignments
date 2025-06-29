def Data(Filename):

    fobj = open(Filename, "w")

    fobj.write("Akash 88\n")
    fobj.write("Riya 72\n")
    fobj.write("Aman 95\n")
    fobj.write("Rahul 67\n")
    fobj.write("Ram 78\n")
    
    print("Student who scored more than 75 marks :")
    fobj = open(Filename, "r")
    with fobj:
        for line in fobj:
            parts = line.strip().split()
            name = parts[0]
            marks = int(parts[1])

            if(marks > 75):
                print(f"{name} - {marks}")

def main():
    print("Enter the name of file :")
    File = input()
   
    Data(File)

if __name__ == "__main__":
    main()