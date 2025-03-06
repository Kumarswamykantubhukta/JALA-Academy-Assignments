from abc import ABC, abstractmethod
 
class Shape(ABC): # Base class / Super class
 
    @abstractmethod
    def sides_count(self):
        pass
 
class ThreeSided(Shape): # Subclass
 
    # Overriding abstract method
    def sides_count(self):
        print("ThreeSided: I have 3 sides")
 
class FiveSided(Shape): # Subclass
 
    # Overriding abstract method
    def sides_count(self):
        print("FiveSided: I have 5 sides")
 
class SixSided(Shape): # Subclass
 
    # Overriding abstract method
    def sides_count(self):
        print("SixSided: I have 6 sides")
 
class FourSided(Shape): # Subclass
 
    # Overriding abstract method
    def sides_count(self):
        print("FourSided: I have 4 sides")
 
# Driver code
# Creating the objects to call the abstract method.
obj1 = ThreeSided()
obj1.sides_count()
 
obj2 = FourSided()
obj2.sides_count()
 
obj3 = FiveSided()
obj3.sides_count()
 
obj4 = SixSided()
obj4.sides_count()
