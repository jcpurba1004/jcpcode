fileName = input ("Enter the file name:")
f = open(fileName, 'r')

lines = f.readlines()

print("Name Hours Total")
for line in lines:
    print(line)

f.close()