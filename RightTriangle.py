import math

def  solve_right_triangle(opposite,adjacent,use_degrees=False):
    result0 = (opposite**2) + (adjacent**2)
    result01 = math.sqrt(result0)
    hs = opposite / adjacent
    atan = math.atan(hs)
    if use_degrees:
        sss = math.degrees(atan)
        return result01,sss
    else:
        return result01, atan
    

#(5.0, 0.6435011087932844)
#(5.0, 36.86989764584402)

print(solve_right_triangle(3.0, 4.0))
print(solve_right_triangle(3.0, 4.0, use_degrees = True))
