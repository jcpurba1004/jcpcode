list(range(1, 6, 1))   # Same as using two arguments
list(range(1, 6, 2))   # Use every other number
list(range(1, 6, 3))   # Use every third number

theSum = 0
for count in range(2, 11, 2):
    theSum += count
theSum