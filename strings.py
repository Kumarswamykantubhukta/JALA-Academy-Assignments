#1. Different ways creating a string
one="first"
two='two'
three="""Third"""
four=three[:-1]
print(one,two,three,four)

#2.concatinating two string using + operator
print(one+two)

#3. finding the length of the string
print("The length of the string",len(four))

#4.extract a string using a substring

#5.searching in string using index
one="kumarswamy"
two="swamy"
three="mars"
print("position of two in one ",one.index(two))
print("position of three in one ",one.index(three))


#6.Matching a string with regular expressions with matches()
import re
sub="umar"
new="um"
val=re.search(new,sub)
print(val)


#7. Comparing strings.
name1 = 'kumar swamy'
name2 = 'ayyappa swamy'
name3 = name1
print(name1 == name2)
print(name1 == name3)
print(name2 == name3)
print(name1 != name2)
print()

#8. startsWith(), endsWith().
fullname = 'viratkohli'
print(fullname.startswith("virat"))
print(fullname.endswith("kohli"))
print()

# 9.Trimming strings with strip().
text = 'Hello World hi'
print(text.strip("hi"))
print()

# 10.Replacing characters in strings with replace()
greeting = 'Hi World'
print(greeting.replace("Hi","Hello"))
print()

#11. Splitting strings with split()
words = 'hi-hello-bye'
print(words.split("-"))
print()

#12. Converting integer objects to Strings.
num = 10
num_str = str(num)
print(num_str)
print(type(num_str))

print()
#13. Converting to uppercase and lowercase.
word1 = 'hello'
word2 = 'WORLD'
print(word1.upper())
print(word2.lower())



