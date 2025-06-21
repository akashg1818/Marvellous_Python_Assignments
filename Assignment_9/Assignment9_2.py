import os
import multiprocessing
import time

def Square(no):

    print("PID of process is :",os.getpid())
    Ans = no * no
    print(Ans) 

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
    
    for i in data:
        P = multiprocessing.Process(target = Square, args = (i,))
        P.start()
        P.join()

    end_time = time.time()

    print("Execution time is :", end_time - start_time)
        

if __name__ == "__main__":
    main()