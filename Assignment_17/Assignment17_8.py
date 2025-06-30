def CheckMail():

    print("Checking mail...")

def main():

    schedule.every(20).seconds.do(CheckMail)

    while True:
        schedule.run_pending()
        time.sleep(1)


if __name__ == "__main__":
    main()