# 1.1. Adding the values in dictionary  

students = {
    101: "Alice",
    102: "Bob",
    103: "Charlie",
    104: "David",
    105: "Emma"
}
print("Student Dictionary:", students)
print()

# 1.2. Updating the values in dictionary  

students[103] = "Charlie Brown"
print("Updated Dictionary:", students)
print()

# 1.3. Accessing the value in dictionary  

print("Accessing Student ID 102:", students[102])
print()

# 1.4. Create a nested loop dictionary  

nested_students = {
    101: {"Name": "Alice", "Age": 20, "Grade": "A"},
    102: {"Name": "Bob", "Age": 21, "Grade": "B"},
    103: {"Name": "Charlie", "Age": 22, "Grade": "A"},
}
print("Nested Dictionary:", nested_students)
print()

# 1.5. Access the values of nested loop dictionary  

print("Accessing Charlie's Age:", nested_students[103]["Age"])
print()

# 1.6. Print the keys present in a particular dictionary  

print("Keys in Student Dictionary:", students.keys())
print()

# 1.7. Delete a value from a dictionary  

del students[104]
print("Dictionary after deletion:", students)
