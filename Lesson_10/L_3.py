def my_range(start, end=None):
    if end is None:
        start, end = 0, start
    while start < end:
        yield start
        start += 1

r = my_range(12, 51)
a = 0
for i in r:
    a += 1
    if a == 21:
        print(i)