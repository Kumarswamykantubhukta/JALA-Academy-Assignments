# 1. write a function for arithmetic operators (+,-,*,//)
def function():
    a,b=98,87
    print("Addition of a and b = ",a+b)
    print("Subtraction of a and b = ",a-b)
    print("Multiplication of a and b = ",a*b)
    print("Division of a and b = ",a//b)
function()

# 2. write a method for incrementing and decrementing operators
def incDec():
    a,b=10,10
    print("Before incrementing and decrementing = ",a,b)
    a+=1
    b-=1
    print("After incrementing and decrementng = ",a,b)
incDec() 

#3. Write a programme to find the two numbers equal or not
one,two=56,56
if one==two:
    print("Two numbers are equal")
else:
    print("Two numbers are not equal")

#4. programme for relational operators <,>,<=,>=
one,two=10,100
three,four=89,78
five=six=77
def operators(one,two):
  if one<two:
    print(f"{one} is less than {two}")
  elif one>two:
    print(f"{one} greater than {two}")
  elif one>=two:
    print(f"{one} greater than or equal to {two}")
operators(one,two)
operators(three,four)
operators(five,six)

#5.Print the smaller and larger number
arr=[1,2,3,4,5]
print("The smaller number is = ",min(arr))
print("The larger number is = ", max(arr))
