from math import sin, cos, atan, asin, acos, atan2, radians, degrees, sqrt

def find_net_force(ListT):
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

#Note that you should only need sin, cos, atan, degrees,
#radians, and sqrt: we've imported the others just in case you
#want to use them.

#print: (87.0, 54.4)

forces = [(10, 90), (10, -90), (100, 45), (20, 180)]
print(find_net_force(forces))

