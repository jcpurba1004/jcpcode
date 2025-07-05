# Edit the code below
sum = 0.0
count = 0
data = input("Enter a number or press Enter to quit: ")
while data != "":
    number = float(data)
    sum += number
    print("number: ", number,"; theSum: ", sum)
    count += 1
    data = input("Enter the number or press Enter to quit: ")
average = float(sum/count)
print("The sum is", sum)
print("The average is ", average)