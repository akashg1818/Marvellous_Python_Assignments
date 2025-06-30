import time
import schedule

def Display():

    print("Namaskar..!")

def main():
    schedule.every().day.at("09:00").do(Display)

    while True:
        schedule.run_pending()
        time.sleep(1)