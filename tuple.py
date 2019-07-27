import sys

tuple1 = ("sachin","abhijeet","ganesh")

print(tuple1)

print(tuple1[0])

#Below code throws - IndexError: tuple index out of range
#print(tuple1[3])

tuple2 = ("shivani","vaijayanti")

tuple3 = tuple1 + tuple2

print(tuple3)

#Below code print tuple3 three times
print(tuple3*3)

#Belo code throws error
print(tuple3 + 5)