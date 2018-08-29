def  average_heart_rate(ListInt):
    beats = 0
    count = 0

    for item in ListInt:
        if item >= 100:
            beats+=item
            count +=1
        else:
            pass
        
    result = beats // count
    return result

#print 114 (because there are 14 measurements from 102 to
#101, their sum is 1609, and 1609 // 14 is 114).
beats = [72, 77, 79, 95, 102, 105, 112, 115, 120, 121, 121,
         125, 125, 123, 119, 115, 105, 101, 96, 92, 90, 85]
print(average_heart_rate(beats))
