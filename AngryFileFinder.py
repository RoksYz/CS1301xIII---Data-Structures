def angry_file_finder(filename):
    yn = False
    files = open(filename,"r")
    readfiles = files.readlines()
    for item in readfiles:
    #could >for item in files
        if "!" in item:
            yn = True
        else:
            return False
    return yn
    files.close()
#print: True
print(angry_file_finder("AngryFileFinderInput.txt"))

