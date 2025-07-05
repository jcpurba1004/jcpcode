for count in range(4):
    print(count, end = " ")

product = 1
for count in range(4):
    product = product * (count + 1)
product

product = 1
for count in range(1, 5):
    product = product * count
product

#for <variable> in range(<lower bound>, <upper bound + 1>):
#    <loop body>

lower = int(input("Enter the lower bound: "))
upper = int(input("Enter the upper bound: "))
theSum = 0
for number in range(lower, upper + 1):
    theSum = theSum + number
theSum