def Display(no):
    if(no <= 0):
        print("Invalid input")
        return

    for i in range(no):
        for j in range(1,no+1):
            print(j ,end="\t")
        print()        

def main():
    value = int(input("Enter the number :"))

    Display(value)

if __name__ == "__main__":
    main()