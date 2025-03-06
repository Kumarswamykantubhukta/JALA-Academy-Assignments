# 1. Write a programme to print your name
print("Kantubhukta Kumarswamy")

#2. Write a programme for single line comment and multi-line comment
# This is the single line comment 
'''This is the multiline comment
   Multiple line are effected with this comment'''
# And also mutilple # also applies for multiline comments


#3.Define variable for different data types int,Boolean,char,float,string and print on the console
one,two,three,four=5,True,'H',7.89
print(type(one),type(two),type(three),type(four))

#4.Define the local and global variables with the same name and print both variables and understand the scope of variables
val=78
def func():
    val=90
    print("local variable",val)
func()
print("gloval variable",val)
# In the above function the val is redefined inside the function so val inside the function acts as local variable its scope is within the block.
# In order to access the variable with same name inside the function we need to use global keyword
val=78
def function():
    global val
    val=80
    print("globla variable accessed",val)
function()
# In the above function we have accessed the global variable and also changed its value.