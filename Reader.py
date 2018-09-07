def reader(filename):

    FileOpen = open(filename,"r")
    ReadFile = FileOpen.readlines()
    FinalList = []

    for item in ReadFile:

        splititem= item.split()
        splititem0= int(splititem[0]) 
        splititem2= int(splititem[2])
        splititem3= int(splititem[3])
        splititem4= float(splititem[4])

        result01 = splititem0,splititem[1],splititem2,splititem3,splititem4
        FinalList.append(result01)

    return FinalList
    FileOpen.close()

#print: 
#[(1, 'assignment_1', 85, 100, 0.25), (2, 'test_1', 90, 100, 0.25), (3, 'exam_1', 95, 100, 0.5)]
print(reader("sample.cs1301"))

