
def replace_all(target,find_string,replace_string):
    target = target.split()
    result = ""
    space = " "
    for s in target:
        if s == find_string:
            s = replace_string
        result+= s
        result+= space 
    
    return result

target = "In case I don't see ya, good afternoon, good evening, and good night!"
find = "good"
replace = "bad"
print(replace_all(target, find, replace))
