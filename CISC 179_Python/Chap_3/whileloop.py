#while <condition>:
#    <sequence of statements>

#set the sum to 0.0
#input a string
#while the string is not the empty string
#    convert the string to a float
#    add the float to the sum
#    input a string
#print the sum

theSum = 0.0
data = input("Enter a number or just enter to quit: ")
while data != "":
    number = float(data)
    theSum += number
    data = input("Enter a number or just enter to quit: ")
print("The sum is", theSum)