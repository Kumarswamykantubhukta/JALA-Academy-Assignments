# 1. write a programme to print bright IT career ten times using for loop
for _ in range(10):
    print("Bright IT career")

# 2. write a programme to print 1 to 20 numbers using while loop
i=1
while i<21:
    print(i,end=" ")
    i+=1
print()


#3.programme to equal operator and not equal operator
a,b=10,20
print(a==b)
print(a!=b)


#4 write a programme to print odd and even number
val=int(input("enter the number to check even or odd = "))
if val%2==0:
    print("Even number")
else:
    print("Odd number")


#5.write a programme to print the largest number among three numbers
a,b,c=10,30,20
print(a if a>b and a>c else b if b>a and b>c else c)

#6.write a programme to print even numbers between 10 20 using while loop
i=10
while i<21:
    if i%2==0:
        print(i,end=" ")
    i+=1
print()

#7.write a programme to print 1 to 10 using the while loop statement
i=1
while i<11:
    print(i,end=" ")
    i+=1
print()


#8.write a programme to find armstrong number or not 

n=153
val=n
count=0
while val>0:
    rem=val%10
    count+=rem**3
    val//=10
if n==count:
    print(f"{n} is a armstrong number .")
else:
    print(f"{n} is not an armstrong number")

#9. write a programme to find prime or not
n=97
check=False
for i in range(2,n//2):
    if n%i==0:
        print(f"{n} is not a Prime Number")
        check=True
        break
if not check:
    print(f"{n} is a prime number")

#10.write a programme to palindrome or not
val=121
val=str(val)
if val==val[::-1]:
    print(val+ " is a palindrome")
else:
    print(val+" is not a palindrome")

#11. write a programme to print if a number is even or odd
val=9
print("{} is Even".format(val) if val%2==0 else "{} is Odd ".format(val))

#12.print male or female programme according to given m/f using elif 

val="M"
if val=="M":
    print("Male")
elif val=="F":
    print("Female")
