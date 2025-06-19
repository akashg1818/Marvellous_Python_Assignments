def main():
    value = int(input("Enter your age :"))

    if(value >= 18):
        print("You are eligible to vote")
    elif(value < 0):
        print("Invalid input")
    else:
        print("You are not eligible to vote")


if __name__ == "__main__":
    main()