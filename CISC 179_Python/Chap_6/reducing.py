from functools import reduce
def add(x, y): return x + y
def multiply(x, y): return x * y
data = [1, 2, 3, 4]
reduce(add, data)
reduce(multiply, data)