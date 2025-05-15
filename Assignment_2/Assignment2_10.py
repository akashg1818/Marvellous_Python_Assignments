def SumDigit(no):
    sum = 0

    if (no == 0):
        return sum

    else:
        no = abs(no)
        while (no > 0):
            digit = no % 10
            sum += digit
            no = no // 10
        return sum


def main():
    value = int(input("Enter the number :"))

    Result = SumDigit(value)
    print("Addition of digits in number are :",Result)

if __name__ == "__main__":
    main()