import sys

var1 = 20
var2 = 5 + 5

print("var1 memory location = {}, var2 memory location = {}".format(id(var1), id(var2)))
print("var1 reference count ={}".format(sys.getrefcount(var1)))
print("var2 reference count ={}".format(sys.getrefcount(var2)))

var3 = 5.5
var4 = 6.5 - 1.0

print("var3 memory location ={}, var4 memory location ={}".format(id(var3), id(var4)))
print("var1 reference count ={}".format(sys.getrefcount(var1)))
print("var2 reference count ={}".format(sys.getrefcount(var2)))

var5 = 1 + 2j
var6 = 1 + 2j

print("var5 memory location ={}, var6 memory location ={}".format(id(var5), id(var6)))
print("var1 reference count ={}".format(sys.getrefcount(var1)))
print("var2 reference count ={}".format(sys.getrefcount(var2)))

var5 = None
var6 = None

print("var5 memory location ={}, var6 memory location ={}".format(id(var5), id(var6)))
print("var1 reference count ={}".format(sys.getrefcount(var1)))
print("var2 reference count ={}".format(sys.getrefcount(var2)))

# del var3, var4, var5, var6

# print("var5 memory location after removal ={}".format(id(var5)))

print("var1 reference count ={}".format(sys.getrefcount(var1)))
print("var2 reference count ={}".format(sys.getrefcount(var2)))

print(globals())
