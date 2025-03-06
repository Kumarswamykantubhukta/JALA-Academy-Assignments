# 1. Write a class with a default constructor, one argument constructor, and two argument constructors. 

class MyClass:
    def __init__(self, a=None, b=None):
        if a is None and b is None:
            print("Default Constructor Called")
        elif b is None:
            print(f"One Argument Constructor Called: {a}")
        else:
            print(f"Two Argument Constructor Called: {a}, {b}")


obj1 = MyClass()          
obj2 = MyClass(10)       
obj3 = MyClass(10, 20)   
print()

# 2. Call the constructors (both default and argument constructors) of super class from a child class.

class Parent:
    def __init__(self, x=None):
        if x is None:
            print("Parent Default Constructor")
        else:
            print(f"Parent Argument Constructor: {x}")

class Child(Parent):
    def __init__(self, y=None):
        if y is None:
            super().__init__()  
            print("Child Default Constructor")
        else:
            super().__init__(y)  
            print(f"Child Argument Constructor: {y}")


child1 = Child()       
child2 = Child(50)     
print()

# 3. Apply private, public, protected, and default access modifiers to the constructor.

class AccessModifiers:
    def __init__(self):          # Public Constructor
        print("Public Constructor Called")

    def _protected_method(self): # Protected Method
        print("Protected Method Called")

    def __private_method(self):  # Private Method
        print("Private Method Called")

# Creating object
obj = AccessModifiers()
obj._protected_method()   
print()

# 4. Write a program which illustrates the concept of attributes of a constructor.

class AttributesExample:
    def __init__(self, name, age):
        self.name = name  
        self.age = age   
    
    def display(self):
        print(f"Name: {self.name}, Age: {self.age}")

person = AttributesExample("Alice", 30)
person.display()
