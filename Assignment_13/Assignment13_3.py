class Numbers:

    def __init__(self,A):
        self.value = A

    def CheckPrime(self):

        flag = True
        
        if(self.value == 1 or self.value == 0):
            flag = False
            return flag

        if(self.value == 2):
            return flag

        for i in range(2,self.value):
            if(self.value % i == 0):
                flag =  False
                break

        return flag

        if(flag == True):
            print(self.value,"is prime number.")
        else:
            print(self.value,"is not prime.")

    
    def CheckPerfect(self):
        sum = 0
        for i in range(1,self.value+1):
            if(self.value % i == 0):
                sum = sum + i
        
        if(sum == self.value):
            print(self.value, "is perfect number.")
        else:
            print(self.value,"is not perfect number.")     
    
    def SumFactors(self):
        sum = 0
        for i in range(1,self.value+1):
            if(self.value % i == 0):
                sum = sum + i
        print("Sum of factors of",self.value,"is :",sum)

    def Factors(self):
        print("Facotors of",self.value,"are :")
        for i in range(1,self.value+1):
            if(self.value % i == 0):
                print(i,end = " ")
        print()



def main():

    obj1 = Numbers(12)

    ret = obj1.CheckPrime()
    if(ret == True):
        print("It is prime number.")
    else:
        print("It is not prime.")

    obj1.CheckPerfect()
    obj1.Factors()
    obj1.SumFactors()
       

if __name__ == "__main__":
    main()