# Inheriting Attributes and Methods:
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print(f"Hello {self.name}")
        # pass  # Placeholder method, to be overridden in subclasses


class Dog(Animal):
    def bark(self):
        print("Woof!")


# Creating an instance of the Dog class
my_dog = Dog("Buddy")

# Inherited attributes and method
print(my_dog.name)  # Output: Buddy

my_dog.speak()  # Calls the speak method from the Animal class


# Overriding Methods:
class Cat(Animal):
    def speak(self):
        print("Meow !!")


my_cat = Cat("Ruju")

my_cat.speak()


class A:
    def method_a(self):
        print("Method A")


class B:
    def method_b(self):
        print("Method B")


class C(A, B):
    def method_c(self):
        print("Method C")


# Creating an instance of the C class
my_instance = C()
print(my_instance)
# Accessing methods from both A and B
my_instance.method_a()  # Output: Method A
my_instance.method_b()  # Output: Method B
my_instance.method_c()  # Output: Method C
