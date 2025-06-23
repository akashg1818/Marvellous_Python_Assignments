def Power(X,n):
    
    if(n == 0):
        return 1       
    return X * Power(X,n-1)


def main():

    print("Enter the first number :")
    value1 = int(input())

    print("Enter the first number :")
    value2 = int(input())


    Ret = Power(value1,value2)
    print("Power is :",Ret)

if __name__ == "__main__":
    main()