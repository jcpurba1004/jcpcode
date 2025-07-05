fileName = input ("Enter the file name: ")
with open('./part_4/' + fileName, 'r') as f:
	readData = f.read()

print(readData)
f.close()