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
    
    FinalDict = {}
    for items in FinalList:
        dic = {'total': items[3],'number': items[0],'grade': items[2],'weight': items[4]}
        FinalDict[items[1]]=dic
    
    return FinalDict

    FileOpen.close()    

#print (although the order of the keys may vary):
#{'assignment_1': {'total': 100, 'number': 1, 'grade': 85, 'weight': 0.25}, 'test_1': {'total': 100, 'number': 2, 'grade': 90, 'weight': 0.25}, 'exam_1': {'total': 100, 'number': 3, 'grade': 95, 'weight': 0.5}} 
print(reader("sample.cs1301"))
