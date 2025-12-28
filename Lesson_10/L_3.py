def my_range(start, end=None):
    if end is None:
        start, end = 0, start
    while start < end:
        yield start
        start += 1

r = my_range(1, 3)
for i in r:
    print(i)