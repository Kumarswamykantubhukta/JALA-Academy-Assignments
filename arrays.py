#1.write a function to add integer values of an array
arr=[1,2,2,4,5]
val=sum(arr)
print(val)

#2. write a function to find the average value of an array of integers
arr=[1,2,2,4,5]
val=sum(arr)/len(arr)
print(val)

#3. write a programme to find the index of an array element
arr=[1,2,2,4,5]
print(arr.index(5))

#4. write a function to test if a array contains specif value
arr=[1,2,2,4,5]
val=5
if val in arr:
    print("Yes {} is present in arr".format(val))
else:
    print("element not found")

#5. write a function to remove a specific element from an array
arr=[1,2,2,4,5]
element=5
arr.remove(element)
print(*arr)

#6. write a function to copy an array to another array
arr=[1,2,2,4,5]
newarr=arr.copy()
print(*newarr)

#7. write a function to insert an element at a specific position in the arr
arr=[1,2,2,4,5]
element=89
index=1
arr.insert(1,element)
print(*arr)

#8.write a function to find out the minimum and maximum of an array
arr=[1,2,2,4,5]
print("minval is",min(arr),"maxval is",max(arr))

#9.write a function to reverse an array
arr=[1,2,2,4,5]
print("original array ",*arr)
arr.reverse()
print("reversed array ",*arr)

#10.write a function to find the duplicate values of an array
arr=[1,2,2,4,4,5]
s=set()
dupli=[]
for i in arr:
    if i not in s:
        s.add(i)
    else:
        dupli.append(i)
print("Dupliacate elements are ",*dupli)

#11.write a programme to find out the common values between two arrays
arr=set([1,2,2,4,5])
arr2=set([2,3,4,6,7])
print(arr.intersection(arr2))

#12. write a method to remove the duplicate elements from an array
def dupli(arr):
    val=list(set(arr))
    return val
print(dupli([1,2,2,3,3,4,5,5]))

#13. write a method to find out the second largest in an array
def secondlarge(arr):
    second,maxindex=-1,-1
    for i in range(len(arr)-1):
        if arr[i]> arr[i+1]:
            maxindex=i
    for i in range(len(arr)-1):
        if i!=maxindex:
            if arr[i]>arr[i+1]:
                second=i
    return arr[second]
val=secondlarge([1,2,3,4,7,6])
print("second maximum val is ",val)


#15.write a method to return the number of even and odd numbers in an array
def evenodd(arr):
    odd,even=0,0
    for i in arr:
        if i%2==0:
            even+=1
        else:
            odd+=1
    return even, odd
val=evenodd([1,2,3,4,5,6,7])
print(f"the number of even indexes {val[0]}  And the number of odd indexes are {val[1]}")


#16.write a function to get the difference between the largest and smallest value
arr=[1,2,2,4,5]
largest=max(arr)
smallest=min(arr)
print("The difference is ",largest-smallest)


#17. write a method to verify if an array contains two specified elements (12,23)
arr=[1,2,2,4,5,12,23]
def contains(arr,one,two):
    if one in arr and two in arr:
        print("The two elements are in the array")
    else:
        print("Either one or two elements are not there in the aray")
contains(arr,12,23)


#18.write a programme to remove the duplicates from the array and return the newarr
arr=[1,2,2,4,5]
newarr=[]
for i in arr:
    if i not in newarr:
        newarr.append(i)
    else:
        continue
print("The new array is ",*newarr)
