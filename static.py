
#1. define a static variable and access that through class
class A:
    static=56
print("Accessing through class ",A.static)

#2. define a static variable and access through an instance
class B:
    var=99
obj=B()
print("Accessing through instance",obj.var)

#3. Define a static variable and change with in the instance
class c:
    val=89
obj=c()
obj.val=90
print("changed throygh the instance " ,obj.val)
print("origianal value" ,c.val)

#4. define a static variable and change within the class
class D:
    val=100
D.val=101
print("changed throygh the class" ,D.val)



