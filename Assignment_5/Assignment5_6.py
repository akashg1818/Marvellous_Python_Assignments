def Fahrenheit(no):
    Ans = 0
    Ans = (no * 9/5) + 32
    return Ans

def main():
    value = int(input("Enter temprature in celsius :"))

    Result = Fahrenheit(value)
    print("Temprature in fahrenheit is :",Result,"\u00B0F")

if __name__ == "__main__":
    main()