def Display(no):
    for i in range(no):
        for j in range(no):
            print("*\t", end="")
        print()

#def Display1(no):
#   for i in range(no):
#        print("*\t" * no)
    



def main():

    value = int(input("Enter the number : "))

    Display(value)
    # Display1(value)

if __name__ == "__main__":
    main()