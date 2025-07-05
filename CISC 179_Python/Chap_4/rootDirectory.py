f = open("/Users/lambertk/parent/current/child/myfile.txt", 'r')

childFile = open("child/myfile.txt", 'r')
parentFile = open("../myfile.txt", 'r')
siblingFile = open("../sibling/myfile.txt", 'r')

import os
currentDirectoryPath = os.getcwd()
listOfFileNames = os.listdir(currentDirectoryPath)
for name in listOfFileNames:
    if ".py" in name:
        print(name)

os.rename("oldname.txt", "newname.txt")