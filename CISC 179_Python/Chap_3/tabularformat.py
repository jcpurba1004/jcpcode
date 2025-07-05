for exponent in range(7, 11):
    print(exponent, 10 ** exponent)

"%6s" % "four"   # Right justify
"%-6s" % "four"  # Left justify

    #<format string> % <datum>

    #<format string> % (<datum-1>, ..., <datum-n>)

for exponent in range(7, 11):
    print("%-3d%12d" % (exponent, 10 ** exponent))

#<field width>.<precision>f

salary = 100.00
print("Your salary is $" + str(salary))
print("Your salary is $%0.2f" % salary)
#"%6.3f" % 3.14