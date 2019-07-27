import sys;

students = {"Sachin" : 45, "Abhijeet": 55, "Ganesh" : 67};

print (students.keys());

print(students.get("Sachin"));
print(students["Ganesh"]);

del students["Ganesh"]

print("Length of students dictionary :- " + str(len(students)))