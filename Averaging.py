def average_file(filename):
    files = open(filename,"r")

    
    result = 0
    fileslen = 0 

    try:
        for item in files:
            result += int(item)
            fileslen+= 1
        return result / fileslen
    except:
        return "Error reading file!"
    
    files.close()

#print: 5.0, then Error reading file!
print(average_file("ValidFile.txt"))
print(average_file("InvalidFile.txt"))