def load_file(filename):
    files = open(filename,"r")
    filesread = files.readline()

    try:
        newfiles = int(filesread)
        return newfiles
    except ValueError:
        try:
            newfiles = float(filesread)
            return newfiles
        except ValueError:
            return filesread

            
    filesread.close()



#If your function works correctly, this will originally
#print 123, followed by <class 'int'>.
contents = load_file("LoadFromFileInput.txt")
print(contents)
print(type(contents))
