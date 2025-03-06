#1.Create a class with private fiels , private method and  a main method  . print the fields in the main method and call the private method in main method.

# Base class
class Parent:
     
     # public data member
     data1 = None
 
     # protected data member
     _data2 = None
     
     # private data member
     __data3 = None
     
     # constructor
     def __init__(self, data1, data2, data3): 
          self.data1 = data1
          self._data2 = data2
          self.__data3 = data3
     
     # public member function  
     def showPublic(self):
  
          # accessing public data members
          print("Public Data Member: ", self.data1)
        
     # protected member function  
     def _showProtected(self):
  
          # accessing protected data members
          print("Protected Data Member: ", self._data2)
      
     # private member function  
     def __showPrivate(self):
  
          # accessing private data members
          print("Private Data Member: ", self.__data3)
 
     # public member function
     def accessPrivate(self):    
           
          # accessing private member function
          self.__showPrivate()
  
# Derived class
class Child(Parent):
  
      # constructor
       def __init__(self, data1, data2, data3):
                Parent.__init__(self, data1, data2, data3)
           
      # public member function
       def accessProtected(self):
                 
                # accessing protected member functions of parent class
                self._showProtected()
  
# creating object of the derived class    
obj = Child("XYZ", 10, "Secret Data")
 
# calling public member functions of the class
obj.showPublic()
obj.accessProtected()
obj.accessPrivate()
 
# Object can access protected member
print("Object is accessing protected member:", obj._data2)
 
# object cannot access private member, so it will generate AttributeError
# print(obj.__data3)
