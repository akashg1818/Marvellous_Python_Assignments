import os
import time
import psutil 
import schedule 
import sys

def CreateLog(FolderName,Data):

    Ret = os.path.exists(FolderName)
    if(Ret == False):
        os.mkdir(FolderName)

    timestamp = time.ctime()
    timestamp = timestamp.replace(" ","")
    timestamp = timestamp.replace(":","_")
    timestamp = timestamp.replace("/","_")

    FileName = os.path.join(FolderName, "ProcessLog%s.Log"%(timestamp))

    fobj = open(FileName, "w")

    border = "-"*80
    fobj.write(border)
    fobj.write("\n\t\tProcess Log File\n")
    fobj.write("\t\tLog file is created at : "+time.ctime()+"\n")
    fobj.write(border)
    fobj.write("\n")
    
    for value in Data:
        fobj.write("%s\n\n"%value)

    fobj.write(border)

    fobj.close()

    print("Sucess")

def ProcInfo(name):

    processinfo = []

    for proc in psutil.process_iter(['name']):

        try:
            if(proc.info ['name'] == name):
                info = proc.as_dict(attrs = ['pid','name','username'])
                processinfo.append(info)

        except(psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass 

    return processinfo

def main():

    if(len(sys.argv) == 2):

        if(sys.argv[1] == "--h" or sys.argv[1] == "--H"):
            print("This is process automation script")
            print("Script return the informstion about running process")
            print("Use --u for the usage ")

        elif(sys.argv[1] == "--u" or sys.argv[1] == "--U"):
            print("Use this script as ")
            print("python Filename.py ArgumentNO1 AgumrntNO2")
            print("ArgumentNO1 - Name of folder")
            print("ArgumentNO2 - Time interval ")
            print("ArgumentNO2 - Name of process ")

        else:
            print("Wrong number of Arguments")
            print("Use --h for help")
            print("Use --u for usage")

    elif(len(sys.argv) == 4):

        Arr = ProcInfo(sys.argv[3])

        FolderName = sys.argv[1]
        Timeinterval = int(sys.argv[2])
        
        schedule.every(Timeinterval).seconds.do(CreateLog, FolderName,Arr)
        
        while True:
            schedule.run_pending()
            time.sleep(1)
    
    else:
        print("Wrong number of Arguments")
        print("Use --h for help")
        print("Use --u for usage")


if __name__  ==  "__main__":
    main()