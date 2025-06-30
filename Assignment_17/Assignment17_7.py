import datetime
import schedule
import time
import os

def BackupFile(File1,File2):

    ret1 = os.path.exists(File1)
    if(ret1 == False):
        print("File not found :",File1)
        exit()

    ret2 = os.path.exists(File2)
    if(ret2 == False):
        print("File not found :",File2)
        exit()


    
    fobj1 = open(File1,"r")
    Data = fobj1.read()

    fobj2 = open(File2,"w")
    fobj2.write(Data)

    fobj1.close()
    fobj2.close()
    

    Mobj = open("Backup_Log.txt","a")
    Mobj.write("Backup of file completed at :")
    Mobj.write(str(datetime.datetime.now()))
    Mobj.write("\n")

    Mobj.close()

    print("Backup completed")


def main():

    print("Enter the name of file that you wants to back up :")
    Fname1 = input()
    print("Enter the name of file in which you wants backup :")
    Fname2 = input()

    schedule.every(1).minutes.do(lambda: BackupFile(Fname1,Fname2))

    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()