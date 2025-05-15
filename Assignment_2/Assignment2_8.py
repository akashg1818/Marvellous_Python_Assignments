#\ 1
#\ 1 2 
#\ 1 2 3
#\ 1 2 3 4

def Display(no):
    if(no <= 0):
        print("Invalid input")
        return

    for i in range(1,no+1):
        for j in range(1,i+1):
            print(j,end="  ")
        print()

def main():
    value = int(input("Enter the number :"))

    Display(value)

if __name__ == "__main__":
    main()