# 1. Write two methods with the same name but different number of parameters of same type and call the methods  

class MethodOverloading1:
    def add(self, a, b=None):
        if b is None:
            print(f"Single parameter: {a}")
        else:
            print(f"Two parameters: {a + b}")

obj1 = MethodOverloading1()
obj1.add(5)
obj1.add(5, 10)
print()

# 2. Write two methods with the same name but different number of parameters of different data type and call the methods  

class MethodOverloading2:
    def display(self, a=None, b=None):
        if isinstance(a, int) and b is None:
            print(f"Integer parameter: {a}")
        elif isinstance(a, str) and isinstance(b, int):
            print(f"String and Integer parameters: {a}, {b}")

obj2 = MethodOverloading2()
obj2.display(10)
obj2.display("Hello", 20)
print()

# 3. Write two methods with the same name and same number of parameters of same type  

class MethodOverloading3:
    def show(self, x):
        print(f"First method: {x}")

    def show(self, x):
        print(f"Second method: {x}")

obj3 = MethodOverloading3()
obj3.show(50)  
