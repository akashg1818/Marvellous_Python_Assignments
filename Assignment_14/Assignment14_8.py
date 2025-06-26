class Vehicle:

    def Display(self):
        print("Display function of vehicle")
    
    def Start(self):
        print("Inside Start of Vehicle")

    def Type(self):
        print("Type of vehicle is ")
        

class Car(Vehicle):

    def Start(self):
        print("Inside Start of Car")

    def Display(self):
        print("Display function of Car")       

    def Brand(self):
        print("Brand of car is")
        
def main():

    obj = Car()
    obj.Start()
    obj.Display()
    obj.Brand()
    obj.Type()

if __name__ == "__main__":
    main()