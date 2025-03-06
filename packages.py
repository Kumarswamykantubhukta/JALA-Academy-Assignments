# 1.1. Create a constructor and a method for each class

class FirstClass:
    def __init__(self, name):
        self.name = name
    
    def display(self):
        print(f"Hello from FirstClass, {self.name}!")


class SecondClass:
    def __init__(self, age):
        self.age = age
    
    def show(self):
        print(f"Your age from SecondClass: {self.age}")


# 1.2. Create a __init__.py for adding all packages
# (Since we are writing everything in a single file, we simulate this by defining classes directly)


# 1.3. Import the respective packages
# (No need for explicit imports as classes are already defined in this file)


# 1.4. Call each class by creating an object to it

obj1 = FirstClass("Alice")
obj1.display()

obj2 = SecondClass(25)
obj2.show()
