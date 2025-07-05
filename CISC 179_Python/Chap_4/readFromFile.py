fileName = input ("Enter the file name: ")
f = open("./python/File/" + fileName, 'r')
#f = open("./python/File/data.txt","r")

lines = f.readlines()

print("Name\tHours\tTotal\n")
for line in lines:
    line = line.strip()
    print(line)

f.close()
