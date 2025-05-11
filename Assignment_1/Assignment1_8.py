def Display(no):
    for i in range(no):
        print("*")  #at new line
    
    print("---------------------")
    for i in range(no):
        print("*",end='\t' ) #tab seperated

    print()
    print("---------------------")
    
    for i in range(no):
        print("*",end=',' if i < no - 1 else '') #comma seperated

    

def main():
    value = int(input("Enter the number :"))

    Display(value)

if __name__ == "__main__":
    main()