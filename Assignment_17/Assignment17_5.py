import time
import schedule
import datetime

def Display():

    fobj = open("Hello.txt", "a")
    Data = datetime.datetime.now()

    fobj.write("Current time to file is :")
    fobj.write(str(Data))
    fobj.write("\n")

    fobj.close()
    print("Display function gets called")
def main():
    schedule.every(5).minutes.do(Display)

    while True:
        schedule.run_pending()
        time.sleep(1)
        

if __name__ == "__main__":
    main()