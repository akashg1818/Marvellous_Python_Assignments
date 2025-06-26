class Employee:

    def __init__(self,A,B,C):
        self.name = A
        self._depatment = B
        self.__salary = C

    def Display(self):
        print("Inside display of Employee ")
        print("Name of Employee is :"+self.name)
        print("Department of employee is :"+self._depatment)
        print("Salary of employee is :",self.__salary)

def main():

    obj1 = Employee("Akash","IT",120000)

    obj1.Display()


if __name__ == "__main__":
    main()