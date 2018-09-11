def find_median(filename):
    OpenFile = open(filename,'r')
    ReadList = []
    for item in OpenFile:
        ReadList.append(int(item))

    ReadList.sort()
    Final = ReadList
    for item in ReadList:
        if item % 2 == 1:
            s = len(ReadList) // 2
            Final =  ReadList[s]
            return Final
        elif item % 2 == 0:
            s = len(ReadList) // 2
            ss = s+1
            Final = ReadList[s] / ReadList[ss]
    return Final
#print: 16
print(find_median("FindMedianInput.txt"))