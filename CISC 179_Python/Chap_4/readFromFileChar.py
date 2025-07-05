fileName = input ("Enter the file name: ")
f = open("./part_4/" + fileName, 'r')

lines = f.readlines()

#print("Name\tHours\tTotal\n")
for line in lines:
    for ch in line:
        print(ch)
f.close()
