class BankAccount:

    ROI = 10.5

    def __init__(self,A,B):
        self.Name = A
        self.Amount = B

    def Deposit(self,X):
        self.Amount = self.Amount + X
        
    def Withdraw(self,Y):
        self.Amount = self.Amount - Y
    
    def CalculateIntrest(self):
        Intrest = 0
        Intrest = ((self.Amount * BankAccount.ROI* 1)/ 100)
        print("Intrest per year is :",Intrest)

    def Display(self):
        print("Account holder is :",self.Name)
        print("Account balance is :",self.Amount)

def main():

    obj1 = BankAccount("Akash Guldagad",10000)
    obj1.Deposit(2000)
    obj1.Withdraw(5000)
    obj1.Display()
    obj1.CalculateIntrest()
    

    obj2 = BankAccount("Ankita Guldagad",20000)

    obj2.Deposit(5000)
    obj2.Withdraw(4000)
    obj2.Display()
    obj2.CalculateIntrest()
    
    
if __name__ == "__main__":
    main()