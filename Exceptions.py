# 1. Write a program to generate Arithmetic Exception without exception handling 

result = 10 / 0  
print()

# 2. Handle the Arithmetic exception using try-catch block  

try:
    result = 10 / 0
except ZeroDivisionError:
    print("Arithmetic Exception: Division by zero is not allowed")
print()

# 3. Write a method which throws exception, Call that method in main class without try block  

def throw_exception():
    raise ValueError("This is a manually raised exception")

throw_exception()
print()

# 4. Write a program with multiple catch blocks  

try:
    num = int("abc")  
except ZeroDivisionError:
    print("Cannot divide by zero")
except ValueError:
    print("Invalid input: Cannot convert string to integer")
print()

# 5. Write a program to throw exception with your own message  

try:
    raise Exception("This is a custom exception message")
except Exception as e:
    print(e)
print()

# 6. Write a program to create your own exception  

class MyCustomException(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)

try:
    raise MyCustomException("This is my own custom exception")
except MyCustomException as e:
    print(f"Caught MyCustomException: {e}")


# 7. Write a program with finally block  

try:
    result = 10 / 2
    print("Result:", result)
except ZeroDivisionError:
    print("Cannot divide by zero")
finally:
    print("This block always executes")
print()

# 8. Write a program to generate Arithmetic Exception  

try:
    result = 10 / 0
except ArithmeticError:
    print("Caught an Arithmetic Exception")
print()

# 9. Write a program to generate FileNotFoundException  

try:
    file = open("non_existent_file.txt", "r")
except FileNotFoundError:
    print("FileNotFoundException: File does not exist")
print()

# 10. Write a program to generate ClassNotFoundException  

try:
    import nonexistent_module  
except ModuleNotFoundError:
    print("ClassNotFoundException: Module not found")
print()

# 11. Write a program to generate IOException  

import os

try:
    os.remove("readonly_file.txt")  
except OSError as e:
    print("IOException: OS Error occurred -", e)
print()

# 12. Write a program to generate NoSuchFieldException  

class Example:
    def __init__(self):
        self.value = 10

obj = Example()
try:
    print(obj.non_existent_field)  
except AttributeError:
    print("NoSuchFieldException: Attribute does not exist")
