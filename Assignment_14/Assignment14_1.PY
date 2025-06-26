class Employee:

    def __init__(self,A,B,C):
        self.name = A
        self.emp_id = B
        self.salary = C 
    
    def Display(self):
        print("Name of employee is :"+self.name)
        print("Employee id is :"+self.emp_id)
        print("Salary of employee is :",self.salary)

def main():

    emp1 = Employee("Akash Guldagad","ABC101",20000)

    emp1.Display()


if __name__ == "__main__":
    main()

