lambda <argname-1, ..., argname-n>: <expression>

data = [1, 2, 3, 4]
reduce(lambda x, y: x + y, data)
reduce(lambda x, y: x * y, data)

def summation(lower, upper):
    """Returns the sum of the numbers form lower 
    through upper."""
    if lower > upper:
        return 0
    else:
        return reduce(lambda x, y: x + y,
                      range(lower, upper + 1))