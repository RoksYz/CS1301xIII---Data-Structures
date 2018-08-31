from math import sin, cos, tan, asin, acos, atan2, radians, degrees,sqrt

def find_net_force_from_file(filename):
    files = open(filename,'r')
    ListT = []

    for item in files:
        item = item.rstrip('\n')
        item = item.split()

        item0 = int(item[0])
        item1 = int(item[1])
        finalitem = item0,item1
        
        tupleitem = tuple(finalitem)
        ListT.append(tupleitem)

    HC = 0
    VC = 0
    for s in ListT:
        s0 = radians(s[0])
        s1 = radians(s[1])

        HC +=s0*cos(s1)
        VC +=s0*sin(s1)
    
    ResultMagnitude = sqrt(HC**2 + VC**2)
    DeMagnitude = degrees(ResultMagnitude)

    ResultAngle = atan2(VC,HC)
    deAngle = degrees(ResultAngle)
    
    return round(DeMagnitude,1),round(deAngle,1)

    files.close()


#print: (87.0, 54.4)
print(find_net_force_from_file("a_few_angles.txt"))
