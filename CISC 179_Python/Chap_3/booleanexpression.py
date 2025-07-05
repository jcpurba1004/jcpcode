number = int(input("Enter the numeric grade: "))
if number > 100:
    print("Error: grade must be between 100 and 0")
elif number < 0:
    print("Error: grade must be between 100 and 0")
else:
    # The code to compute and print the result goes here

#number = int(input("Enter the numeric grade: "))
#if number > 100 or number < 0:
    print("Error: grade must be between 100 and 0")
#else:
    # The code to compute and print the result goes here

number = int(input("Enter the numeric grade: "))
if number >= 0 or number <= 100:
    # The code to compute and print the result goes here
#else:
    print("Error: grade must be between 100 and 0")

A = True
B = False
A and B
False
#    A or B
True
#    not A
False

A = 2
B = 3
result = A + B * 2 < 10 or B == 2
result
False