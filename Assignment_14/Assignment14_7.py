class Person:

    def __init__(self,name,age):
        self.Name = name
        self.Age = age
        print("Person constructor called")
    
    def Display(self):
        print("Inside display of Person")
        print(f"Name : {self.Name}\nAge : {self.Age}")


class Teacher(Person):

    def __init__(self,name,age,subject,salary):
        super().__init__(name,age)
        self.Subject = subject
        self.Salary =  salary
        print("Teacher constructor called")
    
    def Display(self):
        super().Display()
        print("Inside display of Teacher")
        print(f"Subject :{self.Subject}\nSalary :{self.Salary}")
        
def main():

    obj = Teacher("Akash",19,"Python",45000)

    obj.Display()

if __name__ == "__main__":
    main()