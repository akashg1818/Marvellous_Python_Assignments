def CheckVowel(ch,data):

    for value in data:
        if(ch == value):
            return True

def main():
    char = input("Enter the character :")

    Data = ['a','e','i','o','u']

    Ans = CheckVowel(char,Data)
    if(Ans == True):
        print(char,"is vowel")
    else:
        print("It's a constant")

if __name__ == "__main__":
    main()