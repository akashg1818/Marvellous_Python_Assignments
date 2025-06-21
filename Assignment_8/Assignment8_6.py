import threading
import time

def Digits(str2):

    print("Inside Digits")
    count = 0
    for char in str2:
        if char.isdigit():
            print(char)
            count += 1
    print("Number of digits are :",count)
    
def Small(str2):

    print("Inside Samll")
    count = 0
    for char in str2:
        if char.islower():
            print(char)
            count += 1
    print("Number of lowercase characters are :",count)
  
def Capital(str2):

    print("Inside capital")
    count = 0
    for char in str2:
        if char.isupper():
            print(char)
            count += 1
    print("Number of uppercase letters are :",count)



def main():

    print("Inside main")

    Start_time = time.time()

    print("Enter the string :")
    str1 = input()

    T1 = threading.Thread(target = Capital, args = (str1,))
    T2 = threading.Thread(target = Small, args = (str1,))
    T3 = threading.Thread(target = Digits, args = (str1,))

    T1.start()
    T2.start()
    T3.start()

    T1.join()
    T2.join()
    T3.join()   

    End_time = time.time()

    print("Execution time is :",End_time - Start_time)

    print("End of main")

if __name__ == "__main__":
    main()