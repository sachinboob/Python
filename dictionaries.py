import sys;

students = {"Sachin" : 45, "Abhijeet": 55, "Ganesh" : 67};

print("Length of students dictionary :- " + str(len(students)))

print (students.keys());

print(students.get("Sachin"));
print(students["Ganesh"]);

del students["Ganesh"]

#Below code throws error - KeyError: 'Ganesh'
print(students["GaMesh"])

print("Length of students dictionary :- " + str(len(students)))