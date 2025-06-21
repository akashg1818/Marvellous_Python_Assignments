
import threading 
import time

def Display():

    for i in range(1,6):
        print(i)
        time.sleep(1)


def main():

    print("Inside main")

    Start_time = time.time()

    T1 = threading.Thread(target = Display)
    T2 = threading.Thread(target = Display)
    T3 = threading.Thread(target = Display)

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