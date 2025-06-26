class Product:

    def __init__(self,A,B):
        self.Name = A
        self.Price = B

    def __eq__(self,other):
        return self.Price == other.Price


def main():

    obj1 = Product("Watch",1000)
    obj2 = Product("Headphone",1000)
    obj3 = Product("Cap",600)

    print(obj1 == obj2)
    print(obj1 == obj3)


if __name__ == "__main__":
    main()
