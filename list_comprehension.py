my_range = range(1, 11)

# Format 1
# L = [<x> for <x> in <iterable>]

L1 = [x for x in my_range]
print("List Format 1 :- ", L1)

# Format 2
# L = [<f(x)> for <x> in <iterable>]


def list_comprehension_format_2(x):
    return x**2


L2 = [list_comprehension_format_2(x) for x in my_range]
print("List Format 2 :- ", L2)

# Format 3
# L = [<x> for <x> in <iterable> if <C(<x>)> == True]


def list_comprehension_format_3(x):
    return x % 3 == 0


L3 = [x for x in my_range if list_comprehension_format_3(x) == True]
print("List Format 3 :- ", L3)

L3 = [x for x in my_range if x % 2 == 0]
print("List Format 3 :- ", L3)

# Format 4
# L = [f(x) for x in iterable if C(x) == True]


def list_comprehension_format_4(x):
    return x**3


L4 = [list_comprehension_format_4(x) for x in my_range if x % 2 != 0]

print("List Format 4 :- ", L4)


# Format 5
# L = [(x1, x2,...xn) for x1 in iterable1
#                     for x2 in iterable2
#                     .
#                     .
#                     for xn in iterablen]

L5 = [(x1, x2, x3) for x1 in range(1, 3)
      for x2 in range(3, 5) for x3 in range(5, 7)]
print("List Format 5 :- ", L5)


# Format 6
# L = [f1(x1), f2(x2), ... fn(xn)   for x1 in iterable1
#                                   for x2 in iterable2
#                                   .
#                                   .
#                                   for xn in iterablen]

L6 = [(x1**2, x2**3) for x1 in [1, 2, 3] for x2 in [4, 5, 6]]
print("List Format 6 :- ", L6)


# Format 6
# L = [f1(x1), f2(x2), ... fn(xn)   for x1 in iterable1 if c1(x1) == True
#                                   for x2 in iterable2 if c2(x2) == True
#                                   .
#                                   .
#                                   for xn in iterablen] if cn(xn) == True

L7 = [(x1**2, x2**3) for x1 in my_range if x1 %
      2 == 0 for x2 in my_range if x2 % 2 != 0]
print("List Format 7 :- ", L7)
