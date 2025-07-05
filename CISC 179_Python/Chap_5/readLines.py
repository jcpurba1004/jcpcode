# Put your code below:
fileName = input("Enter the file name: ")
f = open (fileName, 'r')

content = f.readlines()
count = len(content)
content = [x.strip() for x in content]
print("The file has ", count, " lines")

# loop to get numbers
numInput = input("Enter a line number [0 to quit]:")
while numInput != "0":
    x = eval(numInput)    # convert to int
    print(x, ":", content[x-1])
    print("The file has ", count, " lines")
    numInput = input("Enter a line number [0 to quit]:")

f.close()
