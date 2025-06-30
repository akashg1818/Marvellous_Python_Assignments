import time
import schedule
import datetime

def Display():

    print("Inside Display at :",datetime.datetime.now())

def main():
    print("Inside main at :",datetime.datetime.now())

    schedule.every(10).seconds.do(Display)

    while True:
        schedule.run_pending()
        time.sleep(1)
        

if __name__ == "__main__":
    main()