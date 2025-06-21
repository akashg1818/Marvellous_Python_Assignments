import multiprocessing
import threading
import time

def DisplaySum():
    
    sum = 0
    for i in range(1,10000001):
        sum = sum + i
    print("Addition is :",sum)

def main():

    print("Inside main ")

    start_time1 = time.time()

    DisplaySum()

    end_time1 = time.time()

    print("Execution time using normal function is :",end_time1 - start_time1)
    
    Border = 80 * "-"
    print(Border)

    start_time2 = time.time()

    T1 = threading.Thread(target = DisplaySum)
    T1.start()
    T1.join()

    end_time2 = time.time()

    print("Execution time using threading is :",end_time2 - start_time2)

    print(Border)

    start_time3 = time.time()

    T1 = multiprocessing.Process(target = DisplaySum)
    T1.start()
    T1.join()

    end_time3 = time.time()

    print("Execution time using threading is :",end_time3 - start_time3)
    

if __name__ == "__main__":
    main()