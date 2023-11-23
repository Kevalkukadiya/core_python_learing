class A:
    def displayA(self):
        print("Welcome to Nivzen Tech")


# Mutlilevel Inheritance
class B(A):
    def displayB(self):
        print("Welcome to Backend Group")


object = B()
# object.displayA()
# object.displayB()


# Mutiple Inheritance
class First:
    def first(self):
        return "This"


class Second(First):
    def second(self):
        return "is a"


class Multiple_Inheritance(Second, First):
    def multiple_inheritance(self):
        return "Multiple Inheritance example "


perry = Multiple_Inheritance()
print(perry.first(), perry.second(), perry.multiple_inheritance())
