def format_checker(filename):
    FileOpen = open(filename,"r")
    ReadFile = FileOpen.readlines()
    count = 0
    countl = 0
    sums = 0
    for item in ReadFile:
        countl +=1
        splititem = item.split()
        try:
            if len(splititem) == 5:
                try:
                    splititem0= int(splititem[0]) 
                    splititem2= int(splititem[2])
                    splititem3= int(splititem[3])
                    if splititem[4].isdecimal:
                        sums+=float(splititem[4])
                        count+=1
                        
                    else:
                       return  False
                except:
                    return   False 
            else:
                return  False
        except:
            return  False
    
    if count == countl:
        if sums == 1.0:
            return True
        else:
            return False
    else:
        return False

    FileOpen.close()

#print: True, False .
print(format_checker("sample_1.cs1301"))
print(format_checker("sample_2.cs1301"))