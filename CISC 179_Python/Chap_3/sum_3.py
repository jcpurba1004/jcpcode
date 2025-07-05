sum = 0.0
count = 0.0
data = input("Enter a number or press Enter to quit: ")
while data != "":
    number = float(data)
    sum += number
    count += 1.0
    data = input("Enter the number or press Enter to quit: ")
average = float(sum/count)
print("The sum is ",round(sum,1))
print("The average is ",round(average,1))