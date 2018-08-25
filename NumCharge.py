
def num_changer(s):  
    even = ""
    odd = ""
    for l in s[1:9:2]:
        even+=l

        
    for l in s[0:9:2]:
        odd+=l
    
    even = int(even)
    odd = int(odd)
    result = even+odd
    return result
        
string_int = "123456"
result = num_changer(string_int)
print(string_int + " -> " + str(result))
