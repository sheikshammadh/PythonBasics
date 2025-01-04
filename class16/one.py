# filter and map
numbers=[10,14,525,7356,2524,22,44,3,545]
def check(ele):
    return ele <100
filter(lambda ele:ele<100,numbers)
print(list(filter(lambda ele:ele<100,numbers)))