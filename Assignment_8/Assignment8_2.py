import threading
import time

def EvenFactor(no):

    print("Inside DisplayEven")
    sum = 0
    for i in range(1,no+1):
        if(no % i == 0):
            if(i % 2 == 0):
                sum = sum + i
    print("sum of even factors is :",sum)
        

def OddFactor(no):

    print("Inside DisplayOdd")

    sum = 0
    for i in range(1,no+1):
        if(no % i == 0):
            
            if(i % 2 != 0):
                sum = sum + i
    print("sum of odd factors is :",sum)

def main():

    print("Inside main")

    Start_time = time.time()

    print("Enter the number :")
    value = int(input())

    T1 = threading.Thread(target= EvenFactor, args = (value,))
    T2 = threading.Thread(target = OddFactor, args =(value,))

    T1.start()
    T2.start()

    T1.join()
    T2.join()

    End_time = time.time()

    print("Execution time is :",End_time - Start_time)

    print("End of main")

if __name__ == "__main__":
    main()