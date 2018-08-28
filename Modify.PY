def modify_list(ss):
    ss.sort()    
    ss.reverse()
    del ss[-3:]
    try:
       ss.remove(7)
    except:
        pass
    
    ss[0] = ss[0]*2
    ss[2] = ss[2]*2
    return ss

import math
print(modify_list([7, 4, 3, 2.0, 81, 37.5, 89, math.pi, -2, math.e]))