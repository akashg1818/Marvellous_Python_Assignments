import time
import schedule

def LunchTime():

    print("Its lunch time.")

def Finish():

    print("Wrap up the work.")

def main():
    schedule.every().day.at("13:00").do(LunchTime)

    schedule.every().day.at("18:00").do(Finish)

    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()