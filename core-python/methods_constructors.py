class DemoClass:
    a = 10
    name = "Keval"

    # Constructors
    def __init__(self):
        print("Hello, Good Morning ")
        print("Today we learn Methods and constructors in Python OOPS ")
        print("Constructors is automatic called when Object is create")
        print("We can't called this its bydefault called when you create object")
        print("the constructor method is named __init__ and start with self")
        print("Here is Example")

        print(self.name)
        self.last = "Kukadiya"

    # Method
    def showvalue(self):
        print(self.a)

    def showvalue1(self):
        print("Welcome Python Developer")


obj = DemoClass()
# print(obj.name + obj.last)
obj.showvalue()
# obj.showvalue1()
