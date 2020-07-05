# While control statement
x = 1
while x <= 10:
    print("x = {}".format(x))
    x = x + 1

print("**********************************************")

# For control statement with range
# range(start, stop, increment)
r = range(0, 20, 3)
# This will print sequence 0, 3, 6,.... 18
for i in r:
    print("i = {}".format(i))

print("**********************************************")

# For control statement with string sequence
str_2 = "SaCH!n"
for ch in str_2:
    print("ch = {}".format(ch))

print("**********************************************")

# For control statement with tuple
tuple_1 = (0, 10, "sachin", 7.5, 9.32433453453345, "boob")
for i in range(0, len(tuple_1), 2):
    print("i = {}".format(tuple_1[i]))

print("**********************************************")

# While control statement
while_count = 0
while while_count in range(9):
    print("count = {}".format(while_count))
    while_count = while_count + 1

print("**********************************************")

# For control statement with list
list_1 = ["sachin", "ramdhan", "boob", 2, 6.5]
for i in range(len(list_1)):
    print("Position {}, item {}".format(i, list_1[i]))

print("**********************************************")

# For control statement with list
for i in range(1, 20, 3):
    print("i = {}".format(i))

print("**********************************************")
