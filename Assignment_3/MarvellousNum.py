def CheckPrime(no):

    if(no <= 1):
        return False

    if(no == 2):
        return True           
    
    for i in range(2,no):

        if(no % i == 0):
            return False
           
    return True