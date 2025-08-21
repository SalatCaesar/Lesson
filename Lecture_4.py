list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
str = '1234567890'
tuple = (1, 2, 3, 4, 5, 6, 7, 8, 9, 0)
print(list)
print(str)
print(tuple)
for i in list:
    print(i + 1)
print()
for i in str:
    print(int(i)+1)
print()
for i in tuple:
    print(tuple[i-1::2])
print()
d = 0
for i in list:
    if list[i-1] % 2 == 0:
     d += list[i-1]
print(d)
print()

a = 2
z = 2
print(a is z)