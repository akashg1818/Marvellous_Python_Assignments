def CountDigit(no):
    count = 0

    if (no == 0):
        count = 1
        return count
    else:
        no = abs(no)
        while (no > 0):
            no = no // 10
            count = count + 1
        return count


def main():
    value = int(input("Enter the number :"))

    Result = CountDigit(value)
    print("Total digits in the number are :",Result)

if __name__ == "__main__":
    main()