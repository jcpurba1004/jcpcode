number = int(input("Enter the numeric grade: "))
if number > 89:
    letter = 'A'
elif number > 79:
    letter = 'B'
elif number > 69:
    letter = 'C'
else:
    letter = 'F'
print("The letter grade is", letter)

#if <condition-1>:
#    <sequence of statements-1>
#elif <condition-n>:
#    <sequence of statements-n>
#else:
#    <default sequence of statements>