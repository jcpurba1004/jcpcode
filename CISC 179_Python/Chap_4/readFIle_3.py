fileName = input ("Enter the file name:")
f = open(fileName, 'r')

lines = f.readlines()

print("Name\tHours\tTotal\n")
for line in lines:
    lineSplit = line.split()
    print(str(lineSplit[0]), int(lineSplit[1]), float(lineSplit[2]))

f.close()