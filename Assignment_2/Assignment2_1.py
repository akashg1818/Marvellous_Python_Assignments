import Arithmetic

def main():
    value1 = int(input("Enter first number :"))
    value2 = int(input("Enter second number :"))

    Result = Arithmetic.Add(value1,value2)
    print("Additon is :",Result)

    Result = Arithmetic.Sub(value1,value2)
    print("Subtraction is :",Result)

    Result = Arithmetic.Mult(value1,value2)
    print("Multiplication is :",Result)

    Result = Arithmetic.Div(value1,value2)
    print("Divisoin is :",Result)



    

if __name__ =="__main__":
    main()