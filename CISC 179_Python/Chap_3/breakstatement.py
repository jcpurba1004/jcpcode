theSum = 0.0
#while True:
#    data = input("Enter a number or just enter to quit: ")
#    if data == "":
#        break
#    number = float(data)
#    theSum += number
print("The sum is", theSum)

while True:
    number = int(input("Enter the numeric grade: "))
    if number >= 0 and number <= 100:
        break
    else:
        print("Error: grade must be between 100 and 0")
print(number)  # Just echo the valid input

done = False
while not done:
    number = int(input("Enter the numeric grade: "))
    if number >= 0 and number <= 100:
        done = True
    else:
        print("Error: grade must be between 100 and 0")
print(number)  # Just echo the valid input