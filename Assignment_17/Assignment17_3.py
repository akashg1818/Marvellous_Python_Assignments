import time
import schedule

def Display():

    print("Do Coding...!")

def main():
    schedule.every(30).minutes.do(Display)

    while True:
        schedule.run_pending()
        time.sleep(1)
        

if __name__ == "__main__":
    main()