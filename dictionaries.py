#Dictionary act as map
#Stores data as key, value pairs
students = {"Sachin": 100, "Abhijeet": 55, "Ganesh": 67}

print("Length of students dictionary :- " + str(len(students)))

print("Keys in the students dictionary ", students.keys())
print("Items in the students dictionary ", students.items())

print("Sachin :- ", students.get("Sachin"))
print("Ganesh :- ", students["Ganesh"])

# Delete Ganesh from the dictionary
del students["Ganesh"]

# Below code throws error - KeyError: 'Ganesh' since the key Ganesh is already deleted
# print(students["Ganesh"])

print("Length of students dictionary after removing one Key :- " + str(len(students)))

# Add new object in the dictionary
students["Shivani"] = 24
students["Vaijyanti"] = 31

print("Length of students dictionary after adding two objects :- ", len(students))
