fileName = input("Enter the file name: ")
f = open ("./part_5/" + fileName, 'r')
lines = f.readlines()
count = len(lines)
print("The file has ", count, " lines")

# loop to get numbers
numInput = input("Enter a line number [0 to quit]:")
while numInput != "0":
    x = eval(numInput)    # convert to int
    lineStrip = lines[x-1].strip()
    print(x, " :", lineStrip)
    print("The file has ", count, " lines")
    numInput = input("Enter a line number [0 to quit]:")

f.close()

