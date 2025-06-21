import os
import multiprocessing
import time

def CalculateFactorial(no):

    print("PID of process is :",os.getpid())
    fact = 1
    for i in range(no,0,-1):
        fact = fact * i   
    return fact
  

def main():

    print("Inside main ")

    start_time = time.time()

    print("Enter the number of values :")
    value = int(input())

    data = []

    print("Enter the values :")
    for i in range(value):
        no = int(input())
        data.append(no)
    print("data[] :",data)

    result = []

    p = multiprocessing.Pool()
    result = p.map(CalculateFactorial,data)

    p.close()
    p.join()

    print(result)

    end_time = time.time()

    print("Execution time is :", end_time - start_time)
        

if __name__ == "__main__":
    main()