#Lists store data of different of same data type as an array
myList1 = ['Sachin', "32", 'Abhijeet', 'Kulkarni', "2.536", "2+3j"]

#Print complete list
print(myList1)

#Print slice of the list
myList2 = myList1[0:3]
print("Sliced list [0:3] :- ", myList2)

print("Printing elements from myList1 from range [1:5]")
for element in myList1[1:5]:
    print("Element :- ", element)

#Add element into list
myList1.append("Shivani")
myList1.append("2-3.5j")

print("Printing list after adding elements :- ", myList1)

myList1.remove("Shivani")

print("Printing list after adding elements :- ", myList1)

myList1.append("Shivani")

myList1.sort()

print("Printing list of values after sorting the list :- ", myList1)
