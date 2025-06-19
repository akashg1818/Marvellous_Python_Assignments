def Display(no):
    print("Multiplication table of :",no)
    Ans = 0
    for i in range(1,11):
        Ans = no *  i
        print(f"{no} * {i} = {Ans}")

def main():
    value =int(input("Enter the number :"))

    Display(value)

if __name__ == "__main__":
    main()