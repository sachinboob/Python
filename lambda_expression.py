"""
General format of Lambda expression

lambda x1, x2, x3, x4,...,xn : RHS (x1, x2, x3,.....,xn, v1,v2,v3,......,vm, c1, c2, c3,.....,ck)
"""

a = 10
b = 20
c = 30

#print((lambda x, y: (a*x+b*y+c*100))(1,2))


F = lambda x, y, z: (x + y + z)

print(type(F))

print(F(1,2,3))

num = (lambda x,y,z: (x**2 + y**2 + z**2))(1,2,3)

print(num)