def main():
    no1,no2,no3= map(int,input("Enter three values :").split())

    print("Entered values are :",no1,no2,no3)

    if(no1 >= no2 and no1 >= no3):
        print("Largest number is :",no1)
    elif(no2 >= no1 and no2 >= no3):
        print("Largest number is :",no2)
    else:
        print("Largest number is :",no3)
   

if __name__ == "__main__":
    main()