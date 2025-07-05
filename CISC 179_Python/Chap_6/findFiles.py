function findFiles(target, path)
    files = []
    lyst = os.listdir(path)
    for element in lyst
        if os.path.isfile(element):
            if target in element:
                files.append(path + os.sep + element)
            else: 
                os.chdir(element)
        files.extend(findFiles(target, os.getcwd()))
        os.chdir("..")
    return files