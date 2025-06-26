class Student:

    SchoolName = "J N V Solapur"

    def __init__(self,A,B):
        self.name = A
        self.roll_no = B
    
    def Display(self):
        print("Name of employee is :"+self.name)
        print("Roll number is :",self.roll_no)
        

    
    def ChangeName(self):
        Student.SchoolName =  "JNV Solapur"
        print("Updated School name is :"+Student.SchoolName)
    

def main():

    print("School name is :"+Student.SchoolName)

    obj1 = Student("Akash Guldagad",1002)

    obj1.Display()
    obj1.ChangeName()

if __name__ == "__main__":
    main()

