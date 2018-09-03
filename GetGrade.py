def get_grade(filename):
    FileOpen = open(filename,"r")
    ReadFile = FileOpen.readlines()
    Result0 = 0

    for item in ReadFile:

        splititem= item.split()
        splititem0= int(splititem[0]) 
        splititem2= int(splititem[2])
        splititem3= int(splititem[3])
        splititem4= float(splititem[4])

        count = (splititem2 / splititem3) * splititem4 * 100
        Result0+=count
    
    return Result0
    FileOpen.close()
#print: 91.55 
print(get_grade("samplegetgrade.cs1301"))