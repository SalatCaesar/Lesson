dict1 = {2:3, 4:5}
dict2 = {i: n+2 for i, n in dict1.items()}
print(dict2)
a = [1, 2, 1, 2, 3]
print(len(set(a)))
b= set(a)
o = {1, 2, 7, 4}
print(b.isdisjoint(o))
print(b == o)
print(o.issubset(b))
print(o.symmetric_difference(b))
print(o)
print(o)
print(o)
print(o)

square = lambda x: (x**2)
print(square(10.1))