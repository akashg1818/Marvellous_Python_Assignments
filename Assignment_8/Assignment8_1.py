import threading
import time

def DisplayEven(no):

    print("Inside DisplayEven")
    
    for i in range(1,no+1):
        print(i*2)

def DisplayOdd(no):

    print("Inside DisplayOdd")

    for i in range(no):
        print(i*2+1)

def main():

    print("Inside main")

    Strat_time = time.time()

    print("Enter how many numbers you want to display:")
    value = int(input())

    T1 = threading.Thread(target = DisplayEven, args = (value,))
    T2 = threading.Thread(target = DisplayOdd, args = (value,))

    T1.start()
    T2.start()

    T1.join()
    T2.join()

    End_time = time.time()

    print("Execution time is :",End_time - Strat_time)

    print("End of main")

if __name__ == "__main__":
    main()