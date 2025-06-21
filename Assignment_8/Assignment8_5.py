import threading
import time

def Thread1(no):

    print("Inside Thraed1 :")

    for i in range(no+1):
        print(i)
        

def Thread2(no):

    print("Inside Thread2 :")

    sum = 0
    for i in range(no,0,-1):         
        print(i)

def main():

    print("Inside main")

    Start_time = time.time()

    T1 = threading.Thread(target= Thread1, args = (50,))
    T2 = threading.Thread(target = Thread2, args =(50,))

    T1.start()
    T1.join()

    T2.start()
    T2.join()

    End_time = time.time()

    print("Execution time is :",End_time - Start_time)

    print("End of main")

if __name__ == "__main__":
    main()