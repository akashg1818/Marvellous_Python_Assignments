import threading
import time

def EvenList(no):

    print("Inside DisplayEven")
    sum = 0
    for i in no:
        if(i % 2 == 0):
            sum = sum + i
    print("sum of even factors is :",sum)
        

def OddList(no):

    print("Inside DisplayOdd")

    sum = 0
    for i in no:         
        if(i % 2 != 0):
            sum = sum + i
    print("sum of odd factors is :",sum)

def main():

    print("Inside main")

    Start_time = time.time()

    print("Enter the number of values that you want to enter :")
    value = int(input())

    data = []

    for i in range(value):
        no = int(input())
        data.append(no)

    print(data)
        

    T1 = threading.Thread(target= EvenList, args = (data,))
    T2 = threading.Thread(target = OddList, args =(data,))

    T1.start()
    T2.start()

    T1.join()
    T2.join()

    End_time = time.time()

    print("Execution time is :",End_time - Start_time)

    print("End of main")

if __name__ == "__main__":
    main()