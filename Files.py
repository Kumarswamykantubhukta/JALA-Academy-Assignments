# 1. Write a program to read a text file 

file1 = open("Sample.txt", "r")
content = file1.read()
print(content)
print()

# 2. Write a program to write text to .txt file using InputStream 

file2 = open("Output.txt", "w")
text = input("Enter text to write in file: ")
file2.write(text)
file2.close()
print("Text written successfully!")
print()

# 3. Write a program to read a file stream 

file3 = open("Sample.txt", "r")
print(file3.readline())
file3.close()
print()

# 4. Write a program to read a file stream supports random access 

file4 = open("Sample.txt", "r+")
print("Current File Position:", file4.tell())
file4.seek(10)
print("File Position after seeking:", file4.tell())
print()

# 5. Write a program to read a file just to a particular index using seek() 

file5 = open("Sample.txt", "r")
file5.seek(5)
print(file5.read(10))  # Reads 10 characters from index 5
file5.close()
print()

# 6. Write a program to check whether a file is having read access and write access permissions 

import os

filename = "Sample.txt"

if os.access(filename, os.R_OK):
    print(f"{filename} has read access")
else:
    print(f"{filename} does not have read access")

if os.access(filename, os.W_OK):
    print(f"{filename} has write access")
else:
    print(f"{filename} does not have write access")
