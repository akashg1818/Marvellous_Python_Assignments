#   *  *  *  * 
#   *  *  *
#   *  *
#   *

def Display(no):
    if(no <= 0):
        print("Invalid input")
        return
    #for i in range(no,0,-1):
    #       print("*\t" * i)
    #       print()

    for i in range(no,0,-1):
        for j in range(i):
            print("*\t", end = "")
        print()

        

def main():
    value = int(input("Enter the number :"))

    Display(value)

if __name__ == "__main__":
    main()