import random;
import sys;

#Code to learn variables
#Declare multiple variables and assign them values
name, age, blood_group, is_happy = "Sachin", 30, "B+", True
random_number = random.randrange(1,999);

# Format String using {}
print("Subject name is : {0}, age : {1}, blood group : {2}".format(name, age,blood_group));
print("Subject {0} is assigned the random id : {1}".format(name,random_number));
print("Is subject {0} happy?? ----- Answer is : {1}".format(name,is_happy));

# Format String using placeholder
print("Subject name is : %s, age : %s, blood group : %s"%(name, age,blood_group));