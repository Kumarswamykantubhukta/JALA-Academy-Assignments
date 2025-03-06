class A():  
    def present(p):
        print("Present Inside class A ")
 # class A exhibit method    
    def exhibit(self):
        print("Exhibit Inside class A")
    
# Inherited or Sub class (Note A in bracket) 
class B (A): 
    def showcase(sh):
        print("Showcase Inside class B")    
    # class B exhibit method
    def exhibit(self):
        print("Exhibit Inside class B")
    
# Inherited or Sub class (Note B in bracket) 
class C (B): 
          
    # class C exhibit method
    def exhibit(self):
        print("Exhibit Inside class C ")         

# Driver code 
obj_a = A()
obj_a.present()
obj_b = B()
obj_b.showcase()
obj_c = C()   
obj_c.exhibit()
